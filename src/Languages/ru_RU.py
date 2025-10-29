from enum import Enum

class Text(Enum):
    language_name = 'Русский (Россия)'
    translate_by = 'Stevesuk0 <stevesukawa@outlook.com>'

    app_name = "Lumine"
    about_detail = "Lumine — это программа с открытым исходным кодом для управления температурой систем Dell / Alienware."

    welcome_title = "Добро пожаловать в Lumine {version}!"
    welcome_desc = "Поздравляем, наконец-то без AWCC."

    config_reloaded_title = "Конфигурация перезагружена"
    config_reloaded_msg = "Файл конфигурации успешно перезагружен.\nПодробнее см. в приложении Lumine."

    update_new_title = "Обнаружена новая версия!"
    update_new_msg = "Доступна новая версия Lumine ({latest}).\nНажмите уведомление, чтобы открыть страницу загрузки."
    update_latest_title = "У вас последняя версия"
    update_latest_msg = "Текущая версия Lumine — самая новая ({version})."

    about_title = "О программе Lumine"
    about_message = "Lumine {version}, автор: {author}"

    tray_show_window = "Показать окно"
    tray_reload_config = "Перезагрузить конфигурацию"
    tray_toggle_theme = "Сменить тему"
    tray_check_updates = "Проверить обновления..."
    tray_exit = "Выход"

    mode_balanced = "Сбалансированный режим"
    mode_gmode = "G-Mode"
    mode_custom = "Пользовательский режим"
    mode_changed_title = "Режим изменён"
    mode_balanced_msg = "Активирован сбалансированный режим.\nПодробнее см. в приложении Lumine."
    mode_gmode_msg = "Активирован G-Mode.\nПодробнее см. в приложении Lumine."

    overheat_title = "Перегрев системы!"
    overheat_msg = "Обнаружено превышение температуры.\nОткройте Lumine для подробностей."

    rpm = "об/мин"
    failsafe_label = "Отключить защиту от перегрева"
    fan_speed = "Скорость вентилятора"
