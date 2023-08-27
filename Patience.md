# Patience License

Yes we are not a team, In fact not "we" I supposedlly I am the only worker @Adam210Adam 
Perhaps it is really hard to create a operating system in "Python" to show you the code
here is the code:


    import tkinter
    import random
    import time
    import os
    from PIL import ImageTk, Image
    from pathlib import Path
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
    class App:
        def __init__(self, App_name: str, App_version: float, App_properties: dict, virus, *args):
            self.Appname = App_name
            self.AppVersion = App_version
            self.AppProperties = App_properties
            self.Virus = virus
            self.Options = self.Commands = args
        def verify(self):
            if not self.Virus:
                print(color.GREEN, color.BOLD, F"Verified App {self.Appname}✔", color.END)
            elif self.Virus:
                print(color.RED, color.BOLD, F"Virus Detected in {self.Appname}✖")
                time.sleep(1)
                print("Deleting Virus")
                time.sleep(3)
                print(color.GREEN, color.BOLD, F"Deleted Virus in App {self.Appname}✔", color.END)
                self.Virus = False
        def run(self):
            if self.Virus:
                for ranges in range(1, 60):
                    print("Haha YOU GOT A VIRUS")
    class Game(App):
        def Play():
            '''
            #To Do#
            '''
    for INITIALIZE_ASSEMBLY in range(random.randint(1, 7)):
        print(color.BOLD, color.BLUE + "Initializing Assembly..." + color.END)
        time.sleep(0.5)
        os.system("cls")
        print(color.BOLD, color.BLUE + "Initializing Assembly." + color.END)
        time.sleep(0.5)
        os.system("cls")
        print(color.BOLD, color.BLUE + "Initializing Assembly.." + color.END)
        time.sleep(0.5)
        os.system("cls")
        print(color.BOLD, color.BLUE + "Initializing Assembly..." + color.END)
        time.sleep(0.5)
    camera = App("Camera", 1.0, {}, False)
    time.sleep(0.3)
    calculator = App("Calculator", 1.0, {}, False)
    time.sleep(0.3)
    Checkboard = Game("Checkboard", 1.0, {}, False)
    time.sleep(0.3)
    Minecraft = Game("Minecraft", 1.0, {}, False)
    time.sleep(0.3)
    Roblox = App("Roblox", 1.0, {}, False)
    time.sleep(0.3)
    Antivirus_Avast = App("Antivirus Avast", 1.0, {}, True)
    Apps = [camera, calculator, Checkboard, Minecraft, Roblox, Antivirus_Avast]
    for App_verify in Apps:
        App_verify.verify()
        time.sleep(0.5)
    time.sleep(2)
    BOOTL = tkinter.Tk()
    BOOTL.state("zoomed")
    BOOTL.configure(bg="#093689")
    def destroy(root):
        root.destroy()
        call(1)
    class innerOperator:
        def innerAddFile():
            filename = ""
            def printfilename(n: tkinter.Text, e: tkinter.Text, f):
                nonlocal filename
                names = n.get("1.0","end-1c")
                extinsions = e.get("1.0", tkinter.END)
                filename += f"{names}.{extinsions}"
                my_file = Path(f"./{filename}")
                os.system(f"msg * Created {filename}.")
                open(filename.replace("\n", ""), "w")
                filename = ""
            addf = tkinter.Tk()
            name = tkinter.Text(addf)
            name.place(x=10, y=10)
            extinsion = tkinter.Text(addf)
            extinsion.place(x=10, y=50)
            butt = tkinter.Button(addf, text="Create", command=lambda: printfilename(name, extinsion, addf)).place(x=10, y=150)
        def innerCall(rootsan: tkinter.Tk):
            rootsan.destroy()
            root = tkinter.Tk()
            root.state("zoomed")
            img = tkinter.PhotoImage(file=r"BGdefault.png")
            img2 = tkinter.PhotoImage(file=r"file-add-line.png")
            img3 = tkinter.PhotoImage(file=r"search-line.png")
            panel = tkinter.Label(root, image = img).pack(fill="both", expand="yes")
            TBACK = tkinter.Label(root, text="..................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................", bg="black", height=3).place(x=0, y=0)
            addfile = tkinter.Button(image=img2, command=innerOperator.innerAddFile).place(x=10, y=10)
            SearchBar = tkinter.Text(height=2, width=40, font=("Arial", 10)).place(y=10, x=50)
            searchicon = tkinter.Label(root, image = img3).place(y=10, x=50)
            root.mainloop()
    def call(page):
        if page == 1:
            ARE = tkinter.Tk()
            ARE.configure(bg="#093689")
            ARE.state("zoomed")
            tkinter.Label(text="Are you sure?", font=("Arial", 45), bg="#093689", fg="white").place(x=30, y=30)
            tkinter.Button(text="Yes", bg="#093689", fg="white", font=("Arial", 50), command=lambda: innerOperator.innerCall(ARE)).place(x=10, y=150)
            tkinter.Button(text="No", bg="#093689", fg="white", font=("Arial", 50), command=lambda: ARE.destroy()).place(x=500, y=150)
    tkinter.Button(text="LINUX_DG_1", bg="#093689", fg="white", font=("Arial", 50), command=lambda: destroy(BOOTL)).place(x=10, y=10)
    q = tkinter.Button(text="LINUX_DG_2", bg="#093689", fg="white", font=("Arial", 50), command=lambda: os.startfile("error.vbs")).place(x=10, y=150)
    a = tkinter.Button(text="LINUX_DG_3", bg="#093689", fg="white", font=("Arial", 50), command=lambda: os.startfile("error.vbs")).place(x=10, y=300)
    r = tkinter.Button(text="LINUX_DG_4", bg="#093689", fg="white", font=("Arial", 50), command=lambda: os.startfile("error.vbs")).place(x=10, y=460)
    l = tkinter.Button(text="LINUX_DG_5", bg="#093689", fg="white", font=("Arial", 50), command=lambda: os.startfile("error.vbs")).place(x=10, y=650)
    tkinter.Label(text='''Intelligente
    DataGarm''', font=("Arial", 50), bg="#093689", fg="white").place(x=1200, y=10)
    BOOTL.mainloop()
