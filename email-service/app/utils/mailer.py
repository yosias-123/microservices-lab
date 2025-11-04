from datetime import datetime
from app.utils.logger import log_info

def send_email(to_email: str, subject: str, body: str):
    """
    Simula el envío de un correo electrónico.
    En producción se conectaría con un SMTP real o un servicio externo.
    """
    log_info(f"[SIMULATED EMAIL] To: {to_email}\nSubject: {subject}\nBody: {body}")
    print(f"[{datetime.now()}] Email simulated to {to_email}")
