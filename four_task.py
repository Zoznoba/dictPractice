d = {}

for _ in range(int(input())):
    number, name = input().lower().split()
    d.update({name: [*d[name], number]}) if d.get(name) else d.update({name: [number]})

for _ in range(int(input())):
    name = input().lower()
    print(*d[name])
