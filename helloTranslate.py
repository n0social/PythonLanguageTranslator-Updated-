#Imports - Step 1

from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import customtkinter

#Setting up the Tkinter Window - # Step 2
root_tk = customtkinter.CTk() #Initialize a root window
root_tk.geometry('200x320') #Set the size of the window
customtkinter.set_appearance_mode("dark")
#root_tk.resizable(0,0) #Set it to a resizable
#root_tk['bg'] = 'blue' #Change the background color to blue
root_tk.title('Google Translator') #Give the window a title

#Creating the GUI - Step 3

label = customtkinter.CTkLabel(master=root_tk, text="Language Translator", font=('Poppins', 20))
label.place(x=10,y=10)

label2 = customtkinter.CTkLabel(master=root_tk, text="Enter Text:", font=('Poppins', 20))
label2.place(x=30,y=50)

Input_text = customtkinter.CTkEntry(master=root_tk, width=150,height=15)
Input_text.place(x=30,y=90)

OutputLabel = customtkinter.CTkLabel(master=root_tk, text="Output:", font=('Poppins', 20))
OutputLabel.place(x=30, y=120)

Output_text = customtkinter.CTkTextbox(master=root_tk, font=('Poppins', 20), height=50, wrap=WORD, width=150)
Output_text.place(x=30, y=150)

language = list(LANGUAGES.values())
dest_lang = customtkinter.CTkComboBox(master=root_tk, values=language, width=150)
dest_lang.place(x=30,y=220)
dest_lang.set('Choose a Language')

#Translation function - Step 4
#The function uses the googletrans library to translate text from an entry
#widget ("input_text") to a specified destination language. It clears the
#output text widget ("Output_text") before inserting the translated text.
#Any errors will print out an error 

def Translate():
    try:
        translator = Translator()
        translation = translator.translate(Input_text.get(), dest=dest_lang.get())
        Output_text.delete(1.0, END)
        Output_text.insert(END,translation.text)
    except Exception as e:
        print(f"Translation error: {e}")
        
#Button for triggering Translation - Step 5
trans_btn = customtkinter.CTkButton(master=root_tk, text="Translate", font=('Poppins', 20), command=Translate)
trans_btn.place(x=30,y=270)

#Run the main loop - Step 6
root_tk.mainloop()