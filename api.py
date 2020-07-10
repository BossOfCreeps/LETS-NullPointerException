from __future__ import unicode_literals
import json
from flask import Flask, request
from db import select_events
from datetime import datetime
import locale
import pymorphy2

locale.setlocale(locale.LC_ALL, ('RU', "UTF-8"))
app = Flask(__name__)
sessionStorage = {}


@app.route("/", methods=['POST'])
def main():
    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)
    return json.dumps(response, ensure_ascii=False, indent=2)


# Функция для непосредственной обработки диалога.
def handle_dialog(req, res):
    user_id = req['session']['user_id']
    user_say = req['request']['original_utterance'].lower()



    # else
    res['response']['text'] = "Простите. Я вас не поняла."

    if req['session']['new']:
        sessionStorage[user_id] = {
            'id': 0
        }
        res['response']['text'] = "Привет. Скажи 'список мероприятий' и мы начнём"

    if user_say.find('мероприяти') >= 0 or user_say.find('событи') >= 0:
        print(1)
        sessionStorage[user_id]['id'] = 1
        res['response']['text'] = event_list(sessionStorage[user_id]['id'])

    if (user_say.find('далее') >= 0 or user_say.find('дальше') >= 0 or user_say.find("следущ") >= 0 or
            user_say.find('вперёд') >= 0) and sessionStorage[user_id]['id'] > 0:
        print(2)
        sessionStorage[user_id]['id'] += 1
        res['response']['text'] = event_list(sessionStorage[user_id]['id'])

    if (user_say.find('назад') >= 0 or user_say.find('прошл') >= 0 or user_say.find("предыдущ") >= 0) and \
            sessionStorage[user_id]['id'] > 1:
        print(3)
        sessionStorage[user_id]['id'] -= 1
        res['response']['text'] = event_list(sessionStorage[user_id]['id'])

    if user_say.find('повтори') >= 0 and sessionStorage[user_id]['id'] > 0:
        print(4)
        res['response']['text'] = event_list(sessionStorage[user_id]['id'])

    if res['response']['text'] == "Больше мероприятий нет":
        print(5)
        sessionStorage[user_id]['id'] = 0

    if (user_say.find('подробнее') >= 0 or user_say.find('точнее') >= 0) and sessionStorage[user_id]['id'] > 0:
        print(6)
        res['response']['text'] = event_podrobno(sessionStorage[user_id]['id'])

    try:
        print(user_say, sessionStorage[user_id]['id'])
    except:
        pass

def event_list(event_id):
    try:
        row = select_events(event_id)[0]
        morph = pymorphy2.MorphAnalyzer()
        DT = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
        day = str(int(DT.strftime("%d")))
        month = morph.parse(DT.strftime("%B"))[0].inflect({'gent'}).word
        hour = str(int(DT.strftime("%H")))
        min = str(int(DT.strftime("%M")))
        return row[0] + ". " + DT.strftime("{}го {} %Yго года. В {} часов {} минут.").format(day, month, hour, min)
    except:
        return "Больше мероприятий нет"


def event_podrobno(event_id):
    try:
        return select_events(event_id)[0][2]
    except:
        return "Ошибка"


# app.run(ssl_context='adhoc', host="0.0.0.0", port=5000)
app.run(host="0.0.0.0", port=5000)
