"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindrome_products = []

for i in range(1000,1,-1):
    for j in range(1000,i,-1):  # setting bound to "i" makes it a little less brute force
        product = i*j
        if str(product) == str(product)[::-1]:
            palindrome_products.append(product)
            print(product)

print(f'Largest palindrome product of 3-digit numbers is {max(palindrome_products)}')
