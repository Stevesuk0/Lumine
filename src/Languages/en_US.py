from enum import Enum

class Text(Enum):
    language_name = 'English (US)'
    translate_by = 'Stevesuk0 <stevesukawa@outlook.com>'

    # Basic
    app_name = "Lumine"
    about_detail = "Lumine is an open-source thermal controller for Dell and Alienware systems."
    already_started = "Another instance of Lumine is already running."
    already_started_detailed = "Please use the existing instance or close it before launching a new one."
    
    # Welcome
    welcome_title = "Welcome to Lumine {version}!"

    # Configuration
    config_reloaded_title = "Configuration reloaded"
    config_reloaded_msg = "Configuration is reloaded.\nSee more in the Lumine app."
    
    # Update check
    update_new_title = "New version detected!"
    update_new_msg = "A new version of Lumine is available ({latest}).\nClick this pop-up to view the download link."
    update_latest_title = "You're up to date!"
    update_latest_msg = "Lumine is already on the latest version. ({version})"
    
    # About window
    about_title = "About Lumine"
    about_message = "Lumine {version} by {author}"
    
    # Tray menu
    tray_show_window = "Show Window"
    tray_reload_config = "Reload Configuration"
    tray_toggle_theme = "Toggle Theme"
    tray_check_updates = "Check Updates..."
    tray_exit = "Exit"

    # Modes
    mode_balanced = "Balanced"
    mode_gmode = "G-Mode"
    mode_custom = "Custom"
    mode_changed_title = "Mode changed"
    mode_balanced_msg = "Balanced mode activated.\nSee more in the Lumine app."
    mode_gmode_msg = "G-Mode activated.\nSee more in the Lumine app."

    # UI texts
    rpm = 'RPM'
    failsafe_label = "Thermal Bypass"
    fan_speed = "Fan Speed"

    example_config = """# Lumine Configuration
# Reload configuration at the application tray.

# Do NOT modify this value.
# This is the application version of Lumine.
lumine_version: v1.4

# Update interval for hardware information.
# Unit: milliseconds.
update_interval: 1000

# Time (in seconds) after which G-Mode will be automatically disabled
# when the system is no longer overheating.
# Unit: seconds.
disable_protect_after: 30

# UI color configuration
colors:
  temp: '#98C379' # Temperature text color
  fan: '#61AFEF' # Fan speed color
  normal: '#98C379' # Normal status color
  warning: '#E5C07B' # Warning status color
  overheat: '#E06C75' # Overheat status color

# UI font
font: Segoe UI

# Temperature thresholds (°C)
# When temperature reaches or exceeds these values,
# the system enters G-Mode.
temp_overheat:
  - 95  # CPU overheat threshold (°C)
  - 85  # GPU overheat threshold (°C)

# Warning threshold [CPU, GPU]
# When temperature reaches or exceeds these values,
# the system enters WARNING state.
temp_warning:
  - 85  # CPU warning threshold (°C)
  - 72  # GPU warning threshold (°C)

# Hotkey system
# - Based on system virtual key codes (keyboard library: https://github.com/boppreh/keyboard)
# - Supports multi-key binding / combination detection
# - Hardware-specific keys are allowed.

g_mode_hotkey: f17
balanced_hotkey: f20"""