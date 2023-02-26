from tkinter import *
from playsound import playsound
class Engine:
    def __init__(self):
        self.morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}
        self.morse_code_reversed ={
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '/': ' '
    }

        PINK = "#e2979c"
        RED = "#e7305b"
        GREEN = "#9bdeac"
        YELLOW = "#f7f5dd"
        FONT_NAME = "Courier"

        self.window = Tk()
        self.window.title("Morse code Converter")
        self.window.config(padx=100, pady=50, bg=YELLOW)
        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.canvas.grid(column=1, row=1)
        self.text_entry = Entry(width=30)
        self.text_entry.grid(column=0, row=2)
        self.start_button = Button(text="Convert", highlightthickness=0, command=self.text_to_morse)
        self.start_button.grid(column=1, row=2)
        self.morse_entry = Entry(width=30)
        self.morse_entry.grid(column=0, row=3)
        self.start_button2 = Button(text="Convert", highlightthickness=0, command=self.morse_to_text)
        self.start_button2.grid(column=1, row=3)
        self.morse_code_text_list = []
        self.morse_code_text = ""
        self.new_text = ""
        self.complete = ""


    def text_to_morse(self):
        """Converts text to morse code."""
        self.text = self.text_entry.get()
        for word in self.text:
            for char in word:
                if char.upper() in self.morse_code:
                    new_char = self.morse_code[char.upper()]
                    self.morse_code_text += new_char + ","

        real_morse = self.morse_code_text.replace(',',' ')
        self.morse_entry.insert(END, f'{real_morse}')
        for char in real_morse:
            if char == '.':
                playsound(r"C:\Users\Aleksa Hadzic\PycharmProjects\morse_code_project\sounds\dot.mp3")
            elif char == '-':
                playsound(r"C:\Users\Aleksa Hadzic\PycharmProjects\morse_code_project\sounds\dash.mp3")
        return self.morse_code_text[:-1]

    def morse_to_text(self):
        """Converts morse code to text."""
        morse_code = self.morse_entry.get()
        morse_words = morse_code.split(" / ")
        decoded_text = ""
        for morse_word in morse_words:
            morse_characters = morse_word.split()
            for character in morse_characters:
                if character:
                    new_character = self.morse_code_reversed[character]
                    decoded_text += new_character
                else:
                    decoded_text += " "
        self.text_entry.delete(END)
        self.text_entry.insert(END, decoded_text)


