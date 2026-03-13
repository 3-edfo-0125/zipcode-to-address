import tkinter as tk
import tkinter.ttk as ttk
from pathlib import Path
import pandas as pd
import pyperclip
import re
import unicodedata
from tkinter import messagebox
import sys

BASE_DIR = Path(__file__).resolve().parent
drop_col = [i for i in range(9, 14 + 1)] # 不要列

try:
    df = pd.read_csv(BASE_DIR / "utf_ken_all.csv")
    df = df.drop(columns=df.columns[drop_col])
    df.columns = ["全国地方公共団体コード", "旧番号", "郵便番号", "都道府県名(カタカナ)", "市区町村名(カタカナ)", "町域名(カタカナ)", "都道府県名", "市区町村名", "町域名"]
except FileNotFoundError:
    messagebox.showwarning("エラー", "郵便番号データが見つかりません")
    sys.exit()

# 検索関数
def zipcode_address(self):
    zipcode = entry1.get()
    if len(zipcode) != 7:
        return
    if not zipcode.isdigit:
        return

    zipcode = zipcode.translate(str.maketrans("零〇一壱二弐三参四五六七八九", "00112233456789"))
    zipcode = unicodedata.normalize("NFKC", zipcode)
    
    filtered = df[df["郵便番号"] == int(zipcode)]
    if filtered.empty:
        return
    
    prefecture = list(dict.fromkeys(filtered["都道府県名"].tolist()))
    city = list(dict.fromkeys(filtered["市区町村名"].tolist()))
    address = list(dict.fromkeys(filtered["町域名"].tolist()))

    pattern = r"（[^（）]*）"

    for i in range(len(address)):
        address[i] = re.sub(pattern, "", address[i])
        if address[i] == "以下に掲載がない場合":
            address[i] = ""

    entry1.delete(0, tk.END)
    entry1.insert(tk.END, zipcode)
    
    combobox1.config(values=prefecture)
    combobox1.set(prefecture[0])
    
    combobox2.config(values=city)
    combobox2.set(city[0])
    
    combobox3.config(values=address)
    combobox3.set(address[0])

# コピー関数
def address_copy():
    ad=[]
    ad.append(combobox1.get())
    ad.append(combobox2.get())
    ad.append(combobox3.get())
    ad.append(entry2.get(1.0, "end - 1 chars"))
    copy_address = "".join(ad)
    pyperclip.copy(copy_address)

# クリア関数
def clear_address():
    entry1.delete(0, tk.END)
    
    combobox1.config(values="")
    combobox1.set("")
    
    combobox2.config(values="")
    combobox2.set("")

    combobox3.config(values="")
    combobox3.set("")

    entry2.delete("1.0", tk.END)

# GUI部分
root = tk.Tk()
root.title("郵便番号→住所入力ツール")

window_width = 500
window_height= 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = tk.Frame(root)
frame.pack(expand=True)

label1 = ttk.Label(frame, text="郵便番号(ハイフンなし) :")
label1.grid(row=0, column=0, sticky="E")

entry1 = tk.Entry(frame, width=12)
entry1.grid(row=0, column=1, padx=5, sticky="W")
entry1.bind("<Return>", zipcode_address)

button1 = ttk.Button(frame, width=10, text="住所検索")
button1.grid(row=0, column=2)
button1.bind("<1>", zipcode_address)
button1.bind("<Return>", zipcode_address)

empty1 = ttk.Label(frame, text="", width=20)
empty1.grid(row=0, column=3)

label2 = ttk.Label(frame, text="都道府県 :")
label2.grid(row=1, column=0, sticky="E")

combobox1 = ttk.Combobox(frame, values="", width=10)
combobox1.grid(row=1, column=1, sticky="W", padx=5, pady=5)

label3 = ttk.Label(frame, text="市区町村 :")
label3.grid(row=2, column=0, sticky="E")

combobox2 = ttk.Combobox(frame, values="", width=40)
combobox2.grid(row=2, column=1, columnspan=3, sticky="W", padx=5)

label4 = ttk.Label(frame, text="番地など :")
label4.grid(row=3, column=0, sticky="E")

combobox3 = ttk.Combobox(frame, values="", width=40)
combobox3.grid(row=3, column=1, columnspan=3, sticky="W", padx=5, pady=5)

label5 = ttk.Label(frame, text="建物名・部屋番号 :")
label5.grid(row=4, column=0, sticky="E")

entry2 = tk.Text(frame, width=40, height=3)
entry2.grid(row=4, column=1, columnspan=3, sticky="W", padx=5)

empty2 = ttk.Label(frame, text="")
empty2.grid(row=5, column=0)

button2 = ttk.Button(frame, text="住所をコピー", width=20, command=address_copy)
button2.grid(row=6, column=0, columnspan=4, pady=5)

button3 = ttk.Button(frame, text="クリア", width=20, command=clear_address)
button3.grid(row=6, column=3)

root.mainloop()
