import os
from Crypto.Cipher import AES

def gcm(data, key):
    nonce = data[:12]
    ct = data[12:-16]
    tag = data[-16:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    pt = cipher.decrypt_and_verify(ct, tag)
    return pt

key = bytes.fromhex("133a985d25765d4af3c84fcb1f8296f888d5d8fa028697e186939dbaf283108e")

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".ryk"):
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                encrypted_data = f.read()
            try:
                decrypted_data = gcm(encrypted_data, key)
                new_file_path = file_path[:-4]
                with open(new_file_path, "wb") as f:
                    f.write(decrypted_data)
                os.remove(file_path)
                print(f"Decrypted: {new_file_path}")
            except Exception as e:
                print(f"Failed to decrypt {file_path}: {e}")