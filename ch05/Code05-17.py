inFp = None    # 입력 파일
inStr = ""        # 읽어온 문자열

inFp = open("C:/Temp/test.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/test.txt", "r")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()
