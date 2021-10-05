import Crypto.Random

key = Crypto.Random.get_random_bytes(16)
with open('./key.bin', "wb") as f:
    f.write(key)