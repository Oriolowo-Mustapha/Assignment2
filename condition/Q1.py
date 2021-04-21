import random
lottery_num = random.randint(100,999)
print(lottery_num)
user_num = int(input("Enter any three digit: "))
lottery_tens = lottery_num // 10
lottery_ones = lottery_num % 10
user_tens = user_num // 10
user_ones = user_num % 10

if lottery_num == user_num:
    print("All your numbers match in exact order! Your reward is $10,000!")
elif lottery_tens == user_tens:
    print("All your numbers match! Your reward is $3,000!")
elif lottery_tens == user_tens:
    print("One of your numbers match the lottery. Your reward is $1,000!")
else:
    print("Your numbers don't match! Sorry!")