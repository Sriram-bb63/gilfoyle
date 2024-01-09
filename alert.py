import tkinter
from tkinter import messagebox
from threading import Thread

def alertThreadFunction(data) -> None:
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showwarning("Gilfoyle", f"Detected abnormal surge in system resources\n {data}")

def alert(data) -> None:
    alertThread = Thread(target=alertThreadFunction, args=(data,), daemon=True)
    alertThread.start()