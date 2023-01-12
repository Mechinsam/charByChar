from time import sleep

def cs():
  print("\033c")

class CharByChar:
    def __init__(self, text="Printing char by char!", delay=0.08333333333):
        self.letters = []
        self.delay = delay
        for x in text:
            self.letters.append(x)
        self.line_print()
   
    def line_print(self):
        to_print = ""
        for x in self.letters:
            sleep(self.delay)
            cs()
            to_print += x
           
            print(to_print)
