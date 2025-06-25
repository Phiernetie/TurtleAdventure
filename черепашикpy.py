import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

countries = [
    {"name": "Франция", "description": "Тут всегда пекут багеты,\nКруассаны — как конфеты.\nСто сортов сыров найдёшь —\nИ Лувр весь ты обойдёшь"},
    {"name": "Япония", "description": "Там сакура весной цветёт,\nИ Фудзи в облака встаёт.\nСуши, чай и иероглиф —\nВосточный мир — как стих без слов."},
    {"name": "Бразилия", "description": "Карнавал и самба в ритме,\nСолнце пляшет в каждый бит.\nАмазонка — дух живой,\nСтрана уж в пляс идет с тобой."},
    {"name": "Египет", "description": "Пирамиды в горячих песках блестят,\nСфинкс загадки всем шепчет подряд,\nРека большая жизнь несет,\nЗолото солнца здесь всегда живет."},
    {"name": "Канада", "description": "Клён на флаге, лёд и лес,\nЗдесь воздух полон, чист и свеж.\nХоккей — их гордость и игра,\nПрирода — главная звезда."},
    {"name": "Италия", "description": "Где пицца с сыром и томатами,\nГондолы плывут по каналам плавно,\nКолизей стоит, вековой и гордый,\nА музыка льется звонко и модно."},
    {"name": "Китай", "description": "Велика стена сквозь горы,\nЧай растёт в туманах зори.\nДракон хранит страну с небес,\nСтрана — загадок полон лес."},
    {"name": "Австралия", "description": "Кенгуру — весёлый друг,\nСкок за скоком — через луг.\nСидней плещет оперой,\nА риф пугает глубиной."},
    {"name": "Россия", "description": "Берёзы, песни и простор,\nОт Волги до Урала — взор.\nЗима снежком рисует путь,\nВ страну, что в сердце держит суть."},
]

class TurtleAdventure:
    def __init__(self, master):
        self.master = master
        self.master.title("Путешествие черепашонка")
        self.master.configure(bg="#d0f0c0")  # мягкий зелёный фон
        self.turtle_image = None
        self.img_label = None
        self.y_offset = 0
        self.direction = 1
        self.load_images()
        self.main_menu()

    def load_images(self):
        try:
            image = Image.open("turtle.png")
            image = image.resize((120, 120))
            self.turtle_image = ImageTk.PhotoImage(image)
        except Exception as e:
            print("Не удалось загрузить изображение черепашки:", e)
            self.turtle_image = None

    def animate_turtle(self):
        if self.img_label:
            self.y_offset += self.direction
            if abs(self.y_offset) > 10:
                self.direction *= -1
            self.img_label.place_configure(y=50 + self.y_offset)
            self.master.after(100, self.animate_turtle)

    def main_menu(self):
        self.clear_window()

        if self.turtle_image:
            self.img_label = tk.Label(self.master, image=self.turtle_image, bg="#d0f0c0")
            self.img_label.place(x=240, y=50)
            self.animate_turtle()

        title = tk.Label(self.master, text="Путешествие черепашонка", font=("Arial", 20, "bold"), bg="#d0f0c0", fg="#2a4d14")
        title.pack(pady=180)

        intro = tk.Label(
            self.master,
            wraplength=500,
            font=("Arial", 12),
            text="Главный герой, черепашонок, хочет отправиться в великое путешествие. Но у него перепутались карточки с описаниями стран! Помоги ему сопоставить описания с правильными странами.",
            bg="#d0f0c0"
        )
        intro.pack(pady=10)

        start_button = tk.Button(self.master, text="Начать игру", command=self.start_game, font=("Arial", 12), bg="#88c070", fg="white")
        start_button.pack(pady=20)

    def start_game(self):
        self.score = 0
        self.round = 0
        self.country_pool = random.sample(countries, len(countries))
        self.clear_window()

        if self.turtle_image:
            self.img_label = tk.Label(self.master, image=self.turtle_image, bg="#d0f0c0")
            self.img_label.pack(pady=5)

        self.label = tk.Label(self.master, text="Описание страны:", font=("Arial", 14, "bold"), bg="#d0f0c0")
        self.label.pack(pady=10)

        self.description_label = tk.Label(self.master, text="", wraplength=500, font=("Arial", 12), bg="#d0f0c0")
        self.description_label.pack(pady=10)

        self.entry = tk.Entry(self.master, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(self.master, text="Ответить", command=self.check_answer, bg="#88c070", fg="white", font=("Arial", 11))
        self.submit_button.pack(pady=10)

        self.status_label = tk.Label(self.master, text="", font=("Arial", 12), bg="#d0f0c0")
        self.status_label.pack(pady=5)

        self.poem_label = tk.Label(self.master, text="", wraplength=500, font=("Arial", 10, "italic"), fg="gray", bg="#d0f0c0")
        self.poem_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.round >= len(self.country_pool):
            self.end_game()
            return

        self.current = self.country_pool[self.round]
        self.description_label.config(text=self.current["description"])
        self.poem_label.config(text=self.current.get("poem", ""))
        self.entry.delete(0, tk.END)
        self.status_label.config(text="")
        self.round += 1

    def check_answer(self):
        user_answer = self.entry.get().strip().lower()
        correct_answer = self.current["name"].lower()
        if user_answer == correct_answer:
            self.score += 1
            self.status_label.config(text="Верно!", fg="green")
        else:
            self.status_label.config(text=f"Неверно. Это была: {self.current['name']}", fg="red")
        self.master.after(2000, self.next_question)

    def end_game(self):
        self.clear_window()

        if self.turtle_image:
            self.img_label = tk.Label(self.master, image=self.turtle_image, bg="#d0f0c0")
            self.img_label.place(x=240, y=50)
            self.animate_turtle()

        end_label = tk.Label(self.master, text="Спасибо за помощь, друг!", font=("Arial", 16, "bold"), bg="#d0f0c0", fg="#2a4d14")
        end_label.pack(pady=180)

        summary = tk.Label(self.master, text=f"Ты угадал {self.score} из {len(countries)} стран!", font=("Arial", 12), bg="#d0f0c0")
        summary.pack(pady=5)

        goodbye = tk.Label(self.master, text="Теперь черепашонок готов к своему великому путешествию!", font=("Arial", 12), bg="#d0f0c0")
        goodbye.pack(pady=10)

        exit_button = tk.Button(self.master, text="Выйти", command=self.master.quit, bg="#88c070", fg="white")
        exit_button.pack(pady=15)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")
    root.configure(bg="#d0f0c0")
    game = TurtleAdventure(root)
    root.mainloop()
