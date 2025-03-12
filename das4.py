geo = input()

if geo =="square":
    a1=int(input())
    print(f"talbai{a1*a1}")
elif geo == "rectangle":
    a1=int(input())
    a2=int(input())
    print(f"talbai{a1*a2}")
elif geo== "circle":
    radius= int (input())
    print(f"talbai{3.14 * radius * radius}")
elif geo == "triangle":
    base = int(input())
    height = int(input())
    print(f"talbai {0.5 * base * height}")
else:
    print("tanii oruulsan geometriin torol buruu bn")