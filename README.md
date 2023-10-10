Это **REST API** контракт для получения **актуального курса валют**.

**Для использования необходимо:**
1. **Установить все зависимости** из файла "**requirements.txt**" (```python pip install -r requirements.txt```);
2. Получить **App API IDs** на сайте https://openexchangerates.org/signup/free и **вставить его в переменную** "**app_api_ids**";
3. **Запустить файл** "**main.py**" (`python main.py`)

**Пример запроса:** ```localhost:5000/api/rates?from=USD&to=RUB```
