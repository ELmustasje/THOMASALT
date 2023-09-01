from hashlib import *
import time
from random import randint
import multiprocessing


def getPassword():
    pword = input("lag et passord i formatet uuudddd: ")
    pword = sha256(bytes(pword, "utf-8")).hexdigest()
    return pword


##går fra AAA0000 - AAA0001 osv
def Bruteforce(hx):
    usrPw = ""
    print("Algorithm 1 running")
    start = time.time()
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
                                    print(f"1 used {time.time()-start} to find {usrPw}")
                                    return usrPw


Bruteforce(getPassword())
