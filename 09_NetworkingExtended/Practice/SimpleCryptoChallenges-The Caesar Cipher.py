decipherthis = "MYXQBKDEVKDSYXC"
alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
shift = int(input("Shift value, like 16: "))
length = len(decipherthis)
deciphered = ""
for i in range(length):
    num = decipherthis[i]
    lookforletter = alphabet.find(num) #Need to determine where the letter is since we can't just shift it to the location. Needs to match.
    looking = (lookforletter + shift)%26
    deciphered += alphabet[looking]
print("Consider this deciphered: ", deciphered)

