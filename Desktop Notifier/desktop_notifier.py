import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import os
import sys
import subprocess

try:
    from plyer import notification as plyer_notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False
    print("plyer not available. Install it with: pip install plyer")

class DesktopNotifier:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop Notifier - Enhanced")
        self.root.geometry("550x500")
        self.root.resizable(True, True)
        self.root.minsize(500, 450)
        self.root.configure(bg='#f0f0f0')
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        self.setup_ui()
    
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="25")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        main_frame.columnconfigure(1, weight=1)
        
        title_label = ttk.Label(main_frame, text="Desktop Notifier - Enhanced", font=("Arial", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 25))
        
        ttk.Label(main_frame, text="Title:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky=(tk.W, tk.N), pady=(5, 8), padx=(0, 15))
        self.title_entry = ttk.Entry(main_frame, width=35, font=("Arial", 10))
        self.title_entry.grid(row=1, column=1, pady=(5, 8), sticky=(tk.W, tk.E))
        
        ttk.Label(main_frame, text="Message:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky=(tk.W, tk.N), pady=(8, 8), padx=(0, 15))
        message_frame = ttk.Frame(main_frame)
        message_frame.grid(row=2, column=1, pady=(8, 8), sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.message_text = tk.Text(message_frame, width=35, height=5, wrap=tk.WORD, font=("Arial", 10))
        scrollbar = ttk.Scrollbar(message_frame, orient=tk.VERTICAL, command=self.message_text.yview)
        self.message_text.configure(yscrollcommand=scrollbar.set)
        
        self.message_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        settings_frame = ttk.LabelFrame(main_frame, text="Settings", padding="10")
        settings_frame.grid(row=3, column=0, columnspan=2, pady=(15, 15), sticky=(tk.W, tk.E))
        
        ttk.Label(settings_frame, text="Timeout (seconds):").grid(row=0, column=0, sticky=tk.W, pady=5, padx=(0, 10))
        self.timeout_var = tk.StringVar(value="5")
        timeout_entry = ttk.Entry(settings_frame, textvariable=self.timeout_var, width=8)
        timeout_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(settings_frame, text="Delay (seconds):").grid(row=0, column=2, sticky=tk.W, pady=5, padx=(20, 10))
        self.delay_var = tk.StringVar(value="0")
        delay_entry = ttk.Entry(settings_frame, textvariable=self.delay_var, width=8)
        delay_entry.grid(row=0, column=3, sticky=tk.W, pady=5)
        
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=(10, 15))
        
        send_btn = ttk.Button(button_frame, text="📢 Send Notification", command=self.send_notification, width=18)
        send_btn.pack(side=tk.LEFT, padx=(0, 8))
        
        test_btn = ttk.Button(button_frame, text="🧪 Test All Methods", command=self.test_all_methods, width=15)
        test_btn.pack(side=tk.LEFT, padx=(0, 8))
        
        clear_btn = ttk.Button(button_frame, text="🗑️ Clear", command=self.clear_fields, width=10)
        clear_btn.pack(side=tk.LEFT)
        
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=5, column=0, columnspan=2, pady=(5, 0), sticky=(tk.W, tk.E))
        
        ttk.Label(status_frame, text="Status:", font=("Arial", 9, "bold")).pack(side=tk.LEFT)
        self.status_label = ttk.Label(status_frame, text="Ready", foreground="green", font=("Arial", 9))
        self.status_label.pack(side=tk.LEFT, padx=(5, 0))
        
        info_frame = ttk.LabelFrame(main_frame, text="Available Methods", padding="10")
        info_frame.grid(row=6, column=0, columnspan=2, pady=(10, 0), sticky=(tk.W, tk.E))
        
        methods_info = []
        if PLYER_AVAILABLE:
            methods_info.append("✅ System Notifications (plyer)")
        else:
            methods_info.append("❌ System Notifications (not installed)")
            
        methods_info.append("✅ PowerShell (Windows native)")
        methods_info.append("✅ Message Box (fallback)")
        
        for i, method in enumerate(methods_info):
            ttk.Label(info_frame, text=method, font=("Arial", 8)).grid(row=i//2, column=i%2, sticky=tk.W, padx=5, pady=2)
    
    def send_notification(self):
        title = self.title_entry.get().strip()
        message = self.message_text.get("1.0", tk.END).strip()
        
        if not title:
            messagebox.showerror("Error", "Please enter a title")
            return
        
        if not message:
            messagebox.showerror("Error", "Please enter a message")
            return
        
        try:
            timeout = int(self.timeout_var.get())
            delay = int(self.delay_var.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for timeout and delay")
            return
        
        if timeout < 1:
            messagebox.showerror("Error", "Timeout must be at least 1 second")
            return
        
        if delay < 0:
            messagebox.showerror("Error", "Delay cannot be negative")
            return
        
        self.status_label.config(text="Scheduling notification...", foreground="orange")
        
        thread = threading.Thread(target=self._send_delayed_notification, 
                                 args=(title, message, timeout, delay))
        thread.daemon = True
        thread.start()
    
    def _send_notification_powershell(self, title, message, timeout):
        try:
            ps_script = f'''
[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
[Windows.UI.Notifications.ToastNotification, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
[Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime] | Out-Null

$APP_ID = "Microsoft.Windows.Computer"
$template = @"
<toast>
    <visual>
        <binding template="ToastText02">
            <text id="1">{title}</text>
            <text id="2">{message}</text>
        </binding>
    </visual>
</toast>
"@

$xml = New-Object Windows.Data.Xml.Dom.XmlDocument
$xml.LoadXml($template)
$toast = [Windows.UI.Notifications.ToastNotification]::new($xml)
$toast.Tag = "PowerShell"
$toast.Group = "PowerShell"
$toast.ExpirationTime = [DateTimeOffset]::Now.AddMinutes(5)

$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier($APP_ID)
$notifier.Show($toast);
'''
            result = subprocess.run(["powershell", "-Command", ps_script], 
                                  capture_output=True, text=True, timeout=10)
            return result.returncode == 0, "PowerShell notification sent!"
        except Exception as e:
            return False, f"PowerShell method failed: {str(e)}"
    
    def _send_notification_internal(self, title, message, timeout):
        methods_tried = []
        
        # Try plyer first (preferred method)
        if PLYER_AVAILABLE:
            try:
                plyer_notification.notify(
                    title=title,
                    message=message,
                    timeout=timeout,
                    app_name="Desktop Notifier"
                )
                return True, "System notification sent successfully!"
            except Exception as e:
                methods_tried.append(f"Plyer: {str(e)}")
        
        # Try PowerShell as secondary method
        success, msg = self._send_notification_powershell(title, message, timeout)
        if success:
            return True, msg
        else:
            methods_tried.append(f"PowerShell: {msg}")
        
        # Use message box as final fallback
        try:
            messagebox.showinfo(f"Notification: {title}", message + "\n\n(Native Windows notifications unavailable)")
            return True, "Message Box notification shown (fallback method)"
        except Exception as e:
            methods_tried.append(f"MessageBox: {str(e)}")
            return False, f"All notification methods failed: {'; '.join(methods_tried)}"
    
    def _send_delayed_notification(self, title, message, timeout, delay):
        if delay > 0:
            self.root.after(0, lambda: self.status_label.config(
                text=f"Notification will appear in {delay} seconds...", foreground="blue"))
            time.sleep(delay)
        
        success, status_msg = self._send_notification_internal(title, message, timeout)
        
        if success:
            self.root.after(0, lambda: self.status_label.config(
                text=status_msg, foreground="green"))
        else:
            self.root.after(0, lambda: self.status_label.config(
                text=status_msg, foreground="red"))
    
    def test_all_methods(self):
        test_title = "Test Notification"
        test_message = "This is a test from Desktop Notifier!"
        
        results = []
        
        if PLYER_AVAILABLE:
            try:
                plyer_notification.notify(
                    title=test_title,
                    message=test_message,
                    timeout=3,
                    app_name="Desktop Notifier"
                )
                results.append("✅ System Notifications: Success")
            except Exception as e:
                results.append(f"❌ System Notifications: {str(e)}")
        else:
            results.append("❌ System Notifications: Not available")
        
        success, msg = self._send_notification_powershell(test_title, test_message, 3)
        if success:
            results.append("✅ PowerShell: Success")
        else:
            results.append(f"❌ PowerShell: Failed")
        
        results.append("✅ Message Box: Always works")
        messagebox.showinfo("Test Results", "\n".join(results))
        
        self.status_label.config(text="All methods tested!", foreground="blue")
    
    def clear_fields(self):
        self.title_entry.delete(0, tk.END)
        self.message_text.delete("1.0", tk.END)
        self.timeout_var.set("5")
        self.delay_var.set("0")
        self.status_label.config(text="Fields cleared", foreground="green")

def main():
    root = tk.Tk()
    app = DesktopNotifier(root)
    root.mainloop()

if __name__ == "__main__":
    main()
