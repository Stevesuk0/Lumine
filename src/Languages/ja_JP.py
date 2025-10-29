from enum import Enum

class Text(Enum):
    language_name = '日本語 (日本)'
    translate_by = 'Stevesuk0 <stevesukawa@outlook.com>'

    # 基本情報
    app_name = "Lumine"
    about_detail = "Lumine は、Dell / Alienware システム向けのオープンソース温度制御アプリです。"
    
    # ようこそ
    welcome_title = "Lumine {version} へようこそ！"
    welcome_desc = "おめでとう、ついに AWCC から解放されたね。"

    # 設定
    config_reloaded_title = "設定ファイルを再読み込みしました"
    config_reloaded_msg = "設定ファイルを正常に再読み込みしました。\n詳細は Lumine アプリで確認できます。"
    
    # アップデート確認
    update_new_title = "新しいバージョンが見つかりました！"
    update_new_msg = "Lumine の新しいバージョン（{latest}）が利用可能です。\nこの通知をクリックするとダウンロードページを開きます。"
    update_latest_title = "最新バージョンです"
    update_latest_msg = "現在の Lumine は最新バージョンです（{version}）。"
    
    # アバウトウィンドウ
    about_title = "Lumine について"
    about_message = "Lumine {version}　作者：{author}"
    
    # トレイメニュー
    tray_show_window = "ウィンドウを表示"
    tray_reload_config = "設定を再読み込み"
    tray_toggle_theme = "テーマを切り替え"
    tray_check_updates = "アップデートを確認..."
    tray_exit = "終了"

    # モード
    mode_balanced = "バランスモード"
    mode_gmode = "G-Mode"
    mode_custom = "カスタムモード"
    mode_changed_title = "モードを切り替えました"
    mode_balanced_msg = "バランスモードに切り替えました。\n詳細は Lumine アプリで確認できます。"
    mode_gmode_msg = "G-Mode に切り替えました。\n詳細は Lumine アプリで確認できます。"

    # オーバーヒート保護
    overheat_title = "システム過熱警告！"
    overheat_msg = "システムの温度が高すぎます。\nLumine アプリで詳細を確認してください。"

    # UIテキスト
    rpm = "RPM（回転/分）"
    failsafe_label = "過熱保護を無効化"
    fan_speed = "ファン速度"