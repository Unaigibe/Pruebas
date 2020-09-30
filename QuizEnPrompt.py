# Programa sencillo que genera preguntas desde una API.
# Mediante respuestas de True y False se obtiene el resultado.

import json
import requests

diccionarioFinal = {'pregunta': '', 'respuestas': [], 'correcta': ''}

def crear_preguntas(archivo_json):
    r = requests.get(archivo_json).text
    diccionario_raw = json.loads(r)

    for elemento in diccionario_raw['results']:
        diccionarioFinal['pregunta'] = elemento['question']
        diccionarioFinal['respuestas'] = elemento['incorrect_answers']
        diccionarioFinal['respuestas'].append(elemento['correct_answer'])
        diccionarioFinal['correcta'] = elemento['correct_answer']
        return diccionarioFinal


archivo_json = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean"
crear_preguntas(archivo_json)
pregunta = diccionarioFinal['pregunta']

print("Responde a la siguiente pregunta")
print(pregunta)
respuesta_usuario = input(str("Escribe True o False")).lower()

if respuesta_usuario in diccionarioFinal['correcta'].lower():
    print("Respuesta CORRECTA")
else:
    print("Respuesta INCORRECTA")
