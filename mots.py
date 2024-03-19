import tkinter as tk
from tkinter import filedialog, messagebox
import random

class WordLearningApp:
    def __init__(self, master):
        self.master = master
        self.master.title("给我背！")
        self.master.geometry("500x300")

        self.words = []
        self.remaining_words = []

        self.word_label = tk.Label(self.master, text="", font=("Helvetica", 40))
        self.word_label.pack(pady=30)

        self.next_button = tk.Button(self.master, text="suivant", command=self.show_next_word)
        self.next_button.pack(pady=5)

        self.load_button = tk.Button(self.master, text="choisissez le fichier", command=self.load_word_file)
        self.load_button.pack(pady=5)

        self.info_label = tk.Label(self.master, text="", font=("Helvetica", 15))
        self.info_label.pack(pady=5)

    def load_word_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.words = self.load_words(file_path)
            self.remaining_words = self.words.copy()
            self.update_info_label()

    def load_words(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            words = file.readlines()
        return [word.strip() for word in words]

    def show_next_word(self):
        if self.remaining_words:
            word = random.choice(self.remaining_words)
            self.word_label.config(text=word)
            self.remaining_words.remove(word)
            self.update_info_label()
        else:
            messagebox.showinfo("提示", "已经背完所有单词！")

    def update_info_label(self):
        remaining_count = len(self.remaining_words)
        learned_count = len(self.words) - remaining_count
        self.info_label.config(text=f"déjà appris:{learned_count}\nmots restants:{remaining_count}")

def main():
    root = tk.Tk()
    app = WordLearningApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
