import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd


def clean_terminal():
    os.system("cls")


def add_new_tickers():
    print("Type the tickers you want...")
    tickers_list = list()
    decision = True
    while decision:
        clean_terminal()
        tickers_list.append(input("Type a Ticker: "))
        value = input("Do you want to add another ticker? [y / n] \n")
        if value == "y":
            decision = True
            clean_terminal()
        elif value == "n":
            decision = False
            clean_terminal()
        else:
            clean_terminal()
            print("type a valid response!")
    print(f" The tickers to be added are: {tickers_list}")
    return tickers_list


def select_file():
    file_path = filedialog.askopenfilename(
        title="Select an excel workbook",
        filetypes=[("Excel files", "*.xlsx;*.xls")],
    )

    if file_path:
        df = pd.read_excel(file_path)
        print("Selected File: ")
        return df

    root = tk.Tk()
    root.attributes('-topmost', True)
    botao_selecionar = tk.Button(root, text="Selecionar Arquivo Excel", command=select_file)
    botao_selecionar.pack(pady=20)

    root.mainloop()
