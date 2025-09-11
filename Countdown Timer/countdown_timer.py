import datetime
import time
import threading
import winsound
import os

class CountdownTimer:
    def __init__(self):
        self.timers = []
        self.running = True
    
    def add_timer(self, target_time, name="Timer"):
        timer = {
            'target_time': target_time,
            'name': name,
            'active': True,
            'created_at': datetime.datetime.now()
        }
        self.timers.append(timer)
        print(f"Timer '{name}' set for {target_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def add_duration_timer(self, hours, minutes, seconds, name="Timer"):
        now = datetime.datetime.now()
        target_time = now + datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
        self.add_timer(target_time, name)
    
    def remove_timer(self, index):
        if 0 <= index < len(self.timers):
            removed = self.timers.pop(index)
            print(f"Removed timer: {removed['name']}")
        else:
            print("Invalid timer index")
    
    def list_timers(self):
        if not self.timers:
            print("No active timers")
            return
        
        print("\nActive timers:")
        for i, timer in enumerate(self.timers):
            remaining = self.get_time_remaining(timer['target_time'])
            if remaining['total_seconds'] > 0:
                print(f"{i+1}. {timer['name']} - {self.format_time_remaining(remaining)}")
            else:
                print(f"{i+1}. {timer['name']} - EXPIRED")
    
    def get_time_remaining(self, target_time):
        now = datetime.datetime.now()
        remaining = target_time - now
        total_seconds = remaining.total_seconds()
        
        if total_seconds <= 0:
            return {'total_seconds': 0, 'hours': 0, 'minutes': 0, 'seconds': 0}
        
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        
        return {
            'total_seconds': total_seconds,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }
    
    def format_time_remaining(self, time_dict):
        h = time_dict['hours']
        m = time_dict['minutes']
        s = time_dict['seconds']
        
        if h > 0:
            return f"{h:02d}:{m:02d}:{s:02d}"
        else:
            return f"{m:02d}:{s:02d}"
    
    def check_timers(self):
        for timer in self.timers[:]:
            if timer['active']:
                remaining = self.get_time_remaining(timer['target_time'])
                if remaining['total_seconds'] <= 0:
                    self.trigger_timer(timer)
                    self.timers.remove(timer)
    
    def trigger_timer(self, timer):
        print(f"\n{'='*50}")
        print(f"TIME'S UP! {timer['name']}")
        print(f"Target time reached: {timer['target_time'].strftime('%H:%M:%S')}")
        print(f"{'='*50}")
        
        for _ in range(3):
            try:
                winsound.Beep(800, 1000)
                time.sleep(0.5)
            except:
                print("DING! DING! DING!")
                time.sleep(0.5)
    
    def display_live_countdown(self, timer_index):
        if timer_index < 0 or timer_index >= len(self.timers):
            print("Invalid timer index")
            return
        
        timer = self.timers[timer_index]
        print(f"Displaying live countdown for: {timer['name']}")
        print("Press Ctrl+C to return to menu")
        
        try:
            while timer['active'] and timer in self.timers:
                remaining = self.get_time_remaining(timer['target_time'])
                
                if remaining['total_seconds'] <= 0:
                    print("\nTIME'S UP!")
                    break
                
                countdown_str = self.format_time_remaining(remaining)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Timer: {timer['name']}")
                print(f"Target: {timer['target_time'].strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"\nTime Remaining: {countdown_str}")
                print("\nPress Ctrl+C to return to menu")
                
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nReturning to menu...")
    
    def run(self):
        def timer_thread():
            while self.running:
                self.check_timers()
                time.sleep(1)
        
        thread = threading.Thread(target=timer_thread)
        thread.daemon = True
        thread.start()
        
        self.show_menu()
    
    def show_menu(self):
        while self.running:
            print(f"\nCurrent time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("\nCountdown Timer Menu:")
            print("1. Set timer by duration (hours, minutes, seconds)")
            print("2. Set timer by target time")
            print("3. List active timers")
            print("4. Watch timer countdown")
            print("5. Remove timer")
            print("6. Exit")
            
            choice = input("Choose an option (1-6): ").strip()
            
            if choice == '1':
                self.set_duration_timer()
            elif choice == '2':
                self.set_target_timer()
            elif choice == '3':
                self.list_timers()
            elif choice == '4':
                self.watch_timer()
            elif choice == '5':
                self.remove_timer_interactive()
            elif choice == '6':
                self.running = False
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def set_duration_timer(self):
        try:
            name = input("Enter timer name (optional): ").strip() or "Duration Timer"
            hours = int(input("Enter hours (0-23): ") or "0")
            minutes = int(input("Enter minutes (0-59): ") or "0")
            seconds = int(input("Enter seconds (0-59): ") or "0")
            
            if hours < 0 or minutes < 0 or seconds < 0:
                print("Time values must be positive")
                return
            
            if hours == 0 and minutes == 0 and seconds == 0:
                print("Timer duration must be greater than 0")
                return
            
            self.add_duration_timer(hours, minutes, seconds, name)
            
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    
    def set_target_timer(self):
        try:
            name = input("Enter timer name (optional): ").strip() or "Target Timer"
            date_str = input("Enter target date (YYYY-MM-DD) or press Enter for today: ").strip()
            time_str = input("Enter target time (HH:MM:SS or HH:MM): ").strip()
            
            if len(time_str.split(':')) == 2:
                time_str += ":00"
            
            if not date_str:
                date_str = datetime.date.today().strftime('%Y-%m-%d')
            
            target_datetime = datetime.datetime.strptime(f"{date_str} {time_str}", '%Y-%m-%d %H:%M:%S')
            
            if target_datetime <= datetime.datetime.now():
                print("Target time must be in the future")
                return
            
            self.add_timer(target_datetime, name)
            
        except ValueError:
            print("Invalid date/time format. Use YYYY-MM-DD for date and HH:MM:SS for time")
    
    def watch_timer(self):
        if not self.timers:
            print("No active timers to watch")
            return
        
        self.list_timers()
        try:
            index = int(input("Enter timer number to watch: ")) - 1
            self.display_live_countdown(index)
        except (ValueError, KeyboardInterrupt):
            print("Invalid input or interrupted")
    
    def remove_timer_interactive(self):
        if not self.timers:
            print("No timers to remove")
            return
        
        self.list_timers()
        try:
            index = int(input("Enter timer number to remove: ")) - 1
            self.remove_timer(index)
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    countdown_timer = CountdownTimer()
    print("Welcome to Countdown Timer!")
    print("Set timers by duration or target time and get notified when they expire.")
    countdown_timer.run()
