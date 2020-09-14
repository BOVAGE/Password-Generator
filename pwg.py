import tkinter as tk
import string, random, pyperclip, time

root = tk.Tk()
root.configure(bg = "#002699")

alphabets = string.ascii_letters
punctuations = string.punctuation
numbers = string.digits

def generatepassword(strength, length):
    """ generates password and return password as string """
    length = int(length)
    copyUpdate.grid_forget()
    if strength.lower() == "weak":
        password = "".join(random.choices(alphabets, k = int((60/100)*length))) + \
                   "".join(random.choices(numbers, k = round((40/100)*length)))
        return password
    elif strength.lower() == "medium":
        password = "".join(random.choices(alphabets, k = int((40/100)*length))) + \
                   "".join(random.choices(numbers, k = int((30/100)*length))) + \
                   "".join(random.choices(punctuations, k = int((30/100)*length)))
        return password
    elif strength.lower() == "strong":
        password = "".join(random.sample(alphabets, k = int((20/100)*length))) + \
                   "".join(random.sample(punctuations, k = int ((40/100)*length))) + \
                   "".join(random.sample(numbers, k = int ((40/100)*length)))
        return password

def validatelength(password, length):
    """ checks the accuracy of the length of the password. """
    if len(password) == length:
        return password
    else:
        password = "".join(random.sample(numbers, k = abs(length - len(password)))) + password
        return password                                   
            
def getpwd():
    """ display the password to the suitable widjet. """
    password = generatepassword(strength.get(),length.get())
    finalpassword = validatelength(password, length.get())
    screenpw.set(finalpassword)

copyUpdate = tk.Label(root, text = "Password copied to clipboard")
def copy(text):
    """ copies the password to clipboard """
    pyperclip.copy(text)
    copyUpdate.grid(row = 1, column = 0)

def savetotxt(text):
    """ saves the password to a text file """
    with open("password.txt", "a") as pwdtxt:
        pwdtxt.write("\n" + text)
    
password = tk.StringVar()
#the value is set to weak so as to prevent the radiobuttons from being rendered
#or set the tristatevalue to 0 in the tri-state mode cause the tristatevalue by
#default is an empty string and the StringVar too is an empty
strength = tk.StringVar(value = "weak")
length = tk.IntVar()
screenpw = tk.StringVar()

titleLabel = tk.Label(root, text = "Password Generator", font = ("Arial", 20, "bold"),
                      anchor =  "center", fg = "white", bg = "#002699")
titleLabel.grid(row = 0, column = 0, columnspan = 2)
screenEntry = tk.Entry(root, width = 20, textvariable = screenpw, relief = "raised",
                  font = ("Helvetica", "17", "bold"), fg = "#000000", bg = "#ffffff")
screenEntry.grid(row = 2, column = 0, columnspan = 2, pady = 10, padx = 10)

copyButton = tk.Button(root, text = "copy", command = lambda:copy(screenEntry.get()))
copyButton.grid(row = 2, column = 2)

fileButton = tk.Button(root, text = "Text", command = lambda: savetotxt(screenEntry.get()))
fileButton.grid(row = 2, column = 3)

lengthLabel = tk.Label(root, text = "Password Length", font = ("Arial", 16, "normal"),
                       bg = "#002699", fg = "white")
lengthLabel.grid(row = 3, column = 0, sticky = "W", padx = 10)

lengthSb = tk.Spinbox(root, from_ = 5, to = 15, textvariable = length)
lengthSb.grid(row = 3, column = 1)


strengthLbFrame = tk.LabelFrame(root, text = "Password Strength", fg = "#ffffff",
                    font = ("Arial", "16", "normal"), bg = "#002699")
strengthLbFrame.grid(row = 4, column = 0, sticky = "W", pady = 10, padx = 10)

option1 = tk.Radiobutton(strengthLbFrame, text = "Strong", font = ("Times", 14, "normal"), fg = "#ffffff",
                         bg = "#002699", variable = strength, value = "strong"
                         ,selectcolor = "black")
option1.grid(row = 5, column = 0, sticky = "W")

option2 = tk.Radiobutton(strengthLbFrame, text = "Medium", font = ("Times", 14, "normal"), fg = "#ffffff",
                         bg = "#002699", variable = strength, value = "medium"
                         ,selectcolor = "black")
option2.grid(row = 6, column = 0, sticky = "W")

option3 = tk.Radiobutton(strengthLbFrame, text = "Weak", font = ("Times", 14, "normal"), fg = "#ffffff",
                         bg = "#002699", variable = strength, value = "weak"
                         ,selectcolor = "black")
option3.grid(row = 7, column = 0, sticky = "W")

getbtn = tk.Button(root, text = "Generate password", font = ("Times", 17, "normal"),
                        bg = "blue", fg = "white", width = 20, command = lambda: getpwd())
getbtn.grid(row = 8, column = 0, columnspan = 2, padx = 10, pady = 10)

root.mainloop()
