from tkinter import *
import tkinter.filedialog as fd
from PIL import ImageTk, Image
import os

# Configure App
root = Tk()
root.configure(background = "black")
root.geometry("1000x800")
root.title("IOM")
root.resizable(False, False)

root.grid_rowconfigure(0, weight = 0)
root.grid_columnconfigure(0, weight = 1)

img = ImageTk.PhotoImage(Image.open("logo.png"))
logo = Label(root, image = img, borderwidth = 0)
logo.grid(row = 0, column = 0, pady = (40, 40))
logo.grid_rowconfigure(0, weight = 0)
logo.grid_columnconfigure(0, weight = 1)

canvas = Canvas(root, width = 500, height = 550)
canvas.grid(row = 1, column = 0)

def openFile():
    filepath = fd.askopenfilename(title='select', filetypes= [("all wav format", ".wav")]) 
    fileNameText.insert("end", os.path.basename(filepath))

def translate():
    print(5)

fromLanguageLabel = Label(root, text = "Alege limba din care doresti sa traduci:", font=("Arial", 17))
fromLanguageLabel.place(x = 300, y = 225)

fromLanguage = StringVar(root, "0")

fromRomanianRadio = Radiobutton(root, text = 'Romana', variable = fromLanguage, indicator = 1, value = 1, font = ("Arial", 11))
fromRomanianRadio.place(x = 300, y = 275)

fromEnglishRadio = Radiobutton(root, text = 'Engleza', variable = fromLanguage, indicator = 2, value = 2, font = ("Arial", 11))
fromEnglishRadio.place(x = 400, y = 275)

fromSpanishRadio = Radiobutton(root, text = 'Spaniola', variable = fromLanguage, indicator = 3, value = 3, font = ("Arial", 11))
fromSpanishRadio.place(x = 500, y = 275)

fromFrenchRadio = Radiobutton(root, text = 'Franceza', variable = fromLanguage, indicator = 4, value = 4, font = ("Arial", 11))
fromFrenchRadio.place(x = 600, y = 275)

toLanguageLabel = Label(root, text = "Alege limba in care doresti sa traduci:", font=("Arial", 16))
toLanguageLabel.place(x = 300, y = 325)

toLanguage = StringVar(root, "0")

toRomanianRadio = Radiobutton(root, text = 'Romana', variable = toLanguage, indicator = 1, value = 1, font = ("Arial", 11))
toRomanianRadio.place(x = 300, y = 375)

toEnglishRadio = Radiobutton(root, text = 'Engleza', variable = toLanguage, indicator = 2, value = 2, font = ("Arial", 11))
toEnglishRadio.place(x = 400, y = 375)

toSpanishRadio = Radiobutton(root, text = 'Spaniola', variable = toLanguage, indicator = 3, value = 3, font = ("Arial", 11))
toSpanishRadio.place(x = 500, y = 375)

toFrenchRadio = Radiobutton(root, text = 'Franceza', variable = toLanguage, indicator = 4, value = 4, font = ("Arial", 11))
toFrenchRadio.place(x = 600, y = 375)

fileTypeLabel = Label(root, text = "Traducere din fisier de tip:", font=("Arial", 16))
fileTypeLabel.place(x = 300, y = 425)

fileType = StringVar(root, "0")

textFileType = Radiobutton(root, text = 'Text', variable = fileType, indicator = 1, value = "text", font = ("Arial", 11))
textFileType.place(x = 300, y = 475)

audioFileType = Radiobutton(root, text = 'Audio', variable = fileType, indicator = 2, value = "audio", font = ("Arial", 11))
audioFileType.place(x = 400, y = 475)

chooseFileLabel = Label(root, text = "Alege fisierul pe care doresti sa il traduci:", font = ("Arial", 16))
chooseFileLabel.place(x = 300, y = 525)

findFileButton = Button(root, text ='Cauta fisier', command = openFile)
findFileButton.place(x = 300, y = 575)

fileNameText = Text(root, height = 1, width = 35)
fileNameText.place(x = 400, y = 579) 

translateButton = Button(root, width = 31, height = 1, bg = '#ff9900', text ='Traducere', command = translate, font = ("Arial", 16))
translateButton.place(x = 300, y = 625)

root.mainloop()