import smtplib
from dotenv import load_dotenv
import os
from validation import generate_code



load_dotenv()


def send_email(email: str, code: str) -> bool:
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(os.getenv("EMAIL"), os.getenv("PASSWD"))
        
        text = (
                "Subject: Your Activation Code\n\n"
                f"Hello,\n\n"
                f"Your activation code is: {code}\n\n"
                "Please enter this code in the application to verify your account.\n\n"
                "Thank you,\n"
                "The Support Team"
            )
        server.sendmail(os.getenv("EMAIL"), email, text)
        server.quit()
        return True
    except:
        return False
    

code = generate_code()
send_email("youssef.basha7@gmail.com", code)