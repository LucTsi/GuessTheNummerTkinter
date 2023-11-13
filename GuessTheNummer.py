#imports
import tkinter as tk
import random
import os

def shutdown():
    #stänger av datorn
    return os.system("shutdown /s /t 100")
#filen som är för hur många gånger du har förlorat
def increment_file_value(filename="los.txt"):
    try:
        #läser txt filen
        with open(filename, 'r') as file:
            value = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        # om filen inte finns så får den value 0
        value = 0

    # plus 1 value
    value += 1

    # lägg till värdet i filen
    with open(filename, 'w') as file:
        file.write(str(value))
    #printa värdet
    print(f"How many times you have lost: {value}")


#sjölva spelet
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        self.target_number = random.randint(1, 5)
        print(self.target_number)
        # Entry widget för input
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=20)

        # knappen som submitar dit svar
        self.button = tk.Button(self.root, text="Submit", command=self.check_input)
        self.button.pack(pady=20)

        # label som vissar text messages
        self.label = tk.Label(self.root, text="")
        self.label.pack(pady=20)
    #själva mechanism som säger om du van eller inte. och hur många gånger du är död
    def check_input(self):
        user_input = self.entry.get()
        if user_input in ["1", "2", "3", "4", "5"]:
            if self.target_number and int(user_input) == self.target_number:
                #det som händer när man vinner
                self.label.config(text="you won")
                #ny random nummer
                self.target_number = random.randint(1, 5)
                #printa nya numret för debug
                print(self.target_number)
            else:
                #det som händer när man förlorar
                self.label.config(text="You Loose!")
                #ny random nummer
                self.target_number = random.randint(1, 5)
                # lägg till 1 i hur många gånger man har förlorat
                increment_file_value()
                #printa nya numret för debug
                print(self.target_number)
        else:
            #du var retarded och skrev inte ett nummer 1- 5
            self.label.config(text="Invalid input. Choose a number 1-5")
#play the gay game
root = tk.Tk()
app = App(root)
root.mainloop()
