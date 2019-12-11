#XOR Example Practice
text = "kquht}"
#print("Enter key of 8 on the next prompt")
key = input("Enter key: ")
length = len(text)

for i in range(length):
    t =text[i]
    #Repeats key if key is shorter than text. Gets modulus of the length.
    k = key[i%len(key)]
    x = ord(k) ^ ord(t)
    print(t, k, x, chr(x))
#If key of 8 is used, then SIMPLE will be output