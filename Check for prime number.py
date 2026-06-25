while True:
    try:
        number = int(input())
        number = abs(number)
        break
    except:
        print("Введите целое число")
# while True:
#     if isinstance(number,int):
#         if number<0:
#             number=-number
#         break
#     print("Введите целое число")
#     number =int(input())
if number % 2 == 0:
    if number == 2:
        print("простое")
    else:
        print("составное")
else:
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            print("составное")
            break
    else:
        print("простое")
