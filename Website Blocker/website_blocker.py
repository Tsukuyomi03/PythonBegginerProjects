import os
import platform

def get_hosts_file_path():
    system = platform.system().lower()
    if system == "windows":
        return r"C:\Windows\System32\drivers\etc\hosts"
    else:
        return "/etc/hosts"

def read_hosts_file():
    hosts_path = get_hosts_file_path()
    try:
        with open(hosts_path, 'r') as file:
            return file.read()
    except PermissionError:
        print("Error: Permission denied. Please run as administrator.")
        return None
    except FileNotFoundError:
        print("Error: Hosts file not found.")
        return None

def write_hosts_file(content):
    hosts_path = get_hosts_file_path()
    try:
        with open(hosts_path, 'w') as file:
            file.write(content)
        return True
    except PermissionError:
        print("Error: Permission denied. Please run as administrator.")
        return False

def is_website_blocked(website, hosts_content):
    lines = hosts_content.split('\n')
    for line in lines:
        if line.strip() and not line.strip().startswith('#'):
            parts = line.split()
            if len(parts) >= 2 and website in parts[1]:
                return True
    return False

def block_website(website):
    hosts_content = read_hosts_file()
    if hosts_content is None:
        return False
    
    if is_website_blocked(website, hosts_content):
        print(f"{website} is already blocked.")
        return True
    
    redirect_ip = "127.0.0.1"
    block_entry = f"\n{redirect_ip} {website}\n{redirect_ip} www.{website}"
    
    updated_content = hosts_content + block_entry
    
    if write_hosts_file(updated_content):
        print(f"{website} has been blocked successfully.")
        return True
    return False

def unblock_website(website):
    hosts_content = read_hosts_file()
    if hosts_content is None:
        return False
    
    if not is_website_blocked(website, hosts_content):
        print(f"{website} is not currently blocked.")
        return True
    
    lines = hosts_content.split('\n')
    filtered_lines = []
    
    for line in lines:
        if line.strip() and not line.strip().startswith('#'):
            parts = line.split()
            if len(parts) >= 2 and (website in parts[1] or f"www.{website}" in parts[1]):
                continue
        filtered_lines.append(line)
    
    updated_content = '\n'.join(filtered_lines)
    
    if write_hosts_file(updated_content):
        print(f"{website} has been unblocked successfully.")
        return True
    return False

def list_blocked_websites():
    hosts_content = read_hosts_file()
    if hosts_content is None:
        return
    
    blocked_sites = []
    lines = hosts_content.split('\n')
    
    for line in lines:
        if line.strip() and not line.strip().startswith('#'):
            parts = line.split()
            if len(parts) >= 2 and parts[0] == "127.0.0.1":
                site = parts[1]
                if not site.startswith('www.') and site not in blocked_sites:
                    blocked_sites.append(site)
    
    if blocked_sites:
        print("\nCurrently blocked websites:")
        for i, site in enumerate(blocked_sites, 1):
            print(f"{i}. {site}")
    else:
        print("\nNo websites are currently blocked.")

def main():
    print("Welcome to Website Blocker!")
    print("Block or unblock websites on your system")
    print("-" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Block a website")
        print("2. Unblock a website")
        print("3. List blocked websites")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            website = input("Enter website to block (e.g., facebook.com): ").strip().lower()
            if website:
                if website.startswith('www.'):
                    website = website[4:]
                block_website(website)
            else:
                print("Error: Please enter a valid website.")
        
        elif choice == '2':
            website = input("Enter website to unblock (e.g., facebook.com): ").strip().lower()
            if website:
                if website.startswith('www.'):
                    website = website[4:]
                unblock_website(website)
            else:
                print("Error: Please enter a valid website.")
        
        elif choice == '3':
            list_blocked_websites()
        
        elif choice == '4':
            print("Thanks for using Website Blocker!")
            break
        
        else:
            print("Error: Please enter a valid choice (1-4).")

if __name__ == "__main__":
    main()
