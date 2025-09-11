import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple To-Do List")
        self.root.geometry("500x600")
        self.root.configure(bg='#f0f0f0')
        
        self.tasks = []
        self.data_file = "todo_GUI.json"
        
        self.load_tasks()
        self.setup_ui()
    
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = ttk.Label(main_frame, text="📝 Simple To-Do List", font=("Arial", 20, "bold"))
        title_label.pack(pady=(0, 20))
        
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.task_entry = ttk.Entry(input_frame, font=("Arial", 12), width=35)
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.task_entry.bind('<Return>', lambda e: self.add_task())
        
        add_btn = ttk.Button(input_frame, text="Add Task", command=self.add_task)
        add_btn.pack(side=tk.RIGHT)
        
        list_frame = ttk.LabelFrame(main_frame, text="Tasks", padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, 
                                      font=("Arial", 11), selectmode=tk.SINGLE,
                                      height=15)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_listbox.yview)
        
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X)
        
        complete_btn = ttk.Button(button_frame, text="✓ Complete", command=self.complete_task)
        complete_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        delete_btn = ttk.Button(button_frame, text="🗑 Delete", command=self.delete_task)
        delete_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_btn = ttk.Button(button_frame, text="Clear All", command=self.clear_all_tasks)
        clear_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        stats_label = ttk.Label(main_frame, text="", font=("Arial", 10))
        stats_label.pack(pady=(10, 0))
        self.stats_label = stats_label
        
        self.update_display()
    
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            task = {
                'text': task_text,
                'completed': False,
                'created': datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.update_display()
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    
    def complete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]['completed'] = True
            self.update_display()
            self.save_tasks()
        else:
            messagebox.showinfo("Info", "Please select a task to complete!")
    
    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            task_text = self.tasks[index]['text']
            if messagebox.askyesno("Confirm", f"Delete task: '{task_text}'?"):
                del self.tasks[index]
                self.update_display()
                self.save_tasks()
        else:
            messagebox.showinfo("Info", "Please select a task to delete!")
    
    def clear_all_tasks(self):
        if self.tasks and messagebox.askyesno("Confirm", "Delete all tasks?"):
            self.tasks.clear()
            self.update_display()
            self.save_tasks()
    
    def update_display(self):
        self.task_listbox.delete(0, tk.END)
        
        for i, task in enumerate(self.tasks):
            status = "✓" if task['completed'] else "○"
            display_text = f"{status} {task['text']} ({task['created']})"
            self.task_listbox.insert(tk.END, display_text)
            
            if task['completed']:
                self.task_listbox.itemconfig(i, {'fg': 'green'})
        
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task['completed'])
        pending_tasks = total_tasks - completed_tasks
        
        stats_text = f"Total: {total_tasks} | Completed: {completed_tasks} | Pending: {pending_tasks}"
        self.stats_label.config(text=stats_text)
    
    def save_tasks(self):
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.tasks, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks: {str(e)}")
    
    def load_tasks(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    self.tasks = json.load(f)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load tasks: {str(e)}")
            self.tasks = []

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
