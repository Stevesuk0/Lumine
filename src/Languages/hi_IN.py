from enum import Enum

class Text(Enum):
    language_name = 'हिन्दी'
    translate_by = 'Claude <noreply@anthropic.com>'

    # Basic
    app_name = "Lumine"
    about_detail = "Lumine, Dell और Alienware सिस्टम के लिए एक ओपन-सोर्स थर्मल कंट्रोलर है।"
    already_started = "Lumine का एक अन्य इंस्टेंस पहले से चल रहा है।"
    already_started_detailed = "कृपया मौजूदा इंस्टेंस का उपयोग करें या नया शुरू करने से पहले उसे बंद करें।"

    # Welcome
    welcome_title = "Lumine {version} में आपका स्वागत है!"

    # Configuration
    config_reloaded_title = "कॉन्फ़िगरेशन पुनः लोड हो गया"
    config_reloaded_msg = "कॉन्फ़िगरेशन पुनः लोड हो गया है।\nअधिक जानकारी के लिए Lumine ऐप देखें।"

    # Update check
    update_new_title = "नया संस्करण मिला!"
    update_new_msg = "Lumine का नया संस्करण ({latest}) उपलब्ध है।\nडाउनलोड लिंक देखने के लिए इस सूचना पर क्लिक करें।"
    update_latest_title = "आप अप टु डेट हैं!"
    update_latest_msg = "Lumine पहले से नवीनतम संस्करण पर है। ({version})"

    # About window
    about_title = "Lumine के बारे में"
    about_message = "Lumine {version}, {author} द्वारा"

    # Tray menu
    tray_show_window = "विंडो दिखाएं"
    tray_reload_config = "कॉन्फ़िगरेशन पुनः लोड करें"
    tray_edit_config = "कॉन्फ़िगरेशन संपादित करें..."
    tray_toggle_theme = "थीम बदलें"
    tray_check_updates = "अपडेट जांचें..."
    tray_start_on_startup = "स्टार्टअप पर चलाएं"
    tray_exit = "बाहर निकलें"

    # Modes
    mode_balanced = "बैलेंस्ड"
    mode_gmode = "G-Mode"
    mode_custom = "कस्टम"
    mode_changed_title = "मोड बदला गया"
    mode_balanced_msg = "बैलेंस्ड मोड सक्रिय हो गया।\nअधिक जानकारी के लिए Lumine ऐप देखें।"
    mode_gmode_msg = "G-Mode सक्रिय हो गया।\nअधिक जानकारी के लिए Lumine ऐप देखें।"

    # UI texts
    rpm = 'RPM'
    failsafe_label = "थर्मल बाईपास"
    fan_speed = "पंखे की गति"

    example_config = """# Lumine कॉन्फ़िगरेशन
# परिवर्तन लागू करने के लिए ट्रे से कॉन्फ़िगरेशन पुनः लोड करें।

# इस मान को संशोधित न करें।
# यह Lumine का एप्लिकेशन संस्करण है।
lumine_version: v1.4

# हार्डवेयर जानकारी अपडेट अंतराल।
# इकाई: मिलीसेकंड।
update_interval: 1000

# सिस्टम के सामान्य होने के बाद G-Mode स्वतः बंद होने का समय
# इकाई: सेकंड।
disable_protect_after: 30

# UI रंग सेटिंग
colors:
  temp: '#98C379' # तापमान टेक्स्ट रंग
  fan: '#61AFEF' # पंखे की गति रंग
  normal: '#98C379' # सामान्य स्थिति रंग
  warning: '#E5C07B' # चेतावनी स्थिति रंग
  overheat: '#E06C75' # अत्यधिक गर्मी स्थिति रंग

# UI फ़ॉन्ट
font: Segoe UI

# तापमान सीमा (°C)
# इस मान तक पहुंचने पर सिस्टम G-Mode में प्रवेश करता है।
temp_overheat:
  - 95  # CPU अत्यधिक गर्मी सीमा (°C)
  - 85  # GPU अत्यधिक गर्मी सीमा (°C)

# चेतावनी सीमा [CPU, GPU]
# इस मान तक पहुंचने पर सिस्टम चेतावनी स्थिति में प्रवेश करता है।
temp_warning:
  - 85  # CPU चेतावनी सीमा (°C)
  - 72  # GPU चेतावनी सीमा (°C)

# हॉटकी सेटिंग
# - सिस्टम वर्चुअल की कोड पर आधारित (keyboard लाइब्रेरी: https://github.com/boppreh/keyboard)
# - मल्टी-की कॉम्बिनेशन समर्थित
# - हार्डवेयर-विशिष्ट कुंजियां भी उपयोग की जा सकती हैं।

g_mode_hotkey: f17
balanced_hotkey: f20
"""
