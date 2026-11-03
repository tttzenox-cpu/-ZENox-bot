
import time

running = False
last_activity = time.time()
timeout = 16 * 60

def show_status():
    print("ZENØX BOT STATUS")
    print("Running:", running)

def process_command(command):
    global running, last_activity

    if command == "/start":
        running = True
        last_activity = time.time()
        print("Bot started")

    elif command == "/stop":
        running = False
        print("Bot stopped")

    elif command == "/status":
        show_status()

    elif command == "/watch":
        last_activity = time.time()
        print("Activity monitoring enabled")

    elif command.startswith("/activity "):
        last_activity = time.time()
        print("Group activity recorded")

    else:
        print("Unknown command")

print("ZENØX BOT CONTROL")
print("Type /help for commands")

while True:
    command = input("> ").strip()

    if command == "/help":
        print("/start /stop /status /watch")
        print("/activity MESSAGE")

    else:
        process_command(command)
    
    if running and time.time() - last_activity >= timeout:
        print("16 minutes of inactivity detected")
        print("Notification: Group is inactive")
        last_activity = time.time()
  
