d = {}
for _ in range(int(input())):
    country, *cities = input().lower().split()
    #cities = [city.lower() for city in cities]
    d.update({country: cities})

for _ in range(int(input())):
    word = input().lower()
    for key, value in d.items():
        print(key.capitalize()) if word in value else False
