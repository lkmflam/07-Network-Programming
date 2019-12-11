# plain text ABCDEFGHIJKLMNOPQRSTUVWXYZ
#Cypher text DEFGHIJKLMNOPQRSTUVWXYSABC
#So HELLO becomes KHOOR

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Str_in = input("Enter a message, Like Hello: ")
n = len(Str_in)
Str_out = ""
for i in range(n):
    c = Str_in[i]
    loc = alpha.find(c)
    print(i, c, loc, end = " ")
    newloc = loc + 3
    Str_out += alpha[newloc]
    print(newloc, Str_out)
print("Obfuscated verion: ", Str_out)     