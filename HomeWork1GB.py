#Point 2
# def kartesh(num):
#     num_str =str (num)
#     sum_kartesh = sum(int(kartesh) for kartesh in num_str)
#     return sum_kartesh

# number = int(input("Write number's three num: "))

# if 100 <= number <= 999:
#     result = kartesh(number)
#     print(f"Total numb's {number}: {result}")
# else:
#     print("Write three number's")

# Point 4
# def find_cranes(num):
#     x = num // 4
#     return (x, 2*x, x)

# num = int(input("Write numbers (num): "))

# result = find_cranes(num)
# print(f" Petya complite {result}, Katya complite {result}, Sergey complite {result}")

def billet_point(ticket_number):
    ticket_str = str(ticket_number)
    ticket_lenght = len(ticket_str) // 2
    
    first_ticket = sum(int(digit) for digit in ticket_str[:ticket_lenght])
    two_ticket = sum(int(digit) for digit in ticket_str[ticket_lenght:])
    return first_ticket == two_ticket


ticket_user = int(input("Write your lucky number's: "))

result = billet_point(ticket_user)

if result:
    print("Your WINNNER!")
else:
    print("Sorry, your LOOSSEE")
