import tkinter as tk
from tkinter import messagebox, Tk
from PIL import Image, ImageTk
import random
import os

countries = [
    {"name": "Франция", "description": "Тут всегда пекут багеты,\nКруассаны — как конфеты.\nСто сортов сыров найдёшь —\nИ Лувр весь ты обойдёшь",
     "info": "Париж, столица Франции, считается культурной столицей \nмира и родиной таких великих творцов, как Виктор Гюго, \nКлод Моне и Мольер. Эйфелева башня, Лувр, Нотр-Дам \nи Версальский дворец стали символами не только Франции, \nно и всей европейской культуры. Кроме того, \nФранция считается родиной высокой моды: Париж проводит одни из \nсамых престижных показов мод в мире."},
    {"name": "Япония", "description": "Там сакура весной цветёт,\nИ Фудзи в облака встаёт.\nСуши, чай и иероглиф —\nВосточный мир — как стих без слов.",
     "info": "Это островное государство в Восточной Азии, \nсочетающее древние традиции с передовыми технологиями. \nЯпонская культура строится на принципах гармонии и самодисциплины, \nЛюбви к икэбана (аранжировка цветов), каллиграфии и театру кабуки. \nВ современной культуре Япония известна как родина аниме, \nманги и видеоигр."},
    {"name": "Бразилия", "description": "Карнавал и самба в ритме,\nСолнце пляшет в каждый бит.\nАмазонка — дух живой,\nСтрана уж в пляс идет с тобой.",
     "info": "Это самая большая страна в Южной Америке. Её культура \nсформировалась под влиянием коренных народов и португальских колонизаторов, \nчто проявляется в музыке, танцах, кухне и праздниках. \nОдной из главных культурных особенностей Бразилии является \nкарнавал — грандиозный фестиваль с пышными костюмами, яркими шествиями \nи зажигательной самбой."},
    {"name": "Египет", "description": "Пирамиды в горячих песках блестят,\nСфинкс загадки всем шепчет подряд,\nРека большая жизнь несет,\nЗолото солнца здесь всегда живет.",
     "info": "Страна с одной из древнейших цивилизаций в мире. Её история \nнасчитывает тысячи лет, оставив богатое наследие в виде пирамид, \nхрамов и уникальных археологических памятников. Египетская культура \nглубоко связана с религиозными традициями и мифологией, \nчто отражается в искусстве, архитектуре"},
    {"name": "Канада", "description": "Клён на флаге, лёд и лес,\nЗдесь воздух полон, чист и свеж.\nХоккей — их гордость и игра,\nПрирода — главная звезда.",
     "info": "Многонациональная страна с богатым культурным наследием, \nсочетающая традиции коренных народов, французских и английских колонизаторов, \nа также иммигрантов со всего мира. В культуре Канады ценятся \nтолерантность, уважение к природе и зимним видам спорта"},
    {"name": "Италия", "description": "Где пицца с сыром и томатами,\nГондолы плывут по каналам плавно,\nКолизей стоит, вековой и гордый,\nА музыка льется звонко и модно.",
     "info": "Это колыбель искусства, архитектуры и кулинарии. \nИтальянская культура ценит семейные традиции, наслаждение жизнью и \nтворческое выражение. Важное место занимает знаменитая \nитальянская кухня с пастой, пиццей и вином."},
    {"name": "Китай", "description": "Велика стена сквозь горы,\nЧай растёт в туманах зори.\nДракон хранит страну с небес,\nСтрана — загадок полон лес.",
     "info": "Одна из древнейших цивилизаций мира с богатой культурой, \nоснованной на философии Конфуция, буддизме и даосизме. \nВажное место занимают традиции уважения к семье, гармонии и коллективизма. \nКитайская культура славится искусством каллиграфии, традиционной музыкой, \nа также разнообразной кухней, в которой блюда заряжены энергетикой инь-ян."},
    {"name": "Австралия", "description": "Кенгуру — весёлый друг,\nСкок за скоком — через луг.\nСидней плещет оперой,\nА риф пугает глубиной.",
     "info": "Страна с уникальным культурным многообразием, \nгде сочетаются традиции коренных аборигенов и влияние европейских поселенцев. \nВ культуре важны уважение к природе, активный образ жизни и спортивные традиции. \nАвстралийская музыка, искусство и праздники отражают это смешение, \nа также открытость и дружелюбие её жителей."},
]

