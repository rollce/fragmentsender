from typing import List

# ⚙️ Настройки Fragment
# Получите FRAGMENT_HASH:
# 1. Откройте fragment.com/stars/buy в браузере
# 2. Нажмите F12 → вкладка Network
# 3. Кликните на поле выбора количества звёзд
# 4. В запросе найдите api?hash=... и скопируйте значение после =
FRAGMENT_HASH = "bebc7fb1d4f09bbfe9"

# 🔑 Настройки TON API
# Получите ключ на TONAPI.io:
# 1. Зарегистрируйтесь на TONAPI.io
# 2. Перейдите в TON API → API KEYS
# 3. Скопируйте ключ
TONAPI_KEY = "AE4XI56233Q4TBQAAAAKSIJQLOHOMDZ5OGMEOLTG3NQ7AV4WNFASD2ZJQHRXFNIQBLEEEYQ"
# 💳 Мнемоническая фраза кошелька v4r2
# Ваша тестовая фраза
MNEMONIC: List[str] = [
    "more", "virus", "cube", "flight", "city", "raven", "venture", "other", 
    "amount", "fever", "verify", "build", "mix", "property", "wall", "fame",
    "milk", "defense", "cattle", "nice", "still", "wealth", "ski", "chest"
]

# 🍪 Настройки cookies для Fragment
# Обновленные cookies из строки
FRAGMENT_COOKIES = {
    "stel_ssid": "511f69fa04393c4d23_8574632093477634836",
    "stel_dt": "-180", 
    "stel_token": "9df47d1b71d31d84f5b37377f5e3a25a9df47d009df47921283aeb474b9e127e9b66f",
    "stel_ton_token": "ZvFUrDuxD78CIvsdFYOMvYQVQoYgE8gEC9XOn1M-XbWI_lPlZ6z7upMaZZ4G0wO5QpyobOiqsRwXFbNkUgQyPog3CHClIHME7e0kS33X9HMjOhuQ4Ykqc_bNY-kYUHnEY4FQHRFEjz5YPdS8eM2p8JIta0uCipH_90nS3wR1bWGTQkBVdUflYevdMxB7oTQ9j_-49hkA"
}

# 🌐 Заголовки для запросов
# Можно заменить User-Agent на свой из браузера:
# Инструменты разработчика → Network → Headers
FRAGMENT_HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
} 