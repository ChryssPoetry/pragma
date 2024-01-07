#solution one
#1A
for x in range(7):
    #checking value from 0-6 to see which satisfies
    if (x**4 + x**3 + 2) %7 == 0:
        print(f"x = {x} is the solution for the congruence")

#1B
for x in range(343):
    #checking values from 0-342 to see which value satisfies
    if (x**7 +x + 1) %343 ==0:
        print(f"x ={x} is the solution to the congruence")


#code for solving problem 2
from math import gcd

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inv(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError('Inverse does not exist')
    return x % m

def chinese_remainder(x1, m1, x2, m2):
    if gcd(m1, m2) != 1:
        raise ValueError('Moduli are not coprime')
    M = m1 * m2
    M1, M2 = M // m1, M // m2
    inv_M1 = mod_inv(M1, m1)
    inv_M2 = mod_inv(M2, m2)
    x = (x1 * M1 * inv_M1 + x2 * M2 * inv_M2) % M
    return x

#code implementation for problem 4
def multiply_polynomials(a, b):
    # Base case: If either polynomial has a single term
    if len(a) == 1 or len(b) == 1:
        return [a[0] * b[0]]  # Return the product of the constants
    
    # Split the polynomials into parts
    m = len(a) // 2
    a0, a1 = a[:m], a[m:]
    b0, b1 = b[:m], b[m:]
    
    # Recursively multiply the polynomials
    c0 = multiply_polynomials(a0, b0)
    c2 = multiply_polynomials(a1, b1)
    temp = multiply_polynomials([a1[i] - a0[i] for i in range(len(a0))], 
                                 [b1[i] - b0[i] for i in range(len(b0))])
    c1 = [c0[i] + c2[i] - temp[i] for i in range(len(c0))]
    
    # Combine the results using the splitting formulas
    shift_c2 = [0] * (2 * m) + c2
    shift_c1 = [0] * m + c1
    
    result = [shift_c2[i] + shift_c1[i] + c0[i] for i in range(len(c0))]
    return result

# Example usage:
poly1 = [1, 2, 3]  # Coefficients of polynomial 1 (3x^2 + 2x + 1)
poly2 = [4, 5, 6]  # Coefficients of polynomial 2 (6x^2 + 5x + 4)
result = multiply_polynomials(poly1, poly2)
print("Result of multiplication:", result)

