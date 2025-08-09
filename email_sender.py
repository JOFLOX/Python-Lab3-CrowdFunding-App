import smtplib
from dotenv import load_dotenv
import os

load_dotenv()


def send_email(email: str, code: str) -> bool:
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(os.getenv("EMAIL"), os.getenv("PASSWD"))

        text = f"Subject: Activation Code\n\nYour activation code is {code}"

        server.sendmail(os.getenv("EMAIL"), email, text)
        server.quit()
        return True
    except:
        return False
    

