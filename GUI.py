import tkinter as tk
from tkinter import filedialog, Text
#to run app
import os
#holds structure
root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        #generate array of apps
        tempApps = tempApps.split(',')
        #remove empty spaces
        apps = [x for x in tempApps if x.strip()]


def addApp()

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = (("executables","*.exe"),("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg = "gray")
        label.pack()
def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height = 800, width = 800, bg = "#263D42")
canvas.pack()

frame = tk.Frame(root, bg = "white")
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.2, rely = 0.2)

#add buttons
openFile = tk.Button(root, text = "Open File", padx = 10, pady = 5, fg = "white", bg = "#263D42", command = addApp )
openFile.pack()

runApps = tk.Button(root, text = "Run Apps", padx = 10, pady = 5, fg = "white", bg = "#263D42", command = runApps)
runApps.pack()


for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()

root.mainloop()
#when app is closed, apps will be written to text file
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
