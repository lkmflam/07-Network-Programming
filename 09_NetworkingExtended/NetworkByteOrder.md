# Little Endian and Big Endian Explained:

A 32-bit integer has four bytes, each byte comprising of 8 bits.
In Little Endian Format, least significant byte(LSB) will be placed in the lowest address and the most significant byte(MSB)
will be placed in the highest address.

 

For example, if the starting address is X, the least significant byte will be placed in X,
and the next least significant byte will be placed in X+1, the next least significant byte
at X+2 and the most significant byte will be placed in X+3.
In Little Endian, the LSB is stored at the smallest address.
