e1v1 = []
e1v2 = []
e1v3 = []


with open("e2.csv","r") as e2:

    e1v4 = e2.readlines()

    for e in e1v4:
        e1v5 = e.split(",")
        e1v1.append(e1v5[0])
        e1v2.append(e1v5[1])
        e1v3.append(e1v5[2])

    for e in range(len(e1v2)):
        print ("----------")
        print ("Rank:" + e1v1[e])
        print ("Girl Name:" + e1v2[e])
        print ("Boy Name: " + e1v3[e])
