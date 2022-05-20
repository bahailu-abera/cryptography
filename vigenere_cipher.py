import tkinter as tk
from functools import partial
import tkinter.font as tkFont


class Input:

    ''' receive and display user input using tkinter text box widget '''

    def __init__(self):
        # Top level window
        self.wn = tk.Tk()
        self.wn.title("TextBox Input")
        self.wn.geometry('1200x600')
        self.wn.config(bg='#040720')
        self.key = str()

        myFont = tkFont.Font(family="Times New Roman", size=20, weight="bold")

        # TextBox for plain text
        label = tk.Label(self.wn, text = "Enter the text here: ", background= '#040720', fg='#FFF')
        label.place(x= 730, y = 0)
        self.plaintxt = tk.Text(self.wn, height = 8, width = 60, font=myFont)
        self.plaintxt.place(x = 730, y = 20)

        # Textbox for the key
        # TextBox for plain text
        key_label = tk.Label(self.wn, text = "Enter the key here: ", background= '#040720', fg='#FFF')
        key_label.place(x= 730, y = 200)
        self.key_txt = tk.Text(self.wn, height = 8, width = 60, font=myFont)
        self.key_txt.place(x = 730, y = 220)

        # Button Creation
        self.encButton = tk.Button(self.wn, text = "Encrypt", command = partial(self.printInput, "-e"), pady=8)
        self.encButton.place(x=850, y=400)
        self.decButton = tk.Button(self.wn, text = "Decrypt", command = partial(self.printInput, "-d"), pady=8,)
        self.decButton.place(x=960, y=400)

        # track the space index
        self.space_index = []

        # Label the input text
        self.lbl = tk.Text(self.wn, height = 8, width = 50, font=myFont)
        self.lbl.place(x = 10)

        # label for the output label
        self.outlbl = tk.Text(self.wn, height = 8, width = 50, font=myFont)
        self.outlbl.place(x = 10, y = 300)
        self.wn.mainloop()
    # Function for getting Input from textbox
    # and printing it at label widget
    def printInput(self, mode):
        inp = self.plaintxt.get(1.0, "end-1c")
        self.key = self.key_txt.get(1.0, "end-1c")
        if mode == "-e":
            result = Vigenere(self.key, inp, mode).translateMessage()
        else:
            result = Vigenere(self.key, inp, mode).translateMessage()

        if (mode == "-e"):

            self.lbl.delete('1.0', 'end')
            self.outlbl.delete('1.0', 'end')
            self.lbl.insert('1.0',  "Th Input Message: "+ inp + "\nThe key is : " + self.key)
            self.outlbl.insert('1.0', "encrypted message: "+ result)

        else:
            self.lbl.delete('1.0', 'end')
            self.outlbl.delete('1.0', 'end')
            self.lbl.insert('1.0', "ecrypted message: "+ inp)
            self.outlbl.insert('1.0', "decrypted message: " + result)

    def remove_space(self, txt):
        message = str()

        for i in range(len(txt)):
            if (txt[i] == " "):
                self.space_index.append(i)
            else:
                message += txt[i]
        return message
    def add_space(self, txt):
        message = str()
        ofset = 0
        for i in range(len(txt)):
            if (i + ofset) in self.space_index:
                message += " "
                ofset += 1
            message += txt[i]
        return message




class Vigenere:
    ''' implementation of vigenere cipher encryption using python '''

    def __init__(self, key = None, message = None, mode = "-e"):

        # the key message for the encrption.
        self.key = key

        # the message to be encrypted.
        self.message = message

        # english alphabet for determining the cipher value
        # of the letters.
        self.alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ\
abcdefghijklmnopqrstuvwxyz0123456789 `~!@#$%^&*()-_=+[{]}\|'\";:.>,</?"
        print(len(self.alph))
        #self.alph =  "abcdefghijklmnopqrstuvwxyz "

        # encrpt or decrypt flag
        self.mode = mode

    # Iterate over the message for
    # encrption or decrption given a key
    def translateMessage(self):

        result = []
        # check for valid value of the key
        # and the message
        if (len(self.key) == 0 or self.message == None):
            return None

        keyIndex = 0
        messIndex = 0
        for lett in self.message:
            post = self.alph.find(lett)
            if post != -1: # the letter exist in alphabet
                if self.mode == "-e":
                    if keyIndex < len(self.key):
                        post += self.alph.find(self.key[keyIndex]) # add if encrypting
                    else:
                        post += self.alph.find(self.message[messIndex])
                        messIndex += 1
                elif self.mode == "-d":
                    if keyIndex < len(self.key):
                        post -= self.alph.find(self.key[keyIndex]) # sub if decrypting
                    else:
                        post -= self.alph.find(result[messIndex])
                        messIndex += 1

                post %= len(self.alph) # handle any wrap around

                # add the encrypted or decrypted letter
                result.append(self.alph[post])

                keyIndex += 1
                # if keyIndex == len(self.key):
                #     keyIndex = 0
            else:
                # append symbol without encrypting
                result.append(lett)
        return ''.join(result)

if __name__ == "__main__":

    Input()
