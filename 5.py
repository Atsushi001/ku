slovo = input()

def capitalize(slovo):
    words = slovo.split()
    capitalized = [word[:1].lower() + word[1:].capitalize() for word in words]
    return ' '.join(capitalized)

result = capitalize(slovo)
print(result)