def calender(a, b, c):
    if a > 31:
        print("Format #3")
    elif a>12 and a <= 31:
        if c > 31:
            print("Format #2") 
        else:
            print("Ambiguous")
    elif a <= 12:
        if b > 12:
            print("Format #1") 
        else:
            print("Ambiguous")

a, b, c = map(int, input().split())

calender(a, b, c)