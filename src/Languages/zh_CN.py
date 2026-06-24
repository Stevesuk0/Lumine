from enum import Enum

class Text(Enum):
    language_name = '简体中文'
    translate_by = 'Stevesuk0 <stevesukawa@outlook.com>'

    # Basic
    app_name = "Lumine"
    about_detail = "Lumine 是一款适用于 Dell 和 Alienware 系统的开源散热控制工具。"
    already_started = "Lumine 的另一个实例已经在运行。"
    already_started_detailed = "请使用已打开的实例，或者先关闭先前的实例后再重新启动。"
    
    # Welcome
    welcome_title = "欢迎使用 Lumine {version}！"

    # Configuration
    config_reloaded_title = "配置已重新加载"
    config_reloaded_msg = "配置已重新加载。\n请在 Lumine 应用中查看更多信息。"
    
    # Update check
    update_new_title = "发现新版本！"
    update_new_msg = "检测到 Lumine 有新版本可用（{latest}）。\n点击此弹窗查看下载链接。"
    update_latest_title = "已是最新版本"
    update_latest_msg = "Lumine 已是最新版本（{version}）"
    
    # About window
    about_title = "关于 Lumine"
    about_message = "Lumine {version} 由 {author} 开发"
    
    # Tray menu
    tray_show_window = "显示窗口"
    tray_reload_config = "重新加载配置"
    tray_edit_config = "编辑配置文件..."
    tray_toggle_theme = "切换主题"
    tray_check_updates = "检查更新..."
    tray_start_on_startup = "设置开机自启动"
    tray_exit = "退出"

    # Modes
    mode_balanced = "均衡模式"
    mode_gmode = "G-Mode"
    mode_custom = "自定义"
    mode_changed_title = "模式已切换"
    mode_balanced_msg = "已启用均衡模式。\n请在 Lumine 应用中查看更多信息。"
    mode_gmode_msg = "已启用 G-Mode。\n请在 Lumine 应用中查看更多信息。"

    # UI texts
    rpm = '转/分'
    failsafe_label = "屏蔽保护"
    fan_speed = "风扇速度"

    example_config = """# Lumine 配置文件
# 在托盘中重新加载配置即可生效。

# 请勿修改此值。
# Lumine 应用版本号。
lumine_version: v1.4

# 硬件信息更新间隔
# 单位：毫秒
update_interval: 1000

# 系统恢复正常后，G-Mode 自动关闭的延迟时间
# 单位：秒
disable_protect_after: 30

# UI 颜色配置
colors:
  temp: '#98C379' # 温度文本颜色
  fan: '#61AFEF' # 风扇速度颜色
  normal: '#98C379' # 正常状态颜色
  warning: '#E5C07B' # 警告状态颜色
  overheat: '#E06C75' # 过热状态颜色

# UI 字体
font: Segoe UI

# 温度阈值（°C）
# 达到或超过该温度时进入 G 模式
temp_overheat:
  - 95  # CPU 过热阈值（°C）
  - 85  # GPU 过热阈值（°C）

# 警告阈值 [CPU, GPU]
# 达到或超过该温度时进入警告状态
temp_warning:
  - 85  # CPU 警告阈值（°C）
  - 72  # GPU 警告阈值（°C）

# 热键系统
# - 基于系统虚拟键码（keyboard 库：https://github.com/boppreh/keyboard）
# - 支持组合键
# - 支持硬件特殊按键

g_mode_hotkey: f17
balanced_hotkey: f20
"""