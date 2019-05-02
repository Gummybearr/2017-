#2014312455-도경회
def computeServiceSales(filename):
    f1 = open(filename, "r")
    f2 = open("sales.txt",'w')
    servicelist = []
    servicedata = []
    #savefile입력 형태는 서비스,:,금액,--,사람이름
    #servicelist자료구조 = [서비스1,서비스2...]
    #servicedata자료구조 = [[서비스1 합산된 가격, [서비스1을 이용한 고객1,서비스1을 이용한 고객2...]],[서비스2 합산된 가격, [서비스2를 이용한 고객1....]]]
    while True:
        line = f1.readline().strip()
        if not line:
            break
        rawdata = line.split(":")
        if rawdata[2] not in servicelist:
            servicelist.append(rawdata[2])
            servicedata.append([rawdata[3],[rawdata[0]]])
        else:
            for i in range(len(servicelist)):
                if rawdata[2] in servicelist[i]:
                    addedprice = int(servicedata[i][0])+int(rawdata[3])
                    servicedata[i][0] = addedprice
                    servicedata[i][1].append(", ")
                    servicedata[i][1].append(rawdata[0])
    for i in range(len(servicelist)):
        f2.write(servicelist[i])
        f2.write(":")
        f2.write(str(servicedata[i][0]))
        f2.write("--")
        for j in range(len(servicedata[i][1])):
            f2.write(servicedata[i][1][j])
        f2.write('\n')
    f2.close()
    f1.close()
    return len(servicelist)
print(computeServiceSales("hotels.txt"))
