str = input()

result = ''
for x in str:
    if x.isupper():
        x = x.lower()
        result += x
    else:
        x = x.upper()
        result += x

print(result)