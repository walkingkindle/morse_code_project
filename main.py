from engine import Engine
from playsound import playsound
from gtts import gTTS
import os

language = 'en'
eng = Engine()
#character equals that same character but in morse code.
#character
if eng.first_question == '1':
    if eng.text:
        eng.text_to_morse()
        real_morse = eng.morse_code_text.replace(',',' ')
        print(real_morse)
        for char in real_morse:
            if char == '.':
                playsound(r"C:\Users\Aleksa Hadzic\PycharmProjects\morse_code_project\sounds\dot.mp3")
            elif char == '-':
                playsound(r"C:\Users\Aleksa Hadzic\PycharmProjects\morse_code_project\sounds\dash.mp3")
elif eng.first_question == '2':
    eng.morse_to_text()
