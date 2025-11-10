
import time

allowed_users = ["Michael", "Ada", "Tunde", "Sandy"]

blocked_users = {"Patrick", "Mr Krabs"}

is_running = True

failed_attempts = 0

def login_system():
    global failed_attempts

    name = input("Enter your name: ").title()

    if name in allowed_users:
        print("Checking.....")
        time.sleep(1.5)
        current_time = time.strftime("%I:%M %p")
        print(f"Access Granted! Welcome {name}✅")
        print(f"Login time: {current_time}")

    elif name in blocked_users:
        print("Checking....")
        time.sleep(1.5)
        print(f"Access Denied! You are blocked❌")

    else:
        failed_attempts += 1
        print("User not recognized..Please register")
        print(f"Failed attempts #{failed_attempts}")
        print()

def register():
    name = input("Enter a name to register: ").title()
    if name in allowed_users:
        print(f"{name} is already registered✅")
        print()
    elif name in blocked_users:
        print(f"cannot register! {name} is blocked")
        print()
    else:
        allowed_users.append(name)
        print(f"{name} successfully registered")
        print()

def status():
    print("======System Status=====")
    print("Checking......")
    time.sleep(2)
    print("Allowed users:", ", ".join(allowed_users))
    print("Blocked users:", ", ".join(blocked_users))

def quit():
    global is_running
    print("Exiting system....")
    time.sleep(1)
    is_running = False

while is_running:
    print("\n----- Login System -----")
    command = input("Enter command(login/register/status/quit): ").lower()

    match command:

        case "login":
            login_system()
        case "register":
            register()
        case "status":
            status()
        case "quit":
            quit()
        case _:
            print("Oops..Command not recognized❌")
