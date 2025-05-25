import psycopg2
import os
from cryptography.fernet import Fernet
from utils.credentials import postgres

try : # for  windows
    key = os.getenv("PYKEY1")
except: # for mac
    key = os.environ["PYKEY1"]


def encrypt_pwd(pwd, key):
    """
        A function to encrypt postgres Password. Used only once in order to insert it to credentials.py
        :pwd -> str
        :key -> global value.
    """
    cipher_eng = Fernet(key)
    enc_pwd = cipher_eng.encrypt(bytes(pwd, 'utf-8'))
    print(enc_pwd.decode('utf-8'))

def decrypt_pwd(pwd, key):
    """
        A Function to decrypt our passwords that are located on credentials.py
    """
    cipher_eng = Fernet(key)
    dec_pwd = cipher_eng.decrypt(bytes(pwd, 'utf-8'))
    return dec_pwd.decode('utf-8')



postgres_pwd = postgres['pwd']
postgres_pwd = decrypt_pwd(postgres_pwd, key)

try:
    conn = psycopg2.connect(f"dbname='EAP_Project' user='postgres' host='localhost' port = '5432' password={postgres_pwd}")
    print("Connect to Database")
except: # for Art
    conn = psycopg2.connect(f"dbname='EAP_Project' user='postgres' host='localhost' port = '5433' password='3989'")
    print("Connect to Database")