"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

largest = 0
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        product = i * j
        if product > largest and str(product) == str(product)[::-1]:
            largest = product

print(largest)
