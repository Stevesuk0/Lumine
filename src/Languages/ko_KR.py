from enum import Enum

class Text(Enum):
    language_name = '한국어'
    translate_by = 'Claude <noreply@anthropic.com>'

    # Basic
    app_name = "Lumine"
    about_detail = "Lumine은 Dell 및 Alienware 시스템을 위한 오픈 소스 열 관리 컨트롤러입니다."
    already_started = "Lumine의 다른 인스턴스가 이미 실행 중입니다."
    already_started_detailed = "기존 인스턴스를 사용하거나 새 인스턴스를 시작하기 전에 닫으세요."

    # Welcome
    welcome_title = "Lumine {version}에 오신 것을 환영합니다!"

    # Configuration
    config_reloaded_title = "설정이 다시 로드되었습니다"
    config_reloaded_msg = "설정이 다시 로드되었습니다.\nLumine 앱에서 자세한 내용을 확인하세요."

    # Update check
    update_new_title = "새 버전이 감지되었습니다!"
    update_new_msg = "새 버전의 Lumine을 사용할 수 있습니다（{latest}）.\n이 팝업을 클릭하여 다운로드 링크를 확인하세요."
    update_latest_title = "최신 버전입니다"
    update_latest_msg = "Lumine은 이미 최신 버전입니다.（{version}）"

    # About window
    about_title = "Lumine 정보"
    about_message = "Lumine {version} 제작: {author}"

    # Tray menu
    tray_view_source = "소스 코드 보기..."
    tray_show_window = "창 표시"
    tray_reload_config = "설정 다시 로드"
    tray_edit_config = "설정 편집..."
    tray_toggle_theme = "테마 전환"
    tray_check_updates = "업데이트 확인..."
    tray_start_on_startup = "시작 프로그램 등록"
    tray_exit = "종료"

    # Modes
    mode_balanced = "균형 모드"
    mode_gmode = "G-Mode"
    mode_custom = "사용자 정의"
    mode_changed_title = "모드가 변경되었습니다"
    mode_balanced_msg = "균형 모드가 활성화되었습니다.\nLumine 앱에서 자세한 내용을 확인하세요."
    mode_gmode_msg = "G-Mode가 활성화되었습니다.\nLumine 앱에서 자세한 내용을 확인하세요."

    # UI texts
    rpm = 'RPM'
    failsafe_label = "열 보호 우회"
    fan_speed = "팬 속도"

    example_config = """# Lumine 설정 파일
# 트레이에서 설정을 다시 로드하면 변경 사항이 적용됩니다.

# 이 값은 수정하지 마세요.
# Lumine 애플리케이션 버전입니다.
lumine_version: v1.4

# 하드웨어 정보 업데이트 간격
# 단위: 밀리초
update_interval: 1000

# 시스템이 정상 온도로 돌아온 후 G-Mode가 자동으로 비활성화되는 시간
# 단위: 초
disable_protect_after: 30

# UI 색상 설정
colors:
  temp: '#98C379' # 온도 텍스트 색상
  fan: '#61AFEF' # 팬 속도 색상
  normal: '#98C379' # 정상 상태 색상
  warning: '#E5C07B' # 경고 상태 색상
  overheat: '#E06C75' # 과열 상태 색상

# UI 폰트
font: Segoe UI

# 온도 임계값（°C）
# 이 값 이상이 되면 G-Mode로 전환됩니다
temp_overheat:
  - 95  # CPU 과열 임계값（°C）
  - 85  # GPU 과열 임계값（°C）

# 경고 임계값 [CPU, GPU]
# 이 값 이상이 되면 경고 상태가 됩니다
temp_warning:
  - 85  # CPU 경고 임계값（°C）
  - 72  # GPU 경고 임계값（°C）

# 단축키 설정
# - 시스템 가상 키 코드 기반（keyboard 라이브러리: https://github.com/boppreh/keyboard）
# - 조합 키 지원
# - 하드웨어 전용 키 사용 가능

g_mode_hotkey: f17
balanced_hotkey: f20
"""
