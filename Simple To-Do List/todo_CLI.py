import json
import os
from datetime import datetime

class TodoCLI:
    def __init__(self):
        self.data_file = "todo_CLI.json"
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    self.tasks = json.load(f)
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []
    
    def save_tasks(self):
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.tasks, f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, task_text):
        task = {
            'id': len(self.tasks) + 1,
            'text': task_text,
            'completed': False,
            'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Added task: '{task_text}'")
    
    def list_tasks(self):
        if not self.tasks:
            print("📋 No tasks found!")
            return
        
        print("\n📋 Your Tasks:")
        print("-" * 60)
        for i, task in enumerate(self.tasks):
            status = "✓" if task['completed'] else "○"
            print(f"{i+1:2d}. {status} {task['text']}")
            print(f"    Created: {task['created']}")
        
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task['completed'])
        pending = total - completed
        print("-" * 60)
        print(f"Total: {total} | Completed: {completed} | Pending: {pending}")
    
    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()
            print(f"✓ Completed: '{self.tasks[task_index]['text']}'")
        else:
            print("❌ Invalid task number!")
    
    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task_text = self.tasks[task_index]['text']
            del self.tasks[task_index]
            self.save_tasks()
            print(f"🗑 Deleted: '{task_text}'")
        else:
            print("❌ Invalid task number!")
    
    def clear_all(self):
        self.tasks.clear()
        self.save_tasks()
        print("🗑 All tasks cleared!")
    
    def show_menu(self):
        print("\n" + "="*50)
        print("📝 SIMPLE TO-DO LIST")
        print("="*50)
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Clear all tasks")
        print("6. Exit")
        print("-"*50)
    
    def run(self):
        while True:
            self.show_menu()
            try:
                choice = input("Choose an option (1-6): ").strip()
                
                if choice == '1':
                    task_text = input("Enter task: ").strip()
                    if task_text:
                        self.add_task(task_text)
                    else:
                        print("❌ Task cannot be empty!")
                
                elif choice == '2':
                    self.list_tasks()
                
                elif choice == '3':
                    self.list_tasks()
                    if self.tasks:
                        task_num = int(input("Enter task number to complete: ")) - 1
                        self.complete_task(task_num)
                
                elif choice == '4':
                    self.list_tasks()
                    if self.tasks:
                        task_num = int(input("Enter task number to delete: ")) - 1
                        self.delete_task(task_num)
                
                elif choice == '5':
                    confirm = input("Delete all tasks? (y/N): ").strip().lower()
                    if confirm == 'y':
                        self.clear_all()
                
                elif choice == '6':
                    print("👋 Goodbye!")
                    break
                
                else:
                    print("❌ Invalid choice! Please enter 1-6.")
                
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            
            input("\nPress Enter to continue...")

def main():
    todo = TodoCLI()
    todo.run()

if __name__ == "__main__":
    main()
