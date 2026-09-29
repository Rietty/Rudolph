import hashlib

from utils.decorators import benchmark


@benchmark
def part_a(data: str) -> str:
    password: str = ""
    index: int = 0
    while len(password) < 8:
        while index > -1:
            hash = hashlib.md5(f"{data}{index}".encode()).hexdigest()
            if hash.startswith("00000"):
                password += hash[5]
                index += 1
                break
            else:
                index += 1
    return password


@benchmark
def part_b(data: str) -> str:
    password: list[str] = [""] * 8
    index: int = 0
    while any(c == "" for c in password):
        while index > -1:
            hash = hashlib.md5(f"{data}{index}".encode()).hexdigest()
            if hash.startswith("00000") and not hash[5].isalpha() and int(hash[5]) < 8:
                if password[int(hash[5])] == "":
                    password[int(hash[5])] = hash[6]
                index += 1
                break
            else:
                index += 1
    return "".join(password)


@benchmark
def parse(data: str) -> str:
    return data.strip()


test_data_a = """abc
"""

test_data_b = test_data_a
