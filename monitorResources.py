import psutil
import time
import subprocess

def send_telegram_message(message):
    subprocess.run(["python3", "telegramMessage.py", message])

cpu_sent = False
memory_sent = False
fileSystem_sent = False
def monitor_resources():
    global cpu_sent,memory_sent,fileSystem_sent

    cpu_percent = psutil.cpu_percent(interval=0.01)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    print(f"CPU Usage: {cpu_percent}%, Memory Usage: {memory_percent}%, Disk Usage: {disk_percent}%")

    if cpu_percent > 84 and not cpu_sent:
        send_telegram_message(f"CPU usage is over 84% !")
        cpu_sent= True
    if memory_percent > 69 and not memory_sent:
        send_telegram_message(f"Memory usage is over 69% !")
        memory_sent= True
    if disk_percent > 77 and not fileSystem_sent:
        send_telegram_message(f"Disk usage is over 77% !")
        fileSystem_sent= True


if __name__ == "__main__":
    while(True):
        monitor_resources()
