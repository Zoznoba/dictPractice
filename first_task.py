d = {k.lower(): v for _ in range(int(input("input n"))) for k, v in [input().split(": ")]}
print(*(d.get(input().lower(), "не найдено") for _ in range(int(input("enter m")))), sep="\n")