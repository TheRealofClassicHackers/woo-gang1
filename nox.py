import time
import random
import getpass
import os

# ANSI color codes for colorful output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Sample password list for simulation (63 wrong + 1 correct)
passwords = [
    "password123", "refentse2023", "hackme123", "letmein", "admin123", "secretpass",
    "facebook2023", "tryharder", "12345678", "qwertyuiop", "hunter2", "pass1234",
    "refentse1", "welcome123", "login123", "abc123", "testpass", "hack4fun",
    "socialmedia", "bruteforce1", "tryagain", "passpass", "123qwe", "zxcvbnm",
    "letmein123", "password!", "refentse99", "fbhack", "crackme", "1234567890",
    "qwerty123", "login2023", "securepass", "hacker123", "trythis", "pass4321",
    "refentse2022", "fb123", "test123", "hackit", "password99", "qwerty321",
    "loginpass", "12345abc", "refentse!", "crack123", "funpass", "social123",
    "tryhard123", "pass2023", "hackme2023", "qwertyabc", "loginme", "ref123",
    "testpass123", "fbpass", "hack2023", "try123", "password2023", "qwerty789",
    "loginfb", "refentsepass", "crack2023", "fun123", "qwerty4sho102"  # Correct password
]

def clear_screen():
    """Clear the console screen for a clean UI."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Display the T.R.C.H. banner."""
    clear_screen()
    print(f"{CYAN}============================================================{RESET}")
    print(f"{BLUE}🎉 T.R.C.H. Brute Force Simulation Tool 🎉{RESET}")
    print(f"{CYAN}       CyberSmith's Account Quest - Level 1       {RESET}")
    print(f"{CYAN}============================================================{RESET}")
    print()

def authenticate_tool():
    """Authenticate user with tool password."""
    tool_password = "TRCH2025"
    print(f"{YELLOW}🔐 Enter the T.R.C.H. tool password to begin:{RESET}")
    user_input = getpass.getpass("Password: ")
    
    if user_input == tool_password:
        print(f"{GREEN}✅ Access Granted! Awesome work, hacker! You're killing it!{RESET}")
        time.sleep(1)
        return True
    else:
        print(f"{RED}❌ Access Denied! Incorrect password. Try again later.{RESET}")
        time.sleep(2)
        return False

def check_target():
    """Prompt for target name/email and verify."""
    print(f"{YELLOW}🎯 Enter the target's name or email:{RESET}")
    target = input("Target: ").strip()
    if target.lower() == "refentse matel":
        print(f"{GREEN}✅ Target 'Refentse Matel' found! Preparing brute force simulation...{RESET}")
        time.sleep(1)
        return True
    else:
        print(f"{RED}❌ Target not found! Please check the name or email and try again.{RESET}")
        time.sleep(2)
        return False

def explain_brute_force():
    """Explain brute-forcing, its uses, and dangers."""
    clear_screen()
    print(f"{CYAN}============================================================{RESET}")
    print(f"{BLUE}📚 Level 1: Understanding Brute Forcing 📚{RESET}")
    print(f"{CYAN}============================================================{RESET}")
    print(f"{YELLOW}What is Brute Forcing?{RESET}")
    print("Brute forcing is a hacking technique where an attacker tries every possible password or key combination to gain access to a system or account. It’s like trying every key on a keyring until one unlocks the door. 🔑")
    print()
    print(f"{YELLOW}How Does It Work?{RESET}")
    print("The tool systematically guesses passwords from a list or generates them (e.g., 'password1', 'password2'). It keeps trying until it finds the correct one or exhausts all options. Automated scripts make this fast, but it can take time for complex passwords. 💻")
    print()
    print(f"{YELLOW}What Can It Be Used For?{RESET}")
    print("- **Ethical Hacking**: With permission, security experts use brute forcing to test system vulnerabilities, helping companies strengthen their defenses. ✅")
    print("- **Password Recovery**: It can help recover lost passwords for personal accounts (if legal). 🔐")
    print()
    print(f"{YELLOW}Why Is It Dangerous?{RESET}")
    print("- **Unauthorized Access**: Malicious hackers use brute forcing to break into accounts, steal data, or cause harm. 😈")
    print("- **Time and Resources**: Strong passwords make brute forcing slow, but weak passwords (like '123456') are cracked quickly. ⏰")
    print("- **Legal Risks**: Unauthorized brute forcing is illegal and can lead to severe consequences. 🚨")
    print("- **Account Lockouts**: Many systems lock accounts after too many failed attempts, disrupting users. 🔒")
    print()
    print(f"{GREEN}This Level Teaches You:{RESET} How to think like an ethical hacker, understand password vulnerabilities, and appreciate the importance of strong, unique passwords. Keep practicing to stay sharp! 🌟")
    print(f"{CYAN}============================================================{RESET}")
    print(f"{YELLOW}Press Enter to start the brute force simulation...{RESET}")
    input()

def simulate_brute_force():
    """Simulate brute-forcing the account."""
    clear_screen()
    print(f"{CYAN}============================================================{RESET}")
    print(f"{BLUE}🔨 Brute Forcing Account: Refentse Matel 🔨{RESET}")
    print(f"{CYAN}============================================================{RESET}")
    print(f"{YELLOW}Initiating brute force attack simulation...{RESET}")
    time.sleep(2)
    
    for i, password in enumerate(passwords, 1):
        print(f"{RED}Attempt #{i}: Trying password '{password}'... ❌ Wrong password!{RESET}")
        time.sleep(0.3)  # Delay for realism
        if password == "qwerty4sho102":
            print(f"{GREEN}✅ Success! Password found: '{password}'{RESET}")
            print(f"{BLUE}🎉 Account access granted for Refentse Matel!{RESET}")
            break
    
    print(f"{CYAN}============================================================{RESET}")
    print(f"{GREEN}Congratulations! You've completed Level 1 of CyberSmith's Account Quest!{RESET}")
    print(f"{YELLOW}Stay tuned for the next challenge!{RESET}")

def main():
    print_banner()
    if not authenticate_tool():
        return
    clear_screen()
    print_banner()
    if not check_target():
        return
    explain_brute_force()
    simulate_brute_force()

if __name__ == "__main__":
    main()