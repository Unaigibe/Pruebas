import json

import requests
from reportlab.pdfgen import canvas

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

print(diccionarioFinal)
print(diccionarioFinal['pregunta'])
opciones = ""
for respuestas in diccionarioFinal['respuestas']:
    opciones += respuestas
print(opciones)
print(diccionarioFinal['correcta'])


doc = canvas.Canvas("Quiz.pdf")

#Escribimos una cadena de Texto dentro del documento
doc.drawString(100, 750, diccionarioFinal['pregunta'])
doc.drawString(300, 850, opciones)
doc.drawString(600, 950, diccionarioFinal['correcta'])

doc.save()