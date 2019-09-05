#Design an algorithm that finds the maximum positive integer
# input by a user.  
# The user repeatedly inputs numbers until a negative value
# is entered.



u_number=0
max_number=0

while 1:
    u_number=int(input("Input a number: "))
    #print(u_number)
    if u_number>max_number:
        max_number=u_number 
    if u_number<0:
        break
print("The maximum is",max_number)