from enum import Enum

class Text(Enum):
    language_name = 'English (US)'
    translate_by = 'Stevesuk0 <stevesukawa@outlook.com>'

    # Basic
    app_name = "Lumine"
    about_detail = "Lumine is an open-source thermal controller for Dell and Alienware systems."
    
    # Welcome
    welcome_title = "Welcome to Lumine {version}!"
    welcome_desc = "Congrats, finally free from AWCC, huh?"

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

    # Overheat protect
    overheat_title = "System overheat!"
    overheat_msg = "Detected your computer is overheating. \nSee more in the Lumine app."

    # UI texts
    rpm = 'RPM'
    failsafe_label = "Thermal Bypass"
    fan_speed = "Fan Speed"