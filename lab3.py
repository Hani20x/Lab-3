import tkinter as tk
from tkinter import messagebox
import random
import pygame
from PIL import Image, ImageTk

# Инициализация pygame для музыки
pygame.mixer.init()

# Функция для генерации ключа
def generate_key():
    dec_number = entry.get()
    if len(dec_number) != 6 or not dec_number.isdigit():
        messagebox.showerror("Ошибка", "Введите 6-значное DEC-число")
        return
    
    # Разделение числа на части
    part1 = dec_number[3:6]  # 4,5,6 цифры
    part2 = dec_number[0:3]  # 1,2,3 цифры
    
    # Генерация случайных букв для блоков
    def random_letters(length):
        return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))
    
    block1 = part1 + random_letters(2)
    block2 = part2 + random_letters(2)
    
    # Сложение чисел из блоков 1 и 2
    sum_blocks = str(int(part1) + int(part2)).zfill(4)
    
    # Формирование итогового ключа
    key = f"{block1}-{block2}-{sum_blocks}"
    key_label.config(text=key)

# Функция для воспроизведения музыки
def play_music():
    pygame.mixer.music.load("8bit_music.mp3")
    pygame.mixer.music.play(-1)  # -1 для бесконечного воспроизведения

# Создание основного окна
root = tk.Tk()
root.title("Keygen Generator")
root.geometry("600x400")

# Загрузка фонового изображения с помощью Pillow
try:
    image = Image.open("background.jpg")
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)
except Exception as e:
    print(f"Ошибка загрузки изображения: {e}")
    # Если изображение не загружено, используем белый фон
    background_label = tk.Label(root, bg="white")
    background_label.place(relwidth=1, relheight=1)

# Поле для ввода DEC-числа
entry_label = tk.Label(root, text="Введите 6-значное DEC-число:", bg="white")
entry_label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

# Кнопка для генерации ключа
generate_button = tk.Button(root, text="Сгенерировать ключ", command=generate_key, bg="lightblue")
generate_button.pack(pady=10)

# Поле для вывода ключа
key_label = tk.Label(root, text="", bg="white", font=("Arial", 14))
key_label.pack(pady=20)

# Анимация (движущийся текст)
animation_label = tk.Label(root, text="Keygen Generator", bg="white", font=("Arial", 16))
animation_label.pack(pady=20)

def move_text():
    x, y = animation_label.winfo_x(), animation_label.winfo_y()
    if x > root.winfo_width():
        x = -200
    else:
        x += 5
    animation_label.place(x=x, y=y)
    root.after(50, move_text)

move_text()

# Воспроизведение музыки
play_music()

# Запуск основного цикла
root.mainloop()