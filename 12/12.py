"""
Практическая работа 12
Получение данных пользователя
Задание: даны самые популярные репозитории на github 
https://habr.com/ru/post/453444/, по последней цифре зачетки получить JSON 
для вашего варианта (вариант 11 - dotnet/roslyn).

Программа с графическим интерфейсом вводим в поле имя репозитория и по 
нажатию кнопки получаем результат.

Необходимо получить в новый файл следующую информацию:
'company': None,
'created_at': '2015-08-03T17:55:43Z',
'email': None,
'id': 13629408,
'name': 'Kubernetes',
'url': 'https://api.github.com/users/kubernetes'
"""

import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

class GitHubRepoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Парсер репозитория")
        self.root.geometry("600x400")
        
        self.repo_data = None
        
        ttk.Label(root, text="GitHub Repository Information", font=("Arial", 14)).pack(pady=10)
        ttk.Label(root, text="Вариант 11: dotnet/roslyn", font=("Arial", 10)).pack()
        
        input_frame = ttk.Frame(root)
        input_frame.pack(pady=20)
        
        ttk.Label(input_frame, text="Имя репозитория:").grid(row=0, column=0, padx=5)
        self.repo_entry = ttk.Entry(input_frame, width=30)
        self.repo_entry.grid(row=0, column=1, padx=5)
        self.repo_entry.insert(0, "dotnet/roslyn")
        
        self.get_btn = ttk.Button(input_frame, text="Получить информацию", command=self.get_repo_info)
        self.get_btn.grid(row=0, column=2, padx=5)
        
        self.save_btn = ttk.Button(root, text="Сохранить в файл", command=self.save_to_file, state=tk.DISABLED)
        self.save_btn.pack(pady=10)
        
        self.result_text = tk.Text(root, height=10, width=70, font=("Courier", 9))
        self.result_text.pack(pady=10, padx=10)
        
        scrollbar = ttk.Scrollbar(root, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)
        
    def get_repo_info(self):
        repo_name = self.repo_entry.get().strip()
        
        if not repo_name:
            messagebox.showwarning("Ошибка", "Введите имя репозитория")
            return
            
        if '/' not in repo_name:
            messagebox.showwarning("Ошибка", "Формат: владелец/репозиторий")
            return
            
        try:
            self.get_btn.config(state=tk.DISABLED)
            url = f"https://api.github.com/repos/{repo_name}"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                
                owner_data = data.get('owner', {})
                
                self.repo_data = {
                    'company': owner_data.get('company'),
                    'created_at': data.get('created_at'),
                    'email': owner_data.get('email'),
                    'id': data.get('id'),
                    'name': data.get('name'),
                    'url': data.get('url')
                }
                
                formatted_json = json.dumps(self.repo_data, indent=2)
                
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, formatted_json)
                self.save_btn.config(state=tk.NORMAL)
                
            elif response.status_code == 404:
                messagebox.showerror("Ошибка", f"Репозиторий '{repo_name}' не найден")
            else:
                messagebox.showerror("Ошибка", f"Ошибка {response.status_code}")
                
        except requests.exceptions.RequestException:
            messagebox.showerror("Ошибка", "Ошибка сети")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка: {str(e)}")
        finally:
            self.get_btn.config(state=tk.NORMAL)
    
    def save_to_file(self):
        if not self.repo_data:
            messagebox.showwarning("Ошибка", "Нет данных для сохранения")
            return
            
        try:
            filename = "github_data.json"
            with open(filename, 'w') as f:
                json.dump(self.repo_data, f, indent=2)
            
            messagebox.showinfo("Успех", f"Данные сохранены в файл: {filename}")
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка сохранения: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GitHubRepoApp(root)
    root.mainloop()
