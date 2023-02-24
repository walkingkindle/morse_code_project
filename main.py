from engine import Engine
from playsound import playsound


eng = Engine()
#character equals that same character but in morse code.
#character
if eng.text:
    eng.text_to_morse()
    real_morse = eng.morse_code_text.replace(',',' ')
    print(real_morse)

