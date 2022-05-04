def sumSquareDigits(self, n):
    output = 0
    while n:
        output += (n % 10) ** 2
        n = n // 10
    return output


print(150 % 10)