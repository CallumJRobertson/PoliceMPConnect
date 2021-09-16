import tkinter as tk
import webbrowser

HEIGHT = 800
WIDTH = 1000

name='PoliceMP',
debug=False,
strip=False,
upx=False,
clean=True,
runtime_tmpdir=None,
console=False,
icon='./pmp.ico',
version='version.txt'

def connect_function():
    print("Connecting to PoliceMP!")
    webbrowser.open(url,new=new)

def connect_function2():
    print("Connecting to the donator server!")
    webbrowser.open("https://cfx.re/join/q8ekq9")

def connect_function3():
    print("Connecting to the development server!")
    webbrowser.open("https://cfx.re/join/xkvdre")

def website_portal():
    print("Taking user to PoliceMP.com")
    webbrowser.open("https://policemp.com")




new = 1
url = "https://cfx.re/join/q8k9av"

root = tk.Tk()
root.title("PoliceMP Connect Tool")
root.iconbitmap('./pmp.ico')


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.place(x=150,y=60)
canvas.pack()

background_image = tk.PhotoImage(file="./images/pmp1.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

connectButtonImage=tk.PhotoImage(file="./images/connect.png")
button = tk.Button(image=connectButtonImage, command=connect_function, highlightthickness = 0, bd = 0)
button.place(relx=0.45, rely=0.5, relwidth=0.19, relheight=0.08)

donatorButtonImage=tk.PhotoImage(file="./images/Donator.png")
button = tk.Button(image=donatorButtonImage, command=connect_function2, highlightthickness = 0, bd = 0)
button.place(relx=0.45, rely=0.6, relwidth=0.19, relheight=0.08)

developmentButtonImage=tk.PhotoImage(file="./images/development.png")
button = tk.Button(image=developmentButtonImage, command=connect_function3, highlightthickness = 0, bd = 0)
button.place(relx=0.45, rely=0.7, relwidth=0.19, relheight=0.08)

LogoButtonImage=tk.PhotoImage(file="./images/logo.png")
button = tk.Button(image=LogoButtonImage, command=website_portal, highlightthickness = 0, bd = 0)
button.place(relx=0.47, rely=0.2,)

logo = tk.PhotoImage(file="./images/logo.png")
canvas.create_image(30,30,image=logo)



root.mainloop()
