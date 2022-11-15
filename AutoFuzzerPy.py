"""
PROJECT_NAME : AutoFuzzerPy (v 1.0.0)
This project made for fuzzing any software or website
AUTHOR : CodeMasterPy
License : MIT
"""
import tkinter
import keyboard
import pyautogui
from tkinter import filedialog as fd


root = tkinter.Tk()
root.title('VULN_CATCHER(v1.0.0)')
root.resizable(False,False)
root.geometry('400x200')

fileName = ""

def getPayloadFromFile():
    global fileName
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    fileName = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    print("SELECTED_FILE_PATH: "+fileName)
    root.destroy()

open_button = tkinter.Button(
    root,
    text='Open a File',
    padx=0,
    pady=0,
    height=3,
    width=10,
    command=getPayloadFromFile
)

open_button.pack(expand=True)
root.mainloop()

def showPayloadsInFile(payloadFileName):
    with open(payloadFileName) as pfp:
        for line in pfp.readlines():
            print(line)

def readPayloadFromFileAndDo(payloadFileName,instruction,repeatCount,sleepTimer):
    counter = 0
    with open(payloadFileName) as pfp:
        for line in pfp.readlines():
            counter+=1
            if counter == repeatCount:
                break
            pyautogui.write(line)
            pyautogui.press('enter')


payloadFile =open(fileName,"r")
while True:
    if keyboard.is_pressed('ctrl'):
        pyautogui.press('enter')
        readPayloadFromFileAndDo(fileName,"",0,0)

    if keyboard.is_pressed('space'):
        break


print("Fuzzing process has been completed.")
exit()

