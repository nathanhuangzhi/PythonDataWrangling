def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    last_digit = digits[len(digits) - 1] + 1
    digits.pop()

    if not digits and last_digit == 10:
        digits = [1, 0]

    elif last_digit != 10:
        digits.append(last_digit)

    else:

        self.plusOne(digits)
        digits.append(0)

    return digits

print(plusOne([9]))