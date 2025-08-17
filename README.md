# Fragment API — Бесплатное API для покупки звёзд и Premium

## 🇷🇺 Русская версия

### Описание
Это бесплатное API для покупки звёзд и Premium на Fragment. Проект позволяет напрямую взаимодействовать с API Fragment без сторонних сервисов.

### ⚙️ Подготовка и настройка

1. **Получение FRAGMENT_HASH**
   - Откройте fragment.com/stars/buy в браузере
   - Нажмите F12 → вкладка Network
   - Кликните на поле выбора количества звёзд
   - В запросе найдите api?hash=... и скопируйте значение после =
   - Вставьте в `config.py` в переменную `FRAGMENT_HASH`

2. **Получение cookie-данных**
   - Привяжите кошелёк v4r2 к Fragment
   - Получите значения:
     - stel_token
     - stel_ssid
     - stel_ton_token
   - Вставьте в `config.py` в `FRAGMENT_COOKIES`

3. **Получение API-ключа от TONAPI.io**
   - Зарегистрируйтесь на TONAPI.io
   - Перейдите в TON API → API KEYS
   - Скопируйте ключ в `config.py` в `TONAPI_KEY`

4. **Добавление мнемонической фразы**
   - Вставьте 24 слова от вашего v4r2-кошелька в `config.py` в `MNEMONIC`

### 🚀 Запуск

```bash
# Установка зависимостей
pip install fastapi uvicorn aiohttp tonutils tonsdk

# Запуск сервера
python -m uvicorn api:app --host 0.0.0.0 --port 8080
```

### 🛰️ Пример запроса

```bash
curl -X POST http://localhost:8080/api/buyStars \
  -H "Content-Type: application/json" \
  -d '{
    "username": "имя_пользователя",
    "quantity": 50,
    "hide_sender": 0
  }'
```

### 📝 Параметры запроса

- `username`: имя пользователя (без @)
- `quantity`: количество звёзд (минимум 50)
- `hide_sender`: 0 (показать отправителя) или 1 (скрыть отправителя)

## 🇬🇧 English Version

### Description
This is a free API for buying Stars and Premium on Fragment. The project allows direct interaction with the Fragment API without third-party services.

### ⚙️ Preparation and Setup

1. **Obtaining FRAGMENT_HASH**
   - Open fragment.com/stars/buy in your browser
   - Press F12 → Network tab
   - Click on the star quantity selector
   - Find api?hash=... in the request and copy the value after =
   - Paste into `config.py` in the `FRAGMENT_HASH` variable

2. **Getting Cookie Data**
   - Link your v4r2 wallet to Fragment
   - Get the values:
     - stel_token
     - stel_ssid
     - stel_ton_token
   - Paste into `config.py` in `FRAGMENT_COOKIES`

3. **Getting an API Key from TONAPI.io**
   - Sign up at TONAPI.io
   - Go to TON API → API KEYS
   - Copy the key into `config.py` in `TONAPI_KEY`

4. **Adding the Mnemonic Phrase**
   - Insert 24 words from your v4r2 wallet into `config.py` in `MNEMONIC`

### 🚀 Running

```bash
# Install dependencies
pip install fastapi uvicorn aiohttp tonutils tonsdk

# Start server
python -m uvicorn api:app --host 0.0.0.0 --port 8080
```

### 🛰️ Example Request

```bash
curl -X POST http://localhost:8080/api/buyStars \
  -H "Content-Type: application/json" \
  -d '{
    "username": "username",
    "quantity": 50,
    "hide_sender": 0
  }'
```

### 📝 Request Parameters

- `username`: username (without @)
- `quantity`: number of stars (minimum 50)
- `hide_sender`: 0 (show sender) or 1 (hide sender)

## 💎 Support
Join our chat: https://t.me/fragmentapioff

## 😄 Donate
If you find this project useful, you can support it with TON:
`UQCSQsHC3A3yz_gHAhYmDug6JJZStmp4rhshV6C6VLf8k9Hf` 