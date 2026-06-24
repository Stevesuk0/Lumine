from enum import Enum

class Text(Enum):
    language_name = '日本語'
    translate_by = 'Claude <noreply@anthropic.com>'

    # Basic
    app_name = "Lumine"
    about_detail = "Lumine は、Dell および Alienware システム向けのオープンソース サーマル コントローラーです。"
    already_started = "Lumine の別のインスタンスがすでに実行中です。"
    already_started_detailed = "既存のインスタンスを使用するか、新しいインスタンスを起動する前に閉じてください。"

    # Welcome
    welcome_title = "Lumine {version} へようこそ！"

    # Configuration
    config_reloaded_title = "設定を再読み込みしました"
    config_reloaded_msg = "設定を再読み込みしました。\nLumine アプリで詳細を確認してください。"

    # Update check
    update_new_title = "新しいバージョンが見つかりました！"
    update_new_msg = "Lumine の新しいバージョン（{latest}）が利用可能です。\nこの通知をクリックしてダウンロードリンクを確認してください。"
    update_latest_title = "最新バージョンです"
    update_latest_msg = "Lumine はすでに最新バージョンです。（{version}）"

    # About window
    about_title = "Lumine について"
    about_message = "Lumine {version}（作者：{author}）"

    # Tray menu
    tray_view_source = "ソースコードを表示..."
    tray_show_window = "ウィンドウを表示"
    tray_reload_config = "設定を再読み込み"
    tray_edit_config = "設定を編集..."
    tray_toggle_theme = "テーマを切り替え"
    tray_check_updates = "アップデートを確認..."
    tray_start_on_startup = "スタートアップに登録"
    tray_exit = "終了"

    # Modes
    mode_balanced = "バランスモード"
    mode_gmode = "G-Mode"
    mode_custom = "カスタム"
    mode_changed_title = "モードが切り替わりました"
    mode_balanced_msg = "バランスモードが有効になりました。\nLumine アプリで詳細を確認してください。"
    mode_gmode_msg = "G-Mode が有効になりました。\nLumine アプリで詳細を確認してください。"

    # UI texts
    rpm = 'RPM'
    failsafe_label = "サーマル バイパス"
    fan_speed = "ファン速度"

    example_config = """# Lumine 設定ファイル
# トレイから設定を再読み込みすると変更が反映されます。

# この値は変更しないでください。
# Lumine のアプリケーション バージョンです。
lumine_version: v1.4

# ハードウェア情報の更新間隔
# 単位：ミリ秒
update_interval: 1000

# システムが正常温度に戻った後、G-Mode が自動的に無効になるまでの時間
# 単位：秒
disable_protect_after: 30

# UI カラー設定
colors:
  temp: '#98C379' # 温度テキストの色
  fan: '#61AFEF' # ファン速度の色
  normal: '#98C379' # 正常状態の色
  warning: '#E5C07B' # 警告状態の色
  overheat: '#E06C75' # 過熱状態の色

# UI フォント
font: Segoe UI

# 温度しきい値（°C）
# この値以上になると G-Mode に切り替わります
temp_overheat:
  - 95  # CPU 過熱しきい値（°C）
  - 85  # GPU 過熱しきい値（°C）

# 警告しきい値 [CPU, GPU]
# この値以上になると警告状態になります
temp_warning:
  - 85  # CPU 警告しきい値（°C）
  - 72  # GPU 警告しきい値（°C）

# ホットキー設定
# - システム仮想キーコードに基づく（keyboard ライブラリ：https://github.com/boppreh/keyboard）
# - 複数キーの組み合わせに対応
# - ハードウェア固有のキーも使用可能

g_mode_hotkey: f17
balanced_hotkey: f20
"""
