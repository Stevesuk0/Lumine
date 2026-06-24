from enum import Enum

class Text(Enum):
    language_name = 'Русский'
    translate_by = 'Claude <noreply@anthropic.com>'

    # Basic
    app_name = "Lumine"
    about_detail = "Lumine — это контроллер управления температурой с открытым исходным кодом для систем Dell и Alienware."
    already_started = "Другой экземпляр Lumine уже запущен."
    already_started_detailed = "Используйте существующий экземпляр или закройте его перед запуском нового."

    # Welcome
    welcome_title = "Добро пожаловать в Lumine {version}!"

    # Configuration
    config_reloaded_title = "Конфигурация перезагружена"
    config_reloaded_msg = "Конфигурация перезагружена.\nПодробнее в приложении Lumine."

    # Update check
    update_new_title = "Обнаружена новая версия!"
    update_new_msg = "Доступна новая версия Lumine ({latest}).\nНажмите на это уведомление, чтобы перейти к ссылке для загрузки."
    update_latest_title = "У вас актуальная версия"
    update_latest_msg = "Lumine уже обновлён до последней версии. ({version})"

    # About window
    about_title = "О программе Lumine"
    about_message = "Lumine {version} от {author}"

    # Tray menu
    tray_view_source = "Просмотреть исходный код..."
    tray_show_window = "Показать окно"
    tray_reload_config = "Перезагрузить конфигурацию"
    tray_edit_config = "Изменить конфигурацию..."
    tray_toggle_theme = "Переключить тему"
    tray_check_updates = "Проверить обновления..."
    tray_start_on_startup = "Запускать при старте системы"
    tray_exit = "Выход"

    # Modes
    mode_balanced = "Сбалансированный"
    mode_gmode = "G-Mode"
    mode_custom = "Пользовательский"
    mode_changed_title = "Режим изменён"
    mode_balanced_msg = "Активирован сбалансированный режим.\nПодробнее в приложении Lumine."
    mode_gmode_msg = "Активирован G-Mode.\nПодробнее в приложении Lumine."

    # UI texts
    rpm = 'об/мин'
    failsafe_label = "Тепловой обход"
    fan_speed = "Скорость вентилятора"

    example_config = """# Конфигурация Lumine
# Перезагрузите конфигурацию через трей для применения изменений.

# НЕ изменяйте это значение.
# Версия приложения Lumine.
lumine_version: v1.4

# Интервал обновления данных оборудования.
# Единица: миллисекунды.
update_interval: 1000

# Время (в секундах), по истечении которого G-Mode автоматически отключается
# после нормализации температуры системы.
# Единица: секунды.
disable_protect_after: 30

# Цветовые настройки интерфейса
colors:
  temp: '#98C379' # Цвет текста температуры
  fan: '#61AFEF' # Цвет скорости вентилятора
  normal: '#98C379' # Цвет нормального состояния
  warning: '#E5C07B' # Цвет состояния предупреждения
  overheat: '#E06C75' # Цвет состояния перегрева

# Шрифт интерфейса
font: Segoe UI

# Пороговые значения температуры (°C)
# При достижении или превышении этих значений система переходит в G-Mode.
temp_overheat:
  - 95  # Порог перегрева CPU (°C)
  - 85  # Порог перегрева GPU (°C)

# Порог предупреждения [CPU, GPU]
# При достижении или превышении этих значений система переходит в состояние ПРЕДУПРЕЖДЕНИЯ.
temp_warning:
  - 85  # Порог предупреждения CPU (°C)
  - 72  # Порог предупреждения GPU (°C)

# Горячие клавиши
# - Основаны на виртуальных кодах клавиш (библиотека keyboard: https://github.com/boppreh/keyboard)
# - Поддержка многоклавишных комбинаций
# - Допускаются аппаратные клавиши.

g_mode_hotkey: f17
balanced_hotkey: f20
"""