W_WIDTH = 600
W_HEIGHT = 600
BG_COLOR = "#d0f0c0"
BUT_BG = "#88c070"
BUT_FG = "white"
FONT_TITLE = ("Arial", 20, "bold")
FONT_TEXT = ("Arial", 12)
FONT_LABEL_B = ("Arial", 14, "bold")
FONT_ITALIC = ("Arial", 10, "italic")
MIN_TO_WIN = 7

class TurtleAdventure:
    def __init__(self, master):
        self.master = master
        self.master.title("Путешествие черепашонка")
        self.master.geometry(f"{W_WIDTH}x{W_HEIGHT}")
        self.master.configure(bg=BG_COLOR)
        self.turtle_image = None
        self.turtle_happy_image = None
        self.turtle_very_happy_image = None
        self.turtle_loose_image = None
        self.turtle_win_image = None
        self.img_label = None
        self.load_images()
        self.main_menu()

        if self.turtle_image:
            self.img_label = tk.Label(master, image=self.turtle_image, bg=BG_COLOR)
            self.img_label.pack()

    def load_images(self):
        try:
            image = Image.open("C:\\Users\\hochy\\OneDrive\\Desktop\\итоговый п\\Turt_think.png")
            image = image.resize((120, 120))
            self.turtle_image = ImageTk.PhotoImage(image)
            happy_image = Image.open("C:\\Users\\hochy\\OneDrive\\Desktop\\итоговый п\\Turt_happy.png")
            happy_image = happy_image.resize((150, 150))
            self.turtle_happy_image = ImageTk.PhotoImage(happy_image)
            very_happy_image = Image.open("C:\\Users\\hochy\\OneDrive\\Desktop\\итоговый п\\Turt_happy2.png")
            very_happy_image = very_happy_image.resize((150, 150))
            self.turtle_very_happy_image = ImageTk.PhotoImage(very_happy_image)
            loose_image = Image.open("C:\\Users\\hochy\\OneDrive\\Desktop\\итоговый п\\turt_sad.png")
            loose_image = loose_image.resize((200, 200))
            self.turtle_loose_image = ImageTk.PhotoImage(loose_image)
            win_image = Image.open("C:\\Users\\hochy\\OneDrive\\Desktop\\итоговый п\\turt_win.png")
            win_image = win_image.resize((200, 200))
            self.turtle_win_image = ImageTk.PhotoImage(win_image)
        except FileNotFoundError:
            print("Файл не найден")

    def main_menu(self):
        self.clear_window()

        if self.turtle_image:
            self.img_label = tk.Label(self.master, image=self.turtle_image, bg=BG_COLOR)
            self.img_label.place(x=240, y=132)

        title = tk.Label(self.master, text="ПУТЕШЕСТВИЕ ЧЕРЕПАШОНКА", font=FONT_TITLE, bg=BG_COLOR, fg="#2a4d14")
        title.pack(pady=100)

        intro = tk.Label(
            self.master,
            wraplength=500,
             font=FONT_TEXT,
            text="Маленький черепашонок собрался в большое путешествие! Он уже собрал вещи, надел шляпку, взял в лапы карту... и понял, что забыл самое главное – он не составил маршрут! Помоги черепашонку продумать путь, чтобы он не заблудился.",
            bg=BG_COLOR
        )
        intro.pack(pady=10)

        start_button = tk.Button(self.master, text="Начать игру", command=self.start_game, font=FONT_TEXT, bg=BUT_BG, fg=BUT_FG)
        start_button.pack(pady=20)

    def start_game(self):
        self.score = 0
        self.round = 0
        self.country_pool = random.sample(countries, len(countries))
        self.clear_window()

        if self.turtle_happy_image:
            self.img_label = tk.Label(self.master, image=self.turtle_happy_image, bg=BG_COLOR)
            self.img_label.pack(pady=5)

        self.label = tk.Label(self.master, text="Описание страны:", font=FONT_LABEL_B, bg=BG_COLOR)
        self.label.pack(pady=10)

        self.description_label = tk.Label(self.master, text="", wraplength=500, font=FONT_TEXT, bg=BG_COLOR)
        self.description_label.pack(pady=10)

        self.entry = tk.Entry(self.master, font=FONT_TEXT)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(self.master, text="Ответить", command=self.check_answer, bg=BUT_BG, fg=BUT_FG, font=("Arial", 11))
        self.submit_button.pack(pady=10)

        self.status_label = tk.Label(self.master, text="", font=FONT_TEXT, bg=BG_COLOR)
        self.status_label.pack(pady=5)

        self.next_question()

    def next_question(self):
        if self.round >= len(self.country_pool):
            self.end_game()
            return

        self.current = self.country_pool[self.round]
        self.description_label.config(text=self.current["description"])
        self.entry.delete(0, tk.END)
        self.status_label.config(text="")
        self.round += 1

        if self.img_label and self.turtle_happy_image:
            self.img_label.config(image=self.turtle_happy_image)

    def check_answer(self):
        user_answer = self.entry.get().strip().lower()
        if not user_answer:
            messagebox.showwarning("Ошибка!", "Введите название страны.")
            return
        correct_answer = self.current["name"].lower()
        if user_answer == correct_answer:
            self.score += 1
            self.status_label.config(text=f"Верно! {self.current["info"]}", fg="green")
            self.master.after(10000, self.next_question)
            self.show_very_happy_image_temporarily()
        else:
            self.status_label.config(text=f"Неверно. Загаданная страна: {self.current["name"]}", fg="red")
            self.master.after(2000, self.next_question)

    def show_very_happy_image_temporarily(self):
        if not self.img_label or not self.turtle_very_happy_image:
            return
        self.img_label.config(image=self.turtle_very_happy_image)
        self.master.after(10000, lambda: self.img_label.config(image=self.turtle_happy_image))

    def end_game(self):
        self.clear_window()

        if self.score > 6:
            if self.turtle_win_image:
                img_label = tk.Label(self.master, image=self.turtle_win_image, bg="#d0f0c0")
                img_label.pack(pady=10)
            end_text = "Спасибо за помощь, друг! \nБез тебя я бы никогда не справился."
            end_color = "#2a4d14"
            goodbye_text = "Теперь черепашонок готов к своему великому путешествию! \nКто знает, может, он и к тебе в гости зайдет?"
        else:
            if self.turtle_loose_image:
                img_label = tk.Label(self.master, image=self.turtle_loose_image, bg="#d0f0c0")
                img_label.pack(pady=10)
            end_text = f"Проигрыш!"
            end_color = "red"
            goodbye_text = "Не унывай! Попробуй снова и у тебя обязательно получится."

        end_label = tk.Label(self.master, text=end_text, font=("Arial", 16, "bold"), bg=BG_COLOR, fg=end_color)
        end_label.pack(pady=20)

        summary = tk.Label(self.master, text=f"Ты угадал {self.score} из {len(countries)} стран!", font=FONT_TEXT, bg=BG_COLOR)
        summary.pack(pady=5)

        goodbye = tk.Label(self.master, text=goodbye_text, font=FONT_TEXT, bg=BG_COLOR)
        goodbye.pack(pady=10)

        restart_button = tk.Button(self.master, text="Начать заново", command=self.start_game, bg=BUT_BG, fg=BUT_FG, width=12)
        restart_button.pack(pady=5)
        exit_button = tk.Button(self.master, text="Выйти", command=self.master.quit, bg=BUT_BG, fg=BUT_FG, width=12)
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