from enum import Enum

class Text(Enum):
    language_name = '繁體中文'
    translate_by = 'Claude <noreply@anthropic.com>'

    # Basic
    app_name = "Lumine"
    about_detail = "Lumine 是一款適用於 Dell 和 Alienware 系統的開源散熱控制工具。"
    already_started = "Lumine 的另一個執行個體已在執行中。"
    already_started_detailed = "請使用已開啟的執行個體，或先關閉舊的執行個體後再重新啟動。"

    # Welcome
    welcome_title = "歡迎使用 Lumine {version}！"

    # Configuration
    config_reloaded_title = "設定已重新載入"
    config_reloaded_msg = "設定已重新載入。\n請在 Lumine 應用程式中查看更多資訊。"

    # Update check
    update_new_title = "發現新版本！"
    update_new_msg = "偵測到 Lumine 有新版本可用（{latest}）。\n點擊此通知查看下載連結。"
    update_latest_title = "已是最新版本"
    update_latest_msg = "Lumine 已是最新版本（{version}）"

    # About window
    about_title = "關於 Lumine"
    about_message = "Lumine {version} 由 {author} 開發"

    # Tray menu
    tray_show_window = "顯示視窗"
    tray_reload_config = "重新載入設定"
    tray_edit_config = "編輯設定檔..."
    tray_toggle_theme = "切換主題"
    tray_check_updates = "檢查更新..."
    tray_start_on_startup = "設定開機自動啟動"
    tray_exit = "結束"

    # Modes
    mode_balanced = "均衡模式"
    mode_gmode = "G-Mode"
    mode_custom = "自訂"
    mode_changed_title = "模式已切換"
    mode_balanced_msg = "已啟用均衡模式。\n請在 Lumine 應用程式中查看更多資訊。"
    mode_gmode_msg = "已啟用 G-Mode。\n請在 Lumine 應用程式中查看更多資訊。"

    # UI texts
    rpm = '轉/分'
    failsafe_label = "散熱保護旁路"
    fan_speed = "風扇轉速"

    example_config = """# Lumine 設定檔
# 在系統匣中重新載入設定即可生效。

# 請勿修改此值。
# Lumine 應用程式版本號。
lumine_version: v1.4

# 硬體資訊更新間隔
# 單位：毫秒
update_interval: 1000

# 系統恢復正常後，G-Mode 自動關閉的延遲時間
# 單位：秒
disable_protect_after: 30

# UI 顏色設定
colors:
  temp: '#98C379' # 溫度文字顏色
  fan: '#61AFEF' # 風扇速度顏色
  normal: '#98C379' # 正常狀態顏色
  warning: '#E5C07B' # 警告狀態顏色
  overheat: '#E06C75' # 過熱狀態顏色

# UI 字型
font: Segoe UI

# 溫度閾值（°C）
# 達到或超過該溫度時進入 G 模式
temp_overheat:
  - 95  # CPU 過熱閾值（°C）
  - 85  # GPU 過熱閾值（°C）

# 警告閾值 [CPU, GPU]
# 達到或超過該溫度時進入警告狀態
temp_warning:
  - 85  # CPU 警告閾值（°C）
  - 72  # GPU 警告閾值（°C）

# 熱鍵系統
# - 基於系統虛擬鍵碼（keyboard 函式庫：https://github.com/boppreh/keyboard）
# - 支援組合鍵
# - 支援硬體特殊按鍵

g_mode_hotkey: f17
balanced_hotkey: f20
"""
