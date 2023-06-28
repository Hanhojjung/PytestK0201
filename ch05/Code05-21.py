outFp = None 
outStr = ""

# outFp = open("C:/Temp/data3.txt", "w", encoding="utf-8")
with open("C:/Temp/data4.txt", "w", encoding="utf-8")as outFp :

    while True:
        outStr = input("내용 입력 : ")
        if outStr != "" :
            outFp.writelines(outStr + "\n")
        else :
            break

# outFp.close()
print("--- 정상적으로 파일에 씀 ---")
