import datetime
import time
import threading
import winsound

class AlarmClock:
    def __init__(self):
        self.alarms = []
        self.running = True
    
    def add_alarm(self, alarm_time, message="Alarm!"):
        self.alarms.append({
            'time': alarm_time,
            'message': message,
            'active': True
        })
        print(f"Alarm set for {alarm_time.strftime('%H:%M:%S')} - {message}")
    
    def remove_alarm(self, index):
        if 0 <= index < len(self.alarms):
            removed = self.alarms.pop(index)
            print(f"Removed alarm: {removed['time'].strftime('%H:%M:%S')}")
        else:
            print("Invalid alarm index")
    
    def list_alarms(self):
        if not self.alarms:
            print("No alarms set")
            return
        
        print("Current alarms:")
        for i, alarm in enumerate(self.alarms):
            status = "Active" if alarm['active'] else "Inactive"
            print(f"{i+1}. {alarm['time'].strftime('%H:%M:%S')} - {alarm['message']} ({status})")
    
    def check_alarms(self):
        current_time = datetime.datetime.now().time()
        for alarm in self.alarms[:]:
            if alarm['active'] and self.time_matches(current_time, alarm['time'].time()):
                self.trigger_alarm(alarm)
                self.alarms.remove(alarm)
    
    def time_matches(self, current, alarm):
        return (current.hour == alarm.hour and 
                current.minute == alarm.minute and 
                current.second == alarm.second)
    
    def trigger_alarm(self, alarm):
        print(f"\n{'='*50}")
        print(f"ALARM! {alarm['message']}")
        print(f"Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
        print(f"{'='*50}")
        
        for _ in range(5):
            try:
                winsound.Beep(1000, 500)
                time.sleep(0.2)
            except:
                print("BEEP! BEEP! BEEP!")
                time.sleep(0.5)
    
    def run(self):
        def alarm_thread():
            while self.running:
                self.check_alarms()
                time.sleep(1)
        
        thread = threading.Thread(target=alarm_thread)
        thread.daemon = True
        thread.start()
        
        self.show_menu()
    
    def show_menu(self):
        while self.running:
            print(f"\nCurrent time: {datetime.datetime.now().strftime('%H:%M:%S')}")
            print("\nAlarm Clock Menu:")
            print("1. Set new alarm")
            print("2. List alarms")
            print("3. Remove alarm")
            print("4. Exit")
            
            choice = input("Choose an option (1-4): ").strip()
            
            if choice == '1':
                self.set_alarm_interactive()
            elif choice == '2':
                self.list_alarms()
            elif choice == '3':
                self.remove_alarm_interactive()
            elif choice == '4':
                self.running = False
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def set_alarm_interactive(self):
        try:
            time_str = input("Enter alarm time (HH:MM:SS or HH:MM): ").strip()
            message = input("Enter alarm message (optional): ").strip() or "Alarm!"
            
            if len(time_str.split(':')) == 2:
                time_str += ":00"
            
            alarm_time = datetime.datetime.strptime(time_str, '%H:%M:%S')
            
            today = datetime.date.today()
            alarm_datetime = datetime.datetime.combine(today, alarm_time.time())
            
            if alarm_datetime <= datetime.datetime.now():
                alarm_datetime += datetime.timedelta(days=1)
                print("Alarm set for tomorrow (time has passed today)")
            
            self.add_alarm(alarm_datetime, message)
            
        except ValueError:
            print("Invalid time format. Please use HH:MM:SS or HH:MM")
    
    def remove_alarm_interactive(self):
        if not self.alarms:
            print("No alarms to remove")
            return
        
        self.list_alarms()
        try:
            index = int(input("Enter alarm number to remove: ")) - 1
            self.remove_alarm(index)
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    alarm_clock = AlarmClock()
    print("Welcome to Simple Alarm Clock!")
    print("You can set multiple alarms and get notified when they go off.")
    alarm_clock.run()
