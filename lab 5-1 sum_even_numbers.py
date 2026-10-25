def sum_even_numbers(*numbers):
    return sum(num for num in numbers if num % 2 == 0)
while True:
    s=input().split()
    if s==["END"]:
        break
    numbers = [int(num) for num in s]
    ans = sum_even_numbers(*numbers)
    print(ans)