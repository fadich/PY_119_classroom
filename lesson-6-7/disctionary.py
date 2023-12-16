import random


dictionary = {
    "hello": "привіт",
    "world": "світ",
    "my_value": None,
}

word = input("Eng word: ")
# if word in dictionary:
#     translation = dictionary[word]
#     print(f"Translation is: {translation}")
# else:
#     print("This word does not exist, sorry")

translation = dictionary.get(word, "<UNKNOWN WORD>")  # dictionary[word] if word in dictionary else None
if translation is None:
    print("This word does not exist, sorry")
else:
    print(f"Translation is: {translation}")

print("==============")
tr = dictionary.pop(word, None)
print(tr, dictionary)

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())


print("====" * 20)

a = {
    "another_key": "Another value",
    "my_value": "My value!",
}

c = {**dictionary, **a}
print(c)

print(list(dictionary))

print("++++" * 20)

for item in dictionary.items():
    # key = item[0]
    # value = item[1]
    key, value = item  # key, value = item[0], item[1]
    print(item, key, value)

for key, value in dictionary.items():
    print(key, value)


c = {i: random.randint(1, 10) for i in range(10)}
print(c)

a = [random.randint(1, 10) for _ in range(10)]
print(c[5])
print(a[5])

dictionary_list = (("hi",  "привіт"), ("hello", "привіт"))
print(dictionary_list, dict(dictionary_list))
