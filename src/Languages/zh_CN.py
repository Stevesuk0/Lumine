from enum import Enum

class Text(Enum):
    language_name = '中文，简体 (中国)'
    translate_by = 'Stevesuk0 <stevesukawa@outlook.com>'

    # 基础信息
    app_name = "Lumine"
    about_detail = "Lumine 是一个开源的 Dell / Alienware 系统温控管理程序。"
    
    # 欢迎
    welcome_title = "欢迎使用 Lumine {version}！"
    welcome_desc = "恭喜，终于摆脱 AWCC 了。"

    # 配置
    config_reloaded_title = "配置文件已重新加载"
    config_reloaded_msg = "配置文件已成功重新加载。\n可在 Lumine 应用中查看更多信息。"
    
    # 更新检查
    update_new_title = "检测到新版本！"
    update_new_msg = "Lumine 有新版本可用（{latest}）。\n点击此通知以查看下载链接。"
    update_latest_title = "已是最新版本"
    update_latest_msg = "当前 Lumine 已是最新版本（{version}）。"
    
    # 关于窗口
    about_title = "关于 Lumine"
    about_message = "Lumine {version}，作者：{author}"
    
    # 托盘菜单
    tray_show_window = "显示窗口"
    tray_reload_config = "重新加载配置"
    tray_toggle_theme = "切换主题"
    tray_check_updates = "检查更新..."
    tray_exit = "退出程序"

    # 模式
    mode_balanced = "平衡模式"
    mode_gmode = "G-Mode"
    mode_custom = "自定义模式"
    mode_changed_title = "模式已切换"
    mode_balanced_msg = "已切换至平衡模式。\n可在 Lumine 应用中查看更多信息。"
    mode_gmode_msg = "已切换至 G-Mode。\n可在 Lumine 应用中查看更多信息。"

    # 过热保护
    overheat_title = "系统过热警告！"
    overheat_msg = "检测到系统温度过高。\n请打开 Lumine 查看详情。"

    # 界面文本
    rpm = "转/分"
    failsafe_label = "关闭过热保护"
    fan_speed = "风扇速度"