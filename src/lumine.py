import sys
import os
import tempfile
import threading
import keyboard
from PIL import Image
from winotify import Notification
import maliang
import maliang.theme
from Backend import AWCCThermal, DetectHardware, Configuration
from pystray import Icon, Menu, MenuItem


def create_lock():
    name = os.path.splitext(os.path.abspath(sys.argv[0]))[0]
    lock_path = os.path.join(tempfile.gettempdir(), name.replace("\\", "-") + ".lock")
    if os.path.exists(lock_path):
        raise PermissionError("Another instance is already running.")
    os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_RDWR)


class LumineApp:
    def __init__(self):
        self.size = (900, 270)
        self.version = 'v1.0'

        self.config = Configuration.use('config')

        if Configuration.get(self.config, 'lumine_version', None) is None:
            Configuration.set(self.config, 'lumine_version', 'v1.0')
            Configuration.set(self.config, 'update_interval', 1000)
            Configuration.set(self.config, 'failsafe_cpu', 95)
            Configuration.set(self.config, 'failsafe_gpu', 85)
            Configuration.set(self.config, 'disable_protect_after', 1000)
            Configuration.set(self.config, 'colors', {
                    "temp": "#98C379",
                    "fan": "#61AFEF",
                    "bg": "#202020",
                    "outline": "#282C34"
                }
            )

            Configuration.sync(self.config)
            

        self.root = maliang.Tk(size=self.size, position=(-1000, -1000))
        self.root.title("Lumine")
        self.root.icon(maliang.PhotoImage(Image.open("icons/icon.png").resize((64, 64))))
        maliang.theme.customize_window(self.root, disable_maximize_button=True)

        self.awcc = AWCCThermal.AWCCThermal()
        self.hardware = DetectHardware.DetectHardware()
        self.current_mode = 0
        self.failsafe = False
        self.failsafe_activated = False
        self.keypressed_mode = None

        self.build_ui()
        self.bind_hotkeys()
        self.start_tray()
        self.schedule_update()

    def build_ui(self):
        size = self.size
        cv = maliang.Canvas(self.root)
        cv.place(x=0, y=0, width=size[0], height=size[1])
        self.cv = cv
        self.build_gpu_ui()
        self.build_cpu_ui()
        self.build_controls()

    def build_gpu_ui(self):
        hw = self.hardware
        self.ui_gpu_temp = maliang.ProgressBar(self.cv, position=(25, 45), size=(310, 40))
        self.ui_gpu_temp_text = maliang.Text(self.cv, position=(350, 55), fontsize=18)
        maliang.Text(self.cv, position=(25, 15), text=hw.getHardwareName(hw.GPUFanIdx), fontsize=18)

    def build_cpu_ui(self):
        prefix = self.size[0] // 2 - 20
        hw = self.hardware
        self.ui_cpu_temp = maliang.ProgressBar(self.cv, position=(prefix + 25, 45), size=(310, 40))
        self.ui_cpu_temp_text = maliang.Text(self.cv, position=(prefix + 350, 55), fontsize=18)
        maliang.Text(self.cv, position=(prefix + 25, 15), text=hw.getHardwareName(hw.CPUFanIdx), fontsize=18)

    def build_controls(self):
        self.ui_modeset = maliang.SegmentedButton(
            self.cv, position=(25, 205),
            text=("Balanced", "Turbo", "Custom"),
            fontsize=18,
            command=self.set_mode,
            default=0
        )
        self.ui_failsafe = maliang.ToggleButton(
            self.cv, position=(self.size[0] - 195, 205),
            size=(100, 35),
            text=("Fail-Safe",),
            fontsize=18,
            command=lambda v: setattr(self, "failsafe", v)
        )
        self.ui_failsafe_status = maliang.Label(
            self.cv, position=(self.size[0] - 85, 205), size=(50, 35)
        )

    def start_tray(self):
        def tray_thread():
            icon = Icon("Lumine", icon=Image.open("icons/app.png").resize((64, 64)), menu=Menu(
                MenuItem("Lumine v1.0", lambda: None),
                Menu.SEPARATOR,
                MenuItem("Show Window", self.show_window),
                MenuItem("Reload Configuration", self.reload_config),
                MenuItem("Exit", self.root.destroy)
            ))
            icon.run()
        threading.Thread(target=tray_thread, daemon=True).start()

    def reload_config(self):
        self.config = Configuration.use('config')

    def bind_hotkeys(self):
        keyboard.add_hotkey("f17", lambda: self.switch_mode(1)) # Turbo mode
        keyboard.add_hotkey("f20", lambda: self.switch_mode(0)) # Balanced mode

    def switch_mode(self, mode):
        self.keypressed_mode = mode

    def schedule_update(self):
        self.update_info()
        self.root.after(Configuration.get(self.config, "update_interval", 1000), self.schedule_update)

    def update_info(self):
        try:
            gpu_temp = self.awcc.getFanRelatedTemp(self.hardware.GPUFanIdx)
            cpu_temp = self.awcc.getFanRelatedTemp(self.hardware.CPUFanIdx)
        except Exception as e:
            print("Error reading hardware:", e)
            return

        self.ui_gpu_temp.set(gpu_temp / 95)
        self.ui_gpu_temp_text.set(f"{gpu_temp} °C")
        self.ui_cpu_temp.set(cpu_temp / 110)
        self.ui_cpu_temp_text.set(f"{cpu_temp} °C")

        if self.failsafe:
            self.check_overheat(cpu_temp, gpu_temp)

        if self.keypressed_mode is not None:
            self.set_mode(self.keypressed_mode)
            self.keypressed_mode = None

    def check_overheat(self, cpu_temp, gpu_temp):
        if gpu_temp > Configuration.get(self.config, "failsafe_gpu", 85) or cpu_temp > Configuration.get(self.config, "failsafe_cpu", 95):
            if not self.failsafe_activated:
                Notification(app_id="Lumine",
                             title="System overheat!",
                             msg="Detected overheating. Switching mode...",
                             icon=os.path.abspath("icons/performance.png")).show()
                self.set_mode(1)
                self.failsafe_activated = True
                self.root.after(Configuration.get(self.config, "disable_protect_after", 30) * 1000, self.disable_overheat)
        else:
            self.failsafe_activated = False

    def disable_overheat(self):
        self.set_mode(0)
        self.failsafe_activated = False

    def set_mode(self, mode):
        self.current_mode = mode
        match mode:
            case 0:
                self.awcc.setMode(self.awcc.Mode.Balanced)
            case 1:
                self.awcc.setMode(self.awcc.Mode.G_Mode)
            case 2:
                self.awcc.setMode(self.awcc.Mode.Custom)

    def show_window(self):
        self.root.deiconify()
        self.root.topmost(True)
        self.root.topmost(False)


def main():
    try:
        create_lock()
    except PermissionError as e:
        print(e)
        sys.exit(1)

    app = LumineApp()
    app.root.mainloop()


if __name__ == "__main__":
    main()
