import os
import smtplib
from email.message import EmailMessage
import pandas as pd
from utils.db_connect import *

# works only for windows for linux env use \
export_path = r'C:\python\EAP_Project\files'



def sent_email(email_subject: str,send_to: str,cc: str = None,bcc: str = None, content_plain=None,content_html=None,attach_dir:str =None,attach_files: list=[],
               smtp_server: str = "smtp.gmail.com", smtp_port: int = 587):
    """
    Send an email (with optional CC/BCC and attachments) via Gmail SMTP + App Password.
    – GMAIL_ADDRESS and GMAIL_APP_PASSWORD must be set in the environment. This will work only for me (Nikos) as iam using my own username
    """
    # Credentials from env
    username = 'rraidenikos@gmail.com'
    password = os.environ['GMAIL_APP_PASSWORD']
    sent_from = username
    # Build message
    msg = EmailMessage()
    msg["Subject"] = email_subject
    msg["From"]    = sent_from
    msg["To"]      = send_to
    if cc:
        msg["Cc"] = cc
    if bcc:
        msg["Bcc"] = bcc

    msg.set_content(content_plain)
    if content_html:
        msg.add_alternative(content_html, subtype="html")

    # Attach files if requested
    if attach_dir and attach_files:
        for fname in attach_files:
            path = f"{attach_dir}/{fname}"
            with open(path, "rb") as fp:
                data = fp.read()
            msg.add_attachment(
                data,
                maintype="application",
                subtype="octet-stream",
                filename=fname
            )

    # Send via Gmail
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(username, password)
            server.send_message(msg)
            print('mail sent')
    except Exception as e:
        print(e)


"""
    Example 
sent_email(email_subject="******", send_to="i",cc=None, bcc=None,content_plain="Υπενθύμιση Ραντεβου",\
           content_html="None",attach_dir=None,attach_files=None)
"""



def export_appointments_date(appointment_date:str):
    file_name = rf'\appointemnts_{appointment_date}.xlsx'
    location = export_path + file_name
    query = f"""
            select 
                b.first_name,
                b.last_name,
                a.appointment_date ,
                a.start_time,
                a.end_time 
        from project.appointments a 
        join 
            project.customers b 
                on	b.customer_id = a.customer_id 
        where 
            appointment_date = '{appointment_date}'
    """

    with conn.cursor() as cur:
        cur.execute(query, (appointment_date,))
        rows = cur.fetchall()
        cols = [desc[0] for desc in cur.description]

    df = pd.DataFrame(rows, columns=cols)
    df.to_excel(location, index=False)
    print(f"File Has been Exported for Date : {appointment_date}")
