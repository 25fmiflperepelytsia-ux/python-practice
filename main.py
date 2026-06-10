word = input("Введіть слово: ")

if word == word[::-1]:
    print("Це паліндром")
else:
    print("Це не паліндром")
