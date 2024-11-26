#Point 2
def kartesh(num):
    num_str =str (num)
    sum_kartesh = sum(int(kartesh) for kartesh in num_str)
    return sum_kartesh

number = int(input("Write number's three num: "))

if 100 <= number <= 999:
    result = kartesh(number)
    print(f"Total numb's {number}: {result}")
else:
    print("Write three number's")