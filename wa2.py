import tkinter as tk
from PIL import Image, ImageTk 
import tkinter.messagebox
from tkinter.constants import SUNKEN

# Membuat window utama
window = tk.Tk()
window.title('Calculator - Cr: Tommy G.')

# Aktifkan mode fullscreen
window.attributes('-fullscreen', True)

# Membaca gambar background menggunakan PIL
bg_image = Image.open("WEB KACAW/fto/1316292.jpeg")
bg_image = bg_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Membuat Canvas untuk background image
canvas = tk.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Frame di atas canvas
frame = tk.Frame(master=window, bg="grey", padx=10)
frame.place(relx=0.5, rely=0.5, anchor='center')  # Tempatkan frame di tengah layar

# Entry field
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=25, font=("arial",20,"bold"), width=30, justify="right")
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2, sticky="nsew")

# Fungsi untuk memasukkan angka ke dalam entry
def myclick(number):
    entry.insert(tk.END, number)

# Fungsi untuk menghitung hasil
def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

# Fungsi untuk membersihkan entry
def clear():
    entry.delete(0, tk.END)

def percentage(sign):
    current_entry = entry.get()
    if sign == '%':
        try:
            result = float(current_entry) / 100
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except ValueError:
            print("Error: Invalid input")

# Pembuatan tombol angka dan operasi
button_1 = tk.Button(master=frame, text='1', padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick(1))
button_1.grid(row=4, column=0, pady=2, sticky="nsew")
button_2 = tk.Button(master=frame, text='2', padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick(2))
button_2.grid(row=4, column=1, pady=2, sticky="nsew")
button_3 = tk.Button(master=frame, text='3', padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick(3))
button_3.grid(row=4, column=2, pady=2, sticky="nsew")
button_4 = tk.Button(master=frame, text='4', padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick(4))
button_4.grid(row=3, column=0, pady=2, sticky="nsew")
button_5 = tk.Button(master=frame, text='5', padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick(5))
button_5.grid(row=3, column=1, pady=2, sticky="nsew")
button_6 = tk.Button(master=frame, text='6', padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick(6))
button_6.grid(row=3, column=2, pady=2, sticky="nsew")
button_7 = tk.Button(master=frame, text='7', padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick(7))
button_7.grid(row=2, column=0, pady=2, sticky="nsew")
button_8 = tk.Button(master=frame, text='8', padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick(8))
button_8.grid(row=2, column=1, pady=2, sticky="nsew")
button_9 = tk.Button(master=frame, text='9', padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick(9))
button_9.grid(row=2, column=2, pady=2, sticky="nsew")
button_0 = tk.Button(master=frame, text='0', padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick(0))
button_0.grid(row=6, column=1, pady=2, sticky="nsew")
button_00 = tk.Button(master=frame, text='00', padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick('00'))
button_00.grid(row=6, column=0, pady=4, sticky="nsew")

button_add = tk.Button(master=frame, text="+", padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick('+'))
button_add.grid(row=4, column=3, pady=2, sticky="nsew")
button_subtract = tk.Button(master=frame, text="-", padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick('-'))
button_subtract.grid(row=3, column=3, pady=2, sticky="nsew")
button_multiply = tk.Button(master=frame, text="x", padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick('*'))
button_multiply.grid(row=2, column=3, pady=2, sticky="nsew")
button_div = tk.Button(master=frame, text="/", padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=lambda: myclick('/'))
button_div.grid(row=1, column=3, pady=2, sticky="nsew")
button_clear = tk.Button(master=frame, text="c", padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=clear)
button_clear.grid(row=1, column=0, columnspan=1, pady=2, sticky="nsew")
button_equal = tk.Button(master=frame, text="=", padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=equal)
button_equal.grid(row=6, column=3, columnspan=2, pady=2, sticky="nsew")

button_percentage= tk.Button(master=frame, text="%", padx=15, pady=5, width=3,bd=8,fg="black",font=("arial",20,"bold"), command=percentage)
button_percentage.grid(row=7, column=3, columnspan=2, pady=2, sticky="nsew")

# Mengatur grid layout untuk tombol
for i in range(8):
    frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame.grid_columnconfigure(j, weight=1)

# Fungsi fullscreen
def toggle_fullscreen(event=None):
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)

def end_fullscreen(event=None):
    window.attributes('-fullscreen', False)

# Bind untuk mengaktifkan dan menonaktifkan fullscreen
window.bind('<F11>', toggle_fullscreen)
window.bind('<Escape>', end_fullscreen)

# Jalankan window
window.mainloop()