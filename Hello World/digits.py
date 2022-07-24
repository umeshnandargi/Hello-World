n = 524
digits = []
while n > 0:
    digits.append(n % 10)
    n = n // 10

digits.reverse()
print(f"digits are {digits} and the sum of digits is {sum(digits)}")
