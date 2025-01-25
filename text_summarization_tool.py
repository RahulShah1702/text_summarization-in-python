import tkinter as tk
from tkinter import filedialog, messagebox, Scrollbar
from transformers import pipeline
import os
from tkinter import ttk

# Function to summarize text
def summarize_text(input_text, max_length=150, min_length=50):
    try:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(input_text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    except ModuleNotFoundError as e:
        return f"Error: {e}. Ensure that required packages are installed."

# Function to open a file and load its content
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            input_text.delete(1.0, tk.END)
            input_text.insert(tk.END, file.read())

# Function to save the summary to a file
def save_summary():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(output_text.get(1.0, tk.END))
        messagebox.showinfo("Success", "Summary saved successfully!")

# Function to generate a summary for the input text
def generate_summary():
    input_content = input_text.get(1.0, tk.END).strip()
    if not input_content:
        messagebox.showwarning("Warning", "Please enter or load text to summarize.")
        return

    try:
        summary = summarize_text(input_content)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, summary)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during summarization: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Text Summarization Tool")
root.geometry("900x700")
root.configure(bg="#f0f8ff")

# Style configuration
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabelFrame", font=("Helvetica", 14, "bold"), background="#f0f8ff", foreground="#333")
style.configure("TText", font=("Helvetica", 12))

# Input Text Section
input_frame = ttk.LabelFrame(root, text="Input Text", padding=10)
input_frame.pack(fill="both", expand=True, padx=10, pady=10)

scrollbar_y = Scrollbar(input_frame, orient="vertical")
scrollbar_y.pack(side="right", fill="y")

input_text = tk.Text(input_frame, wrap=tk.WORD, height=12, yscrollcommand=scrollbar_y.set, bg="#e6f7ff", fg="#333", font=("Helvetica", 12))
input_text.pack(fill="both", expand=True, padx=5, pady=5)
scrollbar_y.config(command=input_text.yview)

# Buttons for input text
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

load_button = ttk.Button(button_frame, text="Load Text File", command=open_file)
load_button.pack(side="left", padx=10)

summarize_button = ttk.Button(button_frame, text="Summarize", command=generate_summary)
summarize_button.pack(side="left", padx=10)

# Output Text Section
output_frame = ttk.LabelFrame(root, text="Summary", padding=10)
output_frame.pack(fill="both", expand=True, padx=10, pady=10)

output_scrollbar_y = Scrollbar(output_frame, orient="vertical")
output_scrollbar_y.pack(side="right", fill="y")

output_text = tk.Text(output_frame, wrap=tk.WORD, height=12, yscrollcommand=output_scrollbar_y.set, bg="#e6ffe6", fg="#333", font=("Helvetica", 12), state=tk.NORMAL)
output_text.pack(fill="both", expand=True, padx=5, pady=5)
output_scrollbar_y.config(command=output_text.yview)

# Buttons for output text
output_button_frame = ttk.Frame(root)
output_button_frame.pack(pady=10)

save_button = ttk.Button(output_button_frame, text="Save Summary", command=save_summary)
save_button.pack(side="left", padx=10)

exit_button = ttk.Button(output_button_frame, text="Exit", command=root.quit)
exit_button.pack(side="left", padx=10)

# Add transition effects
for widget in button_frame.winfo_children() + output_button_frame.winfo_children():
    widget.bind("<Enter>", lambda e, w=widget: w.configure(style="TButtonHover"))
    widget.bind("<Leave>", lambda e, w=widget: w.configure(style="TButton"))

style.map("TButtonHover", background=[("active", "#add8e6")], foreground=[("active", "#000")])

root.mainloop()
