""" Assignment operators: = (x=5), 
                          += (x+=5), 
                          -= (x-=5),
                          *= (x*=5),
                          /= (x/=5),
                          //= (x//=5),
                          %= (x%=5). """

a = 10

print("Simple assignment (=):", a)

a += 5
print("Addition assignment (+=):", a)

a -= 3
print("Subtraction assignment (-=):", a)

a *= 2
print("Multiplication assignment (*=):", a)

a /= 2
print("Division assignment (/=):", a)

a = 10
a //= 3
print("Floor division assignment (//=):", a)

a = 10
a %= 3
print("Modulus assignment (%=):", a)

a = 2
a **= 3
print("Exponentiation assignment (**=):", a)

a = 10
a &= 3
print("Bitwise AND assignment (&=):", a)

a = 10
a |= 3
print("Bitwise OR assignment (|=):", a)

a = 10
a ^= 3
print("Bitwise XOR assignment (^=):", a)

a = 10
a >>= 1
print("Right shift assignment (>>=):", a)

a = 10
a <<= 1
print("Left shift assignment (<<=):", a)


