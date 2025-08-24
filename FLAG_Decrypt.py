import sys
from Crypto.Cipher import AES

def gcm(data, key):
    nonce = data[:12]
    ct = data[12:-16]
    tag = data[-16:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    pt = cipher.decrypt_and_verify(ct, tag)
    return pt

key = bytes.fromhex("133a985d25765d4af3c84fcb1f8296f888d5d8fa028697e186939dbaf283108e")
data = open("FLAG.txt.ryk", "rb").read()
pt = gcm(data, key)
if pt is None:
    print("failed")
    sys.exit(1)
print(pt)

with open("FLAG.txt", "wb") as f:
    f.write(pt)


