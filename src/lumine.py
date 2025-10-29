import sys
import os
import threading
import keyboard
from PIL import Image
from winotify import Notification
import maliang
import maliang.theme
from Backend import AWCCThermal, DetectHardware, Configuration
from pystray import Icon, Menu, MenuItem
        
class LumineApp:
    def __init__(self):
        self.size = (900, 270)
        self.version = 'v1.0.1'

        self.config = Configuration.use('config')

        if Configuration.get(self.config, 'lumine_version', None) is None:
            Configuration.set(self.config, 'lumine_version', 'v1.0')
            Configuration.set(self.config, 'update_interval', 1000)
            Configuration.set(self.config, 'disable_protect_after', 30)
            Configuration.set(self.config, 'colors', {
                    "temp": "#98C379",
                    "fan": "#61AFEF",
                    "bg": "#202020",
                    "outline": "#282C34",
                    "normal": "#98C379",
                    "warning": "#E5C07B",
                    "overheat": "#E06C75",
                }
            )
            Configuration.set(self.config, 'font', 'Segoe UI')
            Configuration.set(self.config, 'temp_overheat', (85, 95))
            Configuration.set(self.config, 'temp_warning', (72, 85))

            Configuration.sync(self.config)

        self.awcc = AWCCThermal.AWCCThermal()
        self.hardware = DetectHardware.DetectHardware()
        
        self.current_mode = 0
        self.original_mode = 0
        self.keypressed_mode = None
        
        self.failsafe = True
        self.failsafe_activated = False

        self.awccthermal = AWCCThermal.AWCCThermal()
        self.awccwrapper = self.awccthermal._awcc
        self.hardware = DetectHardware.DetectHardware()

        self.gpu_name = self.hardware.getHardwareName(self.hardware.GPUFanIdx)
        self.cpu_name = self.hardware.getHardwareName(self.hardware.CPUFanIdx)

        self.failsafe_cpu = Configuration.get(self.config, 'failsafe_cpu')
        self.failsafe_gpu = Configuration.get(self.config, 'failsafe_gpu')
        self.disable_protect_after = Configuration.get(self.config, 'disable_protect_after')
        
        self.create_window()
        self.show_widgets()

        self.root.after(Configuration.get(self.config, 'update_interval', 1000), self.update_info)
        self.root.protocol("WM_DELETE_WINDOW", self.root.withdraw)

        keyboard.add_hotkey('f17', callback=lambda: self.add_mode_event(1))
        keyboard.add_hotkey('f20', callback=lambda: self.add_mode_event(0))
        
        self.set_mode(0)

        threading.Thread(target=self.show_tray, daemon=True).start()

        self.root.mainloop()

    def add_mode_event(self, mode):
        self.keypressed_mode = mode

    def show_window(self):
        self.root.deiconify()
        self.root.topmost(True)
        self.root.topmost(False)

    def reload_config(self):
        self.config = Configuration.use('config')

        toast = Notification(app_id="Lumine",
            title="Configuration reloaded",
            msg="Configuration is reloaded.\nSee more in the Lumine app.",
            icon=os.path.abspath('icons/balanced.png'),
        )
        
        toast.show()

    def show_about(self):
        maliang.TkMessage(
            title='About Lumine',
            message=f'Lumine {self.version} by @Stevesuk0',
            detail='A open-source thermal controller for Dell and Alienware systems.',
            option='ok'
        )

    def show_tray(self):
        self.tray = Icon("TkTray", icon=Image.open('icons/icon.png').resize((64, 64)), menu=Menu(
            MenuItem(text=f'Lumine {self.version}', action=self.show_about),
            Menu.SEPARATOR,
            MenuItem('Show Window', self.show_window, default=True),
            MenuItem('Reload Configuration', self.reload_config),
            MenuItem('Exit', self.root.destroy)
        ))
        self.tray.run()

    def create_window(self):
        self.root = maliang.Tk(size=self.size)
        self.root.title("Lumine")
        self.root.icon(maliang.PhotoImage(Image.open("icons/icon.png").resize((64, 64))))
        maliang.theme.customize_window(self.root, disable_maximize_button=True)

        self.root.maxsize(*self.size)
        self.root.minsize(*self.size)

    def show_widgets(self):
        self.cv = maliang.Canvas(self.root)
        self.cv.place(x=0, y=0, width=self.size[0], height=self.size[1])

        maliang.configs.Env.system = 'Windows10'
        self.ui_gpu_name = maliang.Text(self.cv, position=(25, 15), text=self.gpu_name, fontsize=18, family=Configuration.get(self.config, 'font', 'Segoe UI'))
        self.ui_gpu_temp = maliang.ProgressBar(self.cv, position=(25, 45), size=(310, 40))
        self.ui_gpu_temp_text = maliang.Text(self.cv, position=(350, 55), fontsize=18, family=Configuration.get(self.config, 'font', 'Segoe UI'))
        self.ui_gpu_fan = maliang.ProgressBar(self.cv, position=(25, 95), size=(310, 40))
        self.ui_gpu_fan_text = maliang.Text(self.cv, position=(350, 105), fontsize=18, family=Configuration.get(self.config, 'font', 'Segoe UI'))

        ui_cpu_prefix = self.size[0] // 2 - 20

        self.ui_cpu_name = maliang.Text(self.cv, position=(ui_cpu_prefix + 25, 15), text=self.cpu_name, fontsize=18, family=Configuration.get(self.config, 'font', 'Segoe UI'))
        self.ui_cpu_temp = maliang.ProgressBar(self.cv, position=(ui_cpu_prefix + 25, 45), size=(310, 40))
        self.ui_cpu_temp_text = maliang.Text(self.cv, position=(ui_cpu_prefix + 350, 55), fontsize=18, family=Configuration.get(self.config, 'font', 'Segoe UI'))
        self.ui_cpu_fan = maliang.ProgressBar(self.cv, position=(ui_cpu_prefix + 25, 95), size=(310, 40))
        self.ui_cpu_fan_text = maliang.Text(self.cv, position=(ui_cpu_prefix + 350, 105), fontsize=18, family=Configuration.get(self.config, 'font', 'Segoe UI'))

        maliang.configs.Env.system = 'Windows11'
        self.ui_gpu_fan_slider = maliang.Slider(self.cv, position=(25, 150), size=(310, 40), default=0.5)
        self.ui_gpu_fan_slider.bind_on_update(self.set_fan)
        self.ui_gpu_fan_slitext = maliang.Text(self.cv, position=(349, 155), text='Fan Speed', fontsize=18, family=Configuration.get(self.config, 'font', 'Segoe UI'))

        self.ui_cpu_fan_slider = maliang.Slider(self.cv, position=(ui_cpu_prefix + 25, 150), size=(310, 40), default=0.5)
        self.ui_cpu_fan_slider.bind_on_update(self.set_fan)
        self.ui_cpu_fan_slitext = maliang.Text(self.cv, position=(ui_cpu_prefix + 349, 155), text='Fan Speed', fontsize=18, family=Configuration.get(self.config, 'font', 'Segoe UI'))

        self.ui_modeset = maliang.SegmentedButton(self.cv, position=(25, 205), text=("Balanced", "Turbo", "Custom"), fontsize=18, family=Configuration.get(self.config, 'font', 'Segoe UI'), command=self.set_mode, default=0)
        
        for i in self.ui_modeset.children:
            i.style.set(bg=('#2B2B2B', '#3C3C3C', '#323232', '#3C3C3C', '#3C3C3C', '#323232'), ol=('', '', '', '', '', ''))

        self.ui_failsafe = maliang.ToggleButton(self.cv, position=(self.size[0] - 195, 205), size=(100, self.ui_modeset.size[1]), text=("Override"), fontsize=18, family=Configuration.get(self.config, 'font', 'Segoe UI'), command=self.toggle_failsafe)
        self.ui_failsafe_status = maliang.Label(self.cv, position=(self.size[0] - 85, 205), size=(50, self.ui_modeset.size[1]))

    def disable_overheat(self):
        self.set_mode(self.original_mode)
        self.ui_modeset.set(self.original_mode)

        self.failsafe_activated = False

        self.current_mode = self.original_mode

    def update_info(self):
        gpu_fan_id = self.awccthermal._fanIdsAndRelatedSensorsIds[self.hardware.GPUFanIdx][0]
        cpu_fan_id = self.awccthermal._fanIdsAndRelatedSensorsIds[self.hardware.CPUFanIdx][0]

        self.ui_gpu_temp.set(self.awccthermal.getFanRelatedTemp(self.hardware.GPUFanIdx) / 95)
        self.ui_gpu_temp_text.set(f'{self.awccthermal.getFanRelatedTemp(self.hardware.GPUFanIdx)} °C')
        self.ui_gpu_fan.set(self.awccthermal._awcc.GetFanRPM(gpu_fan_id) / 5500)
        self.ui_gpu_fan_text.set(f'{self.awccthermal._awcc.GetFanRPM(gpu_fan_id)} RPM')

        self.ui_cpu_temp.set(self.awccthermal.getFanRelatedTemp(self.hardware.CPUFanIdx) / 110)
        self.ui_cpu_temp_text.set(f'{self.awccthermal.getFanRelatedTemp(self.hardware.CPUFanIdx)} °C')
        self.ui_cpu_fan.set(self.awccthermal._awcc.GetFanRPM(cpu_fan_id) / 5500)
        self.ui_cpu_fan_text.set(f'{self.awccthermal._awcc.GetFanRPM(cpu_fan_id)} RPM')

        colors = Configuration.get(self.config, 'colors', {
                        "temp": "#98C379",
                        "fan": "#61AFEF",
                        "bg": "#202020",
                        "outline": "#282C34",
                        "normal": "#98C379",
                        "warning": "#E5C07B",
                        "overheat": "#E06C75"
                    }
                )
        
        color_tempbar = colors['temp']
        color_fanbar = colors['fan']
        color_barbg = colors['bg']
        color_barol = colors['outline']
        color_normal = colors['normal']
        color_warning = colors['warning']
        color_overheat = colors['overheat']

        self.ui_gpu_temp.style.set(
            bg_bar  = (color_tempbar, color_tempbar), 
            ol_bar  = (color_tempbar, color_tempbar), 
            bg_slot = (color_barbg, color_barbg), 
            ol_slot = (color_barol, color_barol),
        )

        self.ui_cpu_temp.style.set(
            bg_bar  = (color_tempbar, color_tempbar), 
            ol_bar  = (color_tempbar, color_tempbar), 
            bg_slot = (color_barbg, color_barbg), 
            ol_slot = (color_barol, color_barbg),
        )

        self.ui_gpu_fan.style.set(
            bg_bar  = (color_fanbar, color_fanbar), 
            ol_bar  = (color_fanbar, color_fanbar), 
            bg_slot = (color_barbg, color_barbg), 
            ol_slot = (color_barol, color_barol),
        )
        
        self.ui_cpu_fan.style.set(
            bg_bar  = (color_fanbar, color_fanbar), 
            ol_bar  = (color_fanbar, color_fanbar), 
            bg_slot = (color_barbg, color_barbg), 
            ol_slot = (color_barol, color_barol),
        )

        overheat_level = Configuration.get(self.config, 'temp_overheat', (85, 95))
        warning_level = Configuration.get(self.config, 'temp_warning', (72, 85))

        self.failsafe_gpu = overheat_level[0]
        self.failsafe_cpu = overheat_level[1]

        self.warning_gpu = warning_level[0]
        self.warning_cpu = warning_level[1]

        gpu_temp = self.awccthermal.getFanRelatedTemp(self.hardware.GPUFanIdx)
        cpu_temp = self.awccthermal.getFanRelatedTemp(self.hardware.CPUFanIdx)

        overheat = gpu_temp > self.failsafe_gpu or cpu_temp > self.failsafe_cpu

        if gpu_temp >= self.warning_gpu:
            if not self.failsafe_activated:
                self.ui_failsafe_status.style.set(bg=(color_warning, color_warning)) 
            self.ui_gpu_temp.style.set(
                bg_bar  = (color_warning, color_warning), 
                ol_bar  = (color_warning, color_warning), 
                bg_slot = (color_barbg, color_barbg), 
                ol_slot = (color_barol, color_barol),
            )
        if gpu_temp >= self.failsafe_gpu:
            self.ui_gpu_temp.style.set(
                bg_bar  = (color_overheat, color_overheat), 
                ol_bar  = (color_overheat, color_overheat), 
                bg_slot = (color_barbg, color_barbg), 
                ol_slot = (color_barol, color_barol),
            )
        if cpu_temp >= self.warning_cpu:
            if not self.failsafe_activated:
                self.ui_failsafe_status.style.set(bg=(color_warning, color_warning)) 
            self.ui_cpu_temp.style.set(
                bg_bar  = (color_warning, color_warning), 
                ol_bar  = (color_warning, color_warning), 
                bg_slot = (color_barbg, color_barbg), 
                ol_slot = (color_barol, color_barol),
            )
        if cpu_temp >= self.failsafe_cpu:
            self.ui_cpu_temp.style.set(
                bg_bar  = (color_overheat, color_overheat), 
                ol_bar  = (color_overheat, color_overheat), 
                bg_slot = (color_barbg, color_barbg), 
                ol_slot = (color_barol, color_barol),
            )


        if self.failsafe:
            if overheat:
                if not self.failsafe_activated:
                    toast = Notification(app_id="Lumine",
                        title="System overheat!",
                        msg="Detected your computer is overheating. \nSee more in the Lumine app.",
                        icon=os.path.abspath('icons/performance.png'),
                    )
                    
                    toast.show()
                    self.failsafe_activated = True

                    self.ui_failsafe_status.style.set(bg=(color_overheat, color_overheat))
                    self.original_mode = self.current_mode
                    self.awccthermal.setMode(self.awccthermal.Mode.G_Mode)
                    self.ui_modeset.set(1)

                    self.root.after(Configuration.get(self.config, 'disable_protect_after', 30) * 1000, self.disable_overheat)
            else:
                if not self.failsafe_activated:
                    self.ui_failsafe_status.style.set(bg=(color_normal, color_normal)) 
        else:
            self.ui_failsafe_status.style.set(bg=('#2B2B2B', '#2B2B2B')) 

        if not self.keypressed_mode is None:
            match self.keypressed_mode:
                case 0:
                    toast = Notification(app_id="Lumine",
                        title="Mode changed",
                        msg="Balanced mode activated.\nSee more in the Lumine app.",
                        icon=os.path.abspath('icons/balanced.png'),
                    )
                    
                    toast.show()

                case 1:
                    toast = Notification(app_id="Lumine",
                        title="Mode changed",
                        msg="Turbo mode activated.\nSee more in the Lumine app.",
                        icon=os.path.abspath('icons/performance.png'),
                    )
                    
                    toast.show()

            self.set_mode(self.keypressed_mode)
            self.ui_modeset.set(self.keypressed_mode)
            self.keypressed_mode = None

        self.root.after(Configuration.get(self.config, 'update_interval'), self.update_info)

    def set_fan(self, type, _):
        if type == 'normal':
            self.awccthermal.setMode(self.awccthermal.Mode.Custom)

            cpu_speed = int(self.ui_cpu_fan_slider.get() * 127)
            gpu_speed = int(self.ui_gpu_fan_slider.get() * 127)

            self.awccthermal.setFanSpeed(self.hardware.CPUFanIdx, cpu_speed)
            self.awccthermal.setFanSpeed(self.hardware.GPUFanIdx, gpu_speed)

    def set_mode(self, value):
        self.current_mode = value

        self.ui_gpu_fan_slider.disable(True)
        self.ui_cpu_fan_slider.disable(True)

        match value:
            case 0:
                self.awccthermal.setMode(self.awccthermal.Mode.Balanced)
            case 1:
                self.awccthermal.setMode(self.awccthermal.Mode.G_Mode)
            case 2:
                self.ui_gpu_fan_slider.disable(False)
                self.ui_cpu_fan_slider.disable(False)
                self.awccthermal.setMode(self.awccthermal.Mode.Custom)
                self.set_fan('normal')

    def toggle_failsafe(self, value):
        self.failsafe = not value

if __name__ == "__main__":
    LumineApp()