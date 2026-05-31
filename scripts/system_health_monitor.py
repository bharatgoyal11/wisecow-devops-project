import psutil
from datetime import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    print("\n===== System Health Report =====")
    print(f"Time: {datetime.now()}")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {disk_usage}%")

    if cpu_usage > CPU_THRESHOLD:
        print("ALERT: High CPU Usage!")

    if memory_usage > MEMORY_THRESHOLD:
        print("ALERT: High Memory Usage!")

    if disk_usage > DISK_THRESHOLD:
        print("ALERT: High Disk Usage!")

    print("\nRunning Processes:")
    for process in psutil.process_iter(['pid', 'name']):
        print(process.info)

if __name__ == "__main__":
    check_system_health()