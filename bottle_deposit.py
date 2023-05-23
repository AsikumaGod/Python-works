# This script checks your recycle container size and calculate your refund
print("Welcome to our recycling center\n=========================")
under_one = int(
    input("How many of your conatiners is under or equal to 1litre ?"))
above_one = int(input("How many of your conatiners is above 1litre ?"))

under_one_refund = under_one * 0.10
above_one_refund = above_one * 0.25
total_refund = under_one_refund + above_one_refund
print(
    f'You brought {under_one} containers under or equal to 1 liter, your refund for that is ${under_one_refund}')
print(
    f'You brought {above_one} containers under or equal to 1 liter, your refund for that is ${above_one_refund}')
print(f"Your total refund is ${total_refund}")
print("Thank you for recycling")
