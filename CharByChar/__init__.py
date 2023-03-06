from time import sleep # This will alow the script to utilise the 'delay' variable

def cs(): # CS stands for ClearScreen
  print("\033c")

class CharByChar:
    def __init__(self, text="Printing char by char!", delay=0.08333333333): # For best results, use the default delay
        self.letters = []
        self.delay = delay
        for chacter in text:
            self.letters.append(character)
        character = None # Clear cached data
        self.line_print()
   
    def line_print(self):
        to_print = "" # To print is essintially the 'text' variable but each character is added after each delay
        for character in self.letters:
            sleep(self.delay) # Delay
            cs()
            to_print += character # Character is added after each delay
           
            print(to_print)
