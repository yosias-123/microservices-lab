from datetime import datetime

def log_info(message: str):
    print(f"[{datetime.now()}] {message}")
