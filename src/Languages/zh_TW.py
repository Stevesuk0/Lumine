from enum import Enum

class Text(Enum):
    language_name = '中文，繁體 (中国台灣、香港特别行政区)'
    translate_by = 'Stevesuk0 <stevesukawa@outlook.com>'

    app_name = "Lumine"
    about_detail = "Lumine 是一個開源的 Dell / Alienware 系統溫度控制程式。"

    welcome_title = "歡迎使用 Lumine {version}！"
    welcome_desc = "恭喜，終於擺脫 AWCC 了。"

    config_reloaded_title = "設定檔已重新載入"
    config_reloaded_msg = "設定檔已成功重新載入。\n可在 Lumine 應用程式中查看更多資訊。"

    update_new_title = "偵測到新版本！"
    update_new_msg = "Lumine 有新版本可用（{latest}）。\n點擊此通知以查看下載連結。"
    update_latest_title = "已是最新版本"
    update_latest_msg = "目前的 Lumine 已是最新版本（{version}）。"

    about_title = "關於 Lumine"
    about_message = "Lumine {version}，作者：{author}"

    tray_show_window = "顯示視窗"
    tray_reload_config = "重新載入設定"
    tray_toggle_theme = "切換主題"
    tray_check_updates = "檢查更新..."
    tray_exit = "退出程式"

    mode_balanced = "平衡模式"
    mode_gmode = "G-Mode"
    mode_custom = "自訂模式"
    mode_changed_title = "模式已切換"
    mode_balanced_msg = "已切換至平衡模式。\n可在 Lumine 應用程式中查看更多資訊。"
    mode_gmode_msg = "已切換至 G-Mode。\n可在 Lumine 應用程式中查看更多資訊。"

    overheat_title = "系統過熱警告！"
    overheat_msg = "偵測到系統溫度過高。\n請打開 Lumine 檢視詳細資訊。"

    rpm = "轉/分"
    failsafe_label = "停用過熱保護"
    fan_speed = "風扇速度"