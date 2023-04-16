# This script checks your recycle container size and calculate your refund
print("Welcome to our retail center\n=========================")
all_widgets = int(input("How many Widgets did you buy ?"))
all_gizmos = int(input("How many Gizmos did you buy ?"))

widgets_total = all_widgets * 75
gizmos_total = all_gizmos * 112
total_weight = widgets_total + gizmos_total
print(
    f'You bought {all_widgets} widgets, your total weight is {widgets_total} grams')
print(
    f'You bought {all_gizmos} gizmos, your total weight is {gizmos_total} grams')
print(f"Your total weight is {total_weight} grams")
print("Thank you for buying")
