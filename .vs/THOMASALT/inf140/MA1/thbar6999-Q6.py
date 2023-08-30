from hashlib import *
from random import randint
from multiprocessing import Process
import time


def getPassword():
    pword = sha256(b"ZZZ9999").hexdigest()
    return pword


hxUserPw = getPassword()
print(hxUserPw)


def Bruteforce(hx):
    usrPw = b""
    u = "AAA"
    d = "0000"
    print("running 1")

    while sha256(usrPw).hexdigest() != hx:
        pos = randint(0, 2)
        u = u[:pos] + chr(randint(65, 90)) + u[pos + 1 :]

        pos = randint(0, 3)
        d = d[:pos] + chr(randint(48, 57)) + d[pos + 1 :]

        usrPw = bytes(u + d, "utf-8")
    print(usrPw)


def Bruteforce2(hx):
    usrPw = "AAA0000"
    print("running 2")
    for a in range(ord("A"), ord("Z") + 1):
        usrPw = usrPw[:0] + chr(a) + usrPw[1:]
        for b in range(ord("A"), ord("Z") + 1):
            usrPw = usrPw[:1] + chr(b) + usrPw[2:]
            for c in range(ord("A"), ord("Z") + 1):
                usrPw = usrPw[:2] + chr(c) + usrPw[3:]
                for d in range(ord("0"), ord("9") + 1):
                    usrPw = usrPw[:3] + chr(d) + usrPw[4:]
                    for e in range(ord("0"), ord("9") + 1):
                        usrPw = usrPw[:4] + chr(e) + usrPw[5:]
                        for f in range(ord("0"), ord("9") + 1):
                            usrPw = usrPw[:5] + chr(f) + usrPw[6:]
                            for g in range(ord("0"), ord("9") + 1):
                                usrPw = usrPw[:6] + chr(g) + usrPw[7:]
                                if sha256(bytes(usrPw, "utf-8")).hexdigest() == hx:
                                    return usrPw
