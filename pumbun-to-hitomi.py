import sys
import time
import threading
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.edge.options import Options


def open_page(_pumbun: str, edge_options):
    edge_driver = webdriver.Edge(edge_options)
    edge_driver.get("https://hitomi.la/reader/" + _pumbun + ".html#1")


def on_button_click():
    if not pumbun_text.get() or pumbun_text.get() == placeholder:
        sys.exit()

    pumbun_list = pumbun_text.get().split(" ")
    edge_options = Options()
    edge_options.add_experimental_option("detach", True)

    for pumbun in pumbun_list:
        hitomi_thread = threading.Thread(target=lambda: open_page(pumbun, edge_options))
        hitomi_thread.start()

        time.sleep(3)

    sys.exit()


def focus_in(*args):
    if pumbun_text.get() == placeholder:
        select_entry.delete(0, "end")
        select_entry.configure(fg="black")


def focus_out(*args):
    if not pumbun_text.get():
        select_entry.configure(fg="gray")
        select_entry.insert(0, placeholder)


if __name__ == "__main__":
    window = tk.Tk()
    window.iconbitmap("hitomi.ico")
    window.title("")
    window.resizable(False, False)

    placeholder = "Hitomi 품번을 입력하세요"
    pumbun_text = tk.StringVar()
    select_entry = tk.Entry(window, textvariable=pumbun_text, fg="gray")
    select_entry.insert(0, placeholder)
    select_entry.bind("<FocusIn>", focus_in)
    select_entry.bind("<FocusOut>", focus_out)
    select_entry.grid(column=0, row=0, padx=20, pady=20)

    open_button = tk.Button(window, text="OPEN", command=on_button_click)
    open_button.grid(column=0, row=1, pady=10)

    window.mainloop()
