
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
        self.first_question = input("Type '1': I want to convert text into morse code.\n"
                                    "Type '2': I want to convert morse code into text.")
        if self.first_question == "1":
            self.text = input("Tell me what you want to translate. ")
        else:
            self.text_m = input("Type your morse code here. ")
        self.morse_code_text_list = []
        self.morse_code_text = ""
        self.new_text = ""
        self.complete = ""



    def text_to_morse(self):
        """Converts text to morse code."""
        for word in self.text:
            for char in word:
                if char.upper() in self.morse_code:
                    new_char = self.morse_code[char.upper()]
                    self.morse_code_text += new_char + ","
        return self.morse_code_text[:-1]

    def morse_to_text(self):
        """Converts morse code to text."""
        ready_text = self.text_m.split(' ')
        for character in ready_text:
            new_character = self.morse_code_reversed[character]
            self.complete += new_character
        return print(self.complete.strip())
