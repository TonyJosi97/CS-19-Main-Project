import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox
import subprocess


def sendMailCallBack():
    def sendthemail():
        to = a1.get()
        sub = b1.get()
        cont = c1.get("1.0", tk.END)

        """
        print(isinstance(to, str))
        print(isinstance(sub, str))
        print(isinstance(cont, str))
        """

        f = open("plain", "w+")
        f.write(cont)
        fs = open("subject", "w+")
        fs.write(sub)
        ft = open("to", "w+")
        ft.write(to)
        f.close()
        fs.close()
        ft.close()

        processText = subprocess.Popen(["./processText.sh", "plain"])
        processText.wait()

        sendMail = subprocess.Popen(["./sendMail.sh", "to", "subject"])
        sendMail.wait()

        var = tk.messagebox.showinfo("Send Mail", "Succesfully Sent Mail!!")

        a1.delete(0, tk.END)
        b1.delete(0, tk.END)
        c1.delete("1.0", tk.END)

    def closeWindow():
        smWin.destroy()

    smWin = tk.Toplevel(window)
    smWin.title("Send Mail")
    smWin.geometry("600x400")
    smWin.configure(background="grey")
    a = tk.Label(smWin, text="To: ").grid(row=0, column=0)
    b = tk.Label(smWin, text="Subject: ").grid(row=1, column=0)
    c = tk.Label(smWin, text="Email Content: ").grid(row=2, column=0)
    a1 = tk.Entry(smWin, width="50")
    a1.grid(row=0, column=1)
    b1 = tk.Entry(smWin, width="50")
    b1.grid(row=1, column=1)
    # c1 = Entry(smWin,width="50")
    # c1.grid(row=2,column=1,padx=5,pady=10,ipady=100)
    c1 = ScrolledText(smWin, width=62, height=15, selectborderwidth=2)
    c1.grid(row=2, column=1)
    tk.Button(
        smWin, text="Send", highlightbackground="#3E4149", command=sendthemail
    ).place(relx=0.45, rely=0.85, anchor=tk.CENTER)
    tk.Button(
        smWin, text="Go Back", highlightbackground="#3E4149", command=closeWindow
    ).place(relx=0.55, rely=0.85, anchor=tk.CENTER)


window = tk.Tk()
window.title("Welcome to Secure Mail Sender")
window.geometry("400x400")
window.configure(background="grey")


def closeWindow():
    window.destroy()


btn = ttk.Button(window, text="Send Mail", command=sendMailCallBack).place(
    relx=0.5, rely=0.35, anchor=tk.CENTER
)
btn = ttk.Button(window, text="Extract Data").place(
    relx=0.5, rely=0.55, anchor=tk.CENTER
)
btn = ttk.Button(window, text="Quit", command=closeWindow).place(
    relx=0.5, rely=0.75, anchor=tk.CENTER
)
window.mainloop()