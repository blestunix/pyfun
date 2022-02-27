# Author: Saud Kadiri
# Implementation of the RSA algorithm

def is_prime(num):
    '''
    returns true if the number is prime else; false
    '''
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def get_p_q():
    '''
    We need p and q to be as large as possible but here we take it as input from the user
    '''
    p, q = 4, 4                       # any non-prime number
    while not is_prime(p):
        p = int(input("p: "))
    while not is_prime(q) or q == p:
        q = int(input("q: "))
    return p, q

def gcd(a, b):
    '''
    Finds the GCD of the given pair
    '''
    return a if b == 0 else gcd(b, a % b)

def is_coprime(a, b):
    '''
    returns if the given numbers are relatively prime
    '''
    return gcd(a, b) == 1

def extended_euclid(a, b):
    '''
    Extended euclid algorithm
    '''
    r1, r2 = a, b
    s1, s2 = 1, 0
    q, r = r1 // r2, r1 % r2
    s = s1 - q * s2
    while True:
        if r == 0:
            break
        r1, r2 = r2, r
        s1, s2 = s2, s
        q, r = r1 // r2, r1 % r2
        s = s1 - q * s2
    r1, r2 = r2, r
    s1, s2 = s2, s
    return s1 if s1 > 0 else s1 % b

# Program starts here
p, q = get_p_q()
n = p * q

phi = (p - 1) * (q - 1)
for e in range(2, phi):
    if is_coprime(phi, e):
        break

d = extended_euclid(e, phi)

public_key = (e, n)
private_key = (d, n)

print(f"Public key: {public_key}")
print(f"Private Key: {private_key}\n")

# read the message
m = n
while m >= n:
    m = int(input(f"Enter a message (an integer less than {n}): "))

# Print the encrypted message(ciphertext)
print()
print("=" * 30, "Encryption", "=" * 30)
print("\tC = M ^ e mod n")
print(f"\tC: Ciphertext\n\tM: Message(M < n)\n")
print(f"\tM = {m}\n\te = {e}\n\tn = {n}")
print(f"\n\ti.e. {m} ^ {e} mod {n}")
c = m ** e % n
print(f"\ti.e., C = {c}\n")
print("The encrypted message is:", c)

# print the decrypted message(plaintext)
print("=" * 30, "Decryption", "=" * 30)
print("\tP = C ^ d mod n")
print(f"\tP: Plaintext\n\tC: Ciphertext\n")
print(f"\tC = {c}\n\td = {d}\n\tn = {n}")
print(f"\n\ti.e. {c} ^ {d} mod {n}")
d = c ** d % n
print(f"\ti.e., D = {d}")
print("\nThe plaintext is:", d)
