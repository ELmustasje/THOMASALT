from hashlib import *
import time
import multiprocessing


def getPassword():
    pword = input("lag et passord i formatet uuudddd: ")
    pword = sha256(bytes(pword, "utf-8")).hexdigest()
    print(pword)
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


##går fra ZZZ9999 - ZZZ9998 osv
def Bruteforce2(hx):
    usrPw = ""
    print("Algorithm 2 running")
    start = time.time()
    for a in reversed(range(ord("A"), ord("Z") + 1)):
        usrPw = usrPw[:0] + chr(a) + usrPw[1:]
        for b in reversed(range(ord("A"), ord("Z") + 1)):
            usrPw = usrPw[:1] + chr(b) + usrPw[2:]
            for c in reversed(range(ord("A"), ord("Z") + 1)):
                usrPw = usrPw[:2] + chr(c) + usrPw[3:]
                for d in reversed(range(ord("0"), ord("9") + 1)):
                    usrPw = usrPw[:3] + chr(d) + usrPw[4:]
                    for e in reversed(range(ord("0"), ord("9") + 1)):
                        usrPw = usrPw[:4] + chr(e) + usrPw[5:]
                        for f in reversed(range(ord("0"), ord("9") + 1)):
                            usrPw = usrPw[:5] + chr(f) + usrPw[6:]
                            for g in reversed(range(ord("0"), ord("9") + 1)):
                                usrPw = usrPw[:6] + chr(g) + usrPw[7:]
                                if sha256(bytes(usrPw, "utf-8")).hexdigest() == hx:
                                    print(f"2 used {time.time()-start} to find {usrPw}")


##går fra AAA0000 - BAA0000
def Bruteforce3(hx):
    usrPw = "AAA0000"
    print("Algorithm 3 running")
    start = time.time()
    for a in range(ord("0"), ord("9") + 1):
        usrPw = usrPw[:6] + chr(a) + usrPw[7:]
        for b in range(ord("0"), ord("9") + 1):
            usrPw = usrPw[:5] + chr(b) + usrPw[6:]
            for c in range(ord("0"), ord("9") + 1):
                usrPw = usrPw[:4] + chr(c) + usrPw[5:]
                for d in range(ord("0"), ord("9") + 1):
                    usrPw = usrPw[:3] + chr(d) + usrPw[4:]
                    for e in range(ord("A"), ord("Z") + 1):
                        usrPw = usrPw[:2] + chr(e) + usrPw[3:]
                        for f in range(ord("A"), ord("Z") + 1):
                            usrPw = usrPw[:1] + chr(f) + usrPw[2:]
                            for g in range(ord("A"), ord("Z") + 1):
                                usrPw = usrPw[:0] + chr(g) + usrPw[1:]
                                if sha256(bytes(usrPw, "utf-8")).hexdigest() == hx:
                                    print(f"3 used {time.time()-start} to find {usrPw}")


##går fra ZZZ9999 - YZZ9999
def Bruteforce4(hx):
    usrPw = "ZZZ9999"
    print("Algorithm 4 running")
    start = time.time()
    for a in reversed(range(ord("0"), ord("9") + 1)):
        usrPw = usrPw[:6] + chr(a) + usrPw[7:]
        for b in reversed(range(ord("0"), ord("9") + 1)):
            usrPw = usrPw[:5] + chr(b) + usrPw[6:]
            for c in reversed(range(ord("0"), ord("9") + 1)):
                usrPw = usrPw[:4] + chr(c) + usrPw[5:]
                for d in reversed(range(ord("0"), ord("9") + 1)):
                    usrPw = usrPw[:3] + chr(d) + usrPw[4:]
                    for e in reversed(range(ord("A"), ord("Z") + 1)):
                        usrPw = usrPw[:2] + chr(e) + usrPw[3:]
                        for f in reversed(range(ord("A"), ord("Z") + 1)):
                            usrPw = usrPw[:1] + chr(f) + usrPw[2:]
                            for g in reversed(range(ord("A"), ord("Z") + 1)):
                                usrPw = usrPw[:0] + chr(g) + usrPw[1:]
                                if sha256(bytes(usrPw, "utf-8")).hexdigest() == hx:
                                    print(f"4 used {time.time()-start} to find {usrPw}")


if __name__ == "__main__":
    hxusrpw = getPassword()
    p1 = multiprocessing.Process(target=Bruteforce, args=[hxusrpw])
    p2 = multiprocessing.Process(target=Bruteforce2, args=[hxusrpw])
    p3 = multiprocessing.Process(target=Bruteforce3, args=[hxusrpw])
    p4 = multiprocessing.Process(target=Bruteforce4, args=[hxusrpw])
    p1.start()
    p2.start()
    p3.start()
    p4.start()
