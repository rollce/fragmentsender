from typing import List

# ⚙️ Настройки Fragment
# Получите FRAGMENT_HASH:
# 1. Откройте fragment.com/stars/buy в браузере
# 2. Нажмите F12 → вкладка Network
# 3. Кликните на поле выбора количества звёзд
# 4. В запросе найдите api?hash=... и скопируйте значение после =
FRAGMENT_HASH = ""

# 🔑 Настройки TON API
# Получите ключ на TONAPI.io:
# 1. Зарегистрируйтесь на TONAPI.io
# 2. Перейдите в TON API → API KEYS
# 3. Скопируйте ключ
TONAPI_KEY = ""
# 💳 Мнемоническая фраза кошелька v4r2
# Вставьте 24 слова от вашего кошелька
MNEMONIC: List[str] = [
    
]

# 🍪 Настройки cookies для Fragment
# Получите через:
# 1. Cookie Editor (Chrome)
# 2. Инструменты разработчика → Application → Cookies
FRAGMENT_COOKIES = {
    "stel_token": "",
    "stel_ssid": "",
    "stel_ton_token": ""
}

# 🌐 Заголовки для запросов
# Можно заменить User-Agent на свой из браузера:
# Инструменты разработчика → Network → Headers
FRAGMENT_HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
} 