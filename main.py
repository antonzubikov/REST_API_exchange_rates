from flask import Flask, request, jsonify
import requests


app = Flask(__name__)


@app.route('/api/rates', methods=['GET'])
def exchange_rates():
    """
    Endpoint для получения актуального курса валюты.

    Аргументы:
        — "from": изначальная валюта;
        — "to": конечная валюта

    Пример запроса: 'localhost:5000/api/rates?from=USD&to=RUB'
    """
    currency_from = request.args.get('from')
    currency_to = request.args.get('to')

    # Необходимо вставить свой App API IDs (или оставить этот, если он всё ещё будет работать)
    # Пользовался API сайта https://openexchangerates.org/signup/free
    app_api_ids = 'c57be4d743d64e8ca4ad367d1363c526'

    data = requests.get(
        f'https://openexchangerates.org/api/latest.json'
        f'?app_id={app_api_ids}'
        f'&base={currency_from}'
        f'&symbols={currency_to}').json()

    # "jsonify()" (Flask) позволяет сериализовать словарь Python в JSON
    # Также с помощью "round()" происходит округление значения до 2 знаков после точки
    if data['rates']:  # проверяю, есть ли значения в полученном ответе. Если есть — возвращаю JSON и статус ответа 200
        return jsonify({'result': round(data['rates']['RUB'], 2)}), 200
    else:  # если значений в словаре нет — возвращаю сообщение об ошибке и статус ответа 404 (ошибка на стороне клиента)
        return 'Ошибка в наименовании одной из валют. Попробуйте ещё раз.', 404


if __name__ == '__main__':
    app.run(debug=True)
