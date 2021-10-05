import Crypto.Random

vector = Crypto.Random.get_random_bytes(16)
with open('./iv.bin', "wb") as f:
    f.write(vector)