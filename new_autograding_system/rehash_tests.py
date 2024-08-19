from hashlib import sha256
from os import listdir

f = "".join(listdir("test_cases"))

with open("tests.py", encoding="unicode-escape") as f:
    h = sha256(f.read().encode("unicode-escape")).hexdigest()

with open("test_cases/test_hash.py", "w") as f:
    f.write(f'EXP_HASH="{h}"')
    print("Hash saved as", h)

input()
