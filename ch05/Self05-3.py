inFp = None
inStr = ""
lineNum = 1

inFp = open("C:/Temp/test2.txt","r", encoding="utf-8")

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break
    print("%d : %s" %(lineNum,inStr), end= "")
    lineNum += 1