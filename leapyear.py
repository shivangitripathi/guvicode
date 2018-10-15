teapyear=int(input())
if teapyear%4==0:
    if teapyear%400==0:
        print("yes")
else:
    print("No")