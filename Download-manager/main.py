from tkinter import *
from download import download
root = Tk()
root.configure(background="#f2f2f2")
root.title("Download-manager by VishalKD")
root.geometry("602x150")
root.resizable(False,False)

def download_file():
    #C:\Users\Vishal\Downloads
    url = link.get()
    path = download(url, fn.get(), replace=True, timeout=10)

link = Entry(root, width=50, font=("Verdana",12))
dl = Label(root, text="Download link")
dl1 = Label(root, text="file name with Extension")
fn = Entry(root, width=30, font=("Verdana",12))
download_button = Button(root, text="Download", command=download_file)
dl.pack()
link.pack()
dl1.pack()
fn.pack()
download_button.pack()
root.mainloop()