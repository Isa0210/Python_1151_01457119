def primary_arithmetic(num1, num2):
    carry_count = 0

    # Pad the shorter number with leading zeros
    max_length = max(len(num1), len(num2))
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)

    # Perform addition from right to left
    carry = 0
    for i in range(max_length-1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        if digit_sum >= 10:
            carry_count += 1
            carry = 1
        else:
            carry = 0
    return carry_count

while True:
    num1, num2 = input().split()
    if num1 == '0' and num2 == '0':
        break
    n = primary_arithmetic(num1, num2)
    if n == 0:
        print("No carry operation.")
    elif n == 1:
        print(f"{n} carry operation.")
    else:
        print(f"{n} carry operations.")