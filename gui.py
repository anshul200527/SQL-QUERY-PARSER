import tkinter as tk
from tkinter import messagebox
import ctypes

parser = ctypes.CDLL("./sql_parser.so")
parser.parse_sql.restype = ctypes.c_int
parser.parse_sql.argtypes = [ctypes.c_char_p]

def parse_input():
    query = input_text.get("1.0", tk.END).strip()
    if not query:
        output_text.insert(tk.END, "⚠ No input provided.\n")
        return

    result = parser.parse_sql(query.encode("utf-8"))
    if result == 0:
        output_text.insert(tk.END, "✅ SQL query parsed successfully! Correct Querry ✅ \n")
    else:
        output_text.insert(tk.END, "❌ SQL query parsing failed. Wrong Querry \n")

def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


root = tk.Tk()
root.title("SQL Query Parser")
root.geometry("700x500")
root.configure(bg="#f4f7fa")

# Fonts
header_font = ("Helvetica", 16, "bold")
text_font = ("Consolas", 12)


header = tk.Label(root, text="SQL Query Parser", bg="#4A90E2", fg="white", font=header_font, pady=10)
header.pack(fill=tk.X)


input_frame = tk.Frame(root, bg="#f4f7fa", padx=15, pady=10)
input_frame.pack(fill=tk.BOTH, expand=True)

tk.Label(input_frame, text="Enter SQL Query:", bg="#f4f7fa", font=("Arial", 13)).pack(anchor="w", pady=(0, 5))

input_text = tk.Text(input_frame, height=6, font=text_font, bg="#ffffff", bd=2, relief="solid", insertbackground="black")
input_text.pack(fill=tk.BOTH, expand=True)


btn_frame = tk.Frame(root, bg="#f4f7fa", pady=10)
btn_frame.pack()

parse_btn = tk.Button(btn_frame, text="🚀 Parse", bg="#2ecc71", fg="white", font=("Arial", 12, "bold"),
                      activebackground="#27ae60", padx=20, pady=5, command=parse_input)
parse_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="🧹 Clear", bg="#e74c3c", fg="white", font=("Arial", 12, "bold"),
                      activebackground="#c0392b", padx=20, pady=5, command=clear_all)
clear_btn.grid(row=0, column=1, padx=10)


output_frame = tk.Frame(root, bg="#f4f7fa", padx=15, pady=10)
output_frame.pack(fill=tk.BOTH, expand=True)

tk.Label(output_frame, text="Parser Output:", bg="#f4f7fa", font=("Arial", 13)).pack(anchor="w", pady=(0, 5))

output_text = tk.Text(output_frame, height=8, font=text_font, bg="#fdf6e3", bd=2, relief="solid", insertbackground="black")
output_text.pack(fill=tk.BOTH, expand=True)


root.mainloop()
