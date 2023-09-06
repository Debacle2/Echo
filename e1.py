def e1m1(em1):
    print (str(em1))

def e1m2():
    return input("Enter Input: ")
#    return em2

def e1m3(em1,em2):
    print(int(em1) + int(em2))

def e1m4(em1,em2,em3):
    em4 = int(em1) + int(em2) + int(em3)
    return em4

def e1m5(em1,em2):
    if (em1 < em2):
        print (str(em2))
    else:
        print (str(em1))

e1m1(e1m2())

e1m3(e1m2(),e1m2())

e1m1(e1m4(e1m2(), e1m2(), e1m2()))

e1m5(e1m2(), e1m2())
