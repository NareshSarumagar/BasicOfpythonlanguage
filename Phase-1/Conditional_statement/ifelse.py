# • Write a program: input a number, print whether it is Positive, Negative, or Zero.
# • Build a simple ATM check: if withdrawal amount <= balance ® success, else ® 'Insufficient funds'.


# Write a program: input a number, print whether it is positive, Negative, or Zero.

number = int(input("Enter your number: "))

if number>0: 
    print("The number is Positive: ")
elif number<0: 
    print("The number is Negative: ")
else: print("The number is Zero.")


# Build a simple ATM check: if withdrawal amount <=balance success, 'Insufficient funds'.

Ammount = 4000

Acc_amt = int(input("Enter your withdrawalAmt: "))

if Acc_amt>1000:
    acc_amt = Ammount - Acc_amt
    Acc_amt = Ammount - acc_amt
    print("With Drawal Ammount is : ", Acc_amt)

else: 
    print("Insufficient funds.")