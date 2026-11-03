import time
import threading
import re

running = False
last_activity = time.time()
timeout = 16 * 60
active_tasks = {}

def show_status():
    print("ZENØX BOT STATUS")
    print("Running:", running)
    print("Active tasks:", list(active_tasks.keys()) if active_tasks else "None")

def repeat_message(text, interval, task_id):
    while task_id in active_tasks:
        print(f"[تكرار] {text}")
        time.sleep(interval)

def process_command(command):
    global running, last_activity

    match = re.match(r"^(.+?)(\d+)s$", command.strip())
    if match:
        text = match.group(1).strip()
        seconds = int(match.group(2))

        if seconds < 5:
            print("المدة قصيرة جداً (أقل شي 5 ثواني)")
            return

        task_id = f"{text}_{seconds}"

        if task_id in active_tasks:
            del active_tasks[task_id]

        active_tasks[task_id] = True

        print("تم تفعيل الامر من قبل السيد زينوكس")
        print(text)
        print(f"يتم تكرارها كل {seconds} ثانية")

        thread = threading.Thread(target=repeat_message, args=(text, seconds, task_id), daemon=True)
        thread.start()
        return

    if command == "/start":
        running = True
        last_activity = time.time()
        print("Bot started")

    elif command == "/stop":
        running = False
        active_tasks.clear()
        print("Bot stopped + all repeats cleared")

    elif command == "/status":
        show_status()

    elif command == "/watch":
        last_activity = time.time()
        print("Activity monitoring enabled")

    elif command.startswith("/activity "):
        last_activity = time.time()
        print("Group activity recorded")

    elif command == "/stopall":
        active_tasks.clear()
        print("تم إيقاف جميع التكرارات")

    else:
        print("Unknown command")

print("ZENØX BOT CONTROL")
print("Type /help for commands")

while True:
    command = input("> ").strip()

    if command == "/help":
        print("الأوامر المتاحة:")
        print("/start   /stop   /status   /watch   /stopall")
        print("أو اكتب: نص + رقم + s")
        print("مثال: اهلا60s")
    else:
        process_command(command)

    if running and time.time() - last_activity >= timeout:
        print("16 minutes of inactivity detected")
        print("Notification: Group is inactive")
        last_activity = time.time()
