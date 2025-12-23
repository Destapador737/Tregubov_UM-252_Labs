import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Menu

# Создаем главное окно
root = tk.Tk()
root.title("ТрегубовВО_УМ252 - GUI приложение")  
root.geometry("800x600")
root.resizable(True, True)

# Создаем вкладки
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True, padx=10, pady=10)

# ========== ВКЛАДКА 1: КАЛЬКУЛЯТОР ==========
calc_frame = ttk.Frame(notebook)
notebook.add(calc_frame, text="Калькулятор")

# Метка заголовка
ttk.Label(calc_frame, text="Простой калькулятор", font=('Arial', 14, 'bold')).pack(pady=10)

# Фрейм для ввода чисел
input_frame = ttk.Frame(calc_frame)
input_frame.pack(pady=20)

# Первое число
ttk.Label(input_frame, text="Первое число:").grid(row=0, column=0, padx=5, pady=5)
num1_entry = ttk.Entry(input_frame, width=15)
num1_entry.grid(row=0, column=1, padx=5, pady=5)

# Оператор
ttk.Label(input_frame, text="Операция:").grid(row=1, column=0, padx=5, pady=5)
operator_var = tk.StringVar(value="+")
operator_combo = ttk.Combobox(input_frame, textvariable=operator_var, width=12, state="readonly")
operator_combo['values'] = ("+", "-", "*", "/")
operator_combo.grid(row=1, column=1, padx=5, pady=5)

# Второе число
ttk.Label(input_frame, text="Второе число:").grid(row=2, column=0, padx=5, pady=5)
num2_entry = ttk.Entry(input_frame, width=15)
num2_entry.grid(row=2, column=1, padx=5, pady=5)

# Функция вычисления
def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operator = operator_var.get()
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                result_label.config(text="Ошибка: деление на ноль!", foreground="red")
                return
            result = num1 / num2
        else:
            result_label.config(text="Ошибка: неизвестная операция!", foreground="red")
            return
        
        result_label.config(text=f"Результат: {result}", foreground="green")
    except ValueError:
        result_label.config(text="Ошибка: введите числа!", foreground="red")
    except Exception as e:
        result_label.config(text=f"Ошибка: {str(e)}", foreground="red")

# Кнопка вычисления
calc_button = ttk.Button(calc_frame, text="Вычислить", command=calculate)
calc_button.pack(pady=10)

# Метка для результата
result_label = ttk.Label(calc_frame, text="Результат: ", font=('Arial', 12))
result_label.pack(pady=10)

# ========== ВКЛАДКА 2: ЧЕКБОКСЫ ==========
checkbox_frame = ttk.Frame(notebook)
notebook.add(checkbox_frame, text="Чекбоксы")

# Метка заголовка
ttk.Label(checkbox_frame, text="Выберите вариант", font=('Arial', 14, 'bold')).pack(pady=20)

# Переменные для чекбоксов
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

# Создаем чекбоксы
cb1 = ttk.Checkbutton(checkbox_frame, text="Первый", variable=var1)
cb1.pack(pady=5)

cb2 = ttk.Checkbutton(checkbox_frame, text="Второй", variable=var2)
cb2.pack(pady=5)

cb3 = ttk.Checkbutton(checkbox_frame, text="Третий", variable=var3)
cb3.pack(pady=5)

# Функция обработки выбора
def show_selection():
    selected = []
    if var1.get():
        selected.append("Первый")
    if var2.get():
        selected.append("Второй")
    if var3.get():
        selected.append("Третий")
    
    if selected:
        message = f"Вы выбрали: {', '.join(selected)}"
        messagebox.showinfo("Выбор", message)
    else:
        messagebox.showwarning("Выбор", "Вы ничего не выбрали!")

# Кнопка подтверждения выбора
select_button = ttk.Button(checkbox_frame, text="Подтвердить выбор", command=show_selection)
select_button.pack(pady=20)

# ========== ВКЛАДКА 3: РАБОТА С ТЕКСТОМ ==========
text_frame = ttk.Frame(notebook)
notebook.add(text_frame, text="Текст")

# Создаем меню
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Меню "Файл"
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)

# Текстовое поле с прокруткой
text_frame_inner = ttk.Frame(text_frame)
text_frame_inner.pack(fill='both', expand=True, padx=10, pady=10)

text_scroll = ttk.Scrollbar(text_frame_inner)
text_scroll.pack(side='right', fill='y')

text_widget = tk.Text(text_frame_inner, height=20, width=70, yscrollcommand=text_scroll.set)
text_widget.pack(side='left', fill='both', expand=True)
text_scroll.config(command=text_widget.yview)

# Метка статуса
status_label = ttk.Label(text_frame, text="Текст не загружен", relief='sunken', anchor='w')
status_label.pack(fill='x', padx=10, pady=5)

# Функция загрузки файла
def load_file():
    file_path = filedialog.askopenfilename(
        title="Выберите текстовый файл",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                text_widget.delete('1.0', tk.END)  # Очищаем текстовое поле
                text_widget.insert('1.0', content)  # Вставляем содержимое файла
                status_label.config(text=f"Загружен файл: {file_path}")
                messagebox.showinfo("Успех", f"Файл успешно загружен!\nПуть: {file_path}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить файл:\n{str(e)}")

# Функция сохранения файла
def save_file():
    file_path = filedialog.asksaveasfilename(
        title="Сохранить файл",
        defaultextension=".txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    
    if file_path:
        try:
            content = text_widget.get('1.0', tk.END)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            status_label.config(text=f"Сохранен файл: {file_path}")
            messagebox.showinfo("Успех", f"Файл успешно сохранен!\nПуть: {file_path}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{str(e)}")

# Функция очистки текста
def clear_text():
    text_widget.delete('1.0', tk.END)
    status_label.config(text="Текст очищен")

# Добавляем пункты в меню "Файл"
file_menu.add_command(label="Открыть", command=load_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Очистить", command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)

# Панель кнопок в третьей вкладке
button_frame = ttk.Frame(text_frame)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Загрузить из файла", command=load_file).pack(side='left', padx=5)
ttk.Button(button_frame, text="Сохранить в файл", command=save_file).pack(side='left', padx=5)
ttk.Button(button_frame, text="Очистить текст", command=clear_text).pack(side='left', padx=5)

# Информация о программе
info_frame = ttk.Frame(root)
info_frame.pack(fill='x', pady=5)

ttk.Label(info_frame, text="Приложение создано Ивановым Иваном Ивановичем", 
          font=('Arial', 8)).pack(side='left', padx=10)
ttk.Label(info_frame, text="Практическая работа 11: GUI", 
          font=('Arial', 8)).pack(side='right', padx=10)

# Запуск главного цикла
root.mainloop()

