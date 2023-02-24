
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
        self.text = input("Tell me what you want to translate. ")
        self.morse_code_text_list = []
        self.morse_code_text = ""

    def text_to_morse(self):
        """Converts Morse code to text."""
        for word in self.text:
            for char in word:
                if char.upper() in self.morse_code:
                    new_char = self.morse_code[char.upper()]
                    self.morse_code_text += new_char + ","
                    print(self.morse_code_text[:-1])
        return self.morse_code_text[:-1]

