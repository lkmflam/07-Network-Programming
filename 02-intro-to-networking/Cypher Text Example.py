# plain text ABCDEFGHIJKLMNOPQRSTUVWXYZ
#Cypher text DEFGHIJKLMNOPQRSTUVWXYSABC
#So HELLO becomes KHOOR

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Str_in = input("Enter a message, Like Hello: ")
shift = int(input("Shift value, like 13: "))
n = len(Str_in)
Str_out = ""
for i in range(n):
    c = Str_in[i]
    loc = alpha.find(c)
    #print(i, c, loc, end = " ")
    newloc = (loc + shift)%26
    Str_out += alpha[newloc]
    #print(newloc, Str_out)
print("Obfuscated verion: ", Str_out)     

#Works as long as user enters all upper case letters
#Be familiar with ASCII encoding chart