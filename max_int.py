#

u_number=0
max_number=0

while 1:
    u_number=int(input("Enter a number "))
    print(u_number)
    if u_number>max_number:
        max_number=u_number
    print(max_number)
    if u_number<0:
        break