# Author: Saud Kadiri
# Aim:    Multiplicative inverse using Extended Eucllidean Algorithm

class MultiplicativeInverse:

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)

    def is_coprime(self, a, b):
        return self.gcd(a, b) == 1

    def multiplicative_inverse(self, a, b):
        if self.is_coprime(a, b):
            print("Table:")
            print("\tq\tr1\tr2\tr\tt1\tt2\tt")
            r1, r2 = a, b
            q = r1 // r2
            r = r1 % r2
            t1, t2 = 0, 1
            t = t1 - q * t2
            while True:
                print(f"\t{q}\t{r1}\t{r2}\t{r}\t{t1}\t{t2}\t{t}")
                if r == 0:
                    break
                r1, r2 = r2, r
                q = r1 // r2
                r = r1 % r2
                t1, t2 = t2, t
                t = t1 - q * t2
            r1, r2 = r2, r
            t1, t2 = t2, t
            print(f"\t\t{r1}\t{r2}\t\t{t1}\t{t2}\n")
            print("s values not needed")
            print(f"gcd({a}, {b}) = 1")
            print(f"Inverse of {b} is {t1 if t1 >= 0 else t1, t1 % a}")
        else:
            print("No solution")
            return


mi = MultiplicativeInverse()
mi.multiplicative_inverse(100, 23)
