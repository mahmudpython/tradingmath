"""
Now coin price is 100 taka.
30 minus ago its down to 80 taka and 10 minutes ago its highest price was 120 taka.
How much percentage the price goes and down?
"""

current_price = int(input("What is current price ? :"))
# TODO : Use input for high_price and low_price
high_price = int(input("What is high price ? :"))
low_price = int(input("What is low price ? :"))


price_increase = high_price-current_price
high_percentage = (price_increase*100)/current_price
print(f"Height percentage: {high_percentage} %")


lost_price = low_price-current_price
lost_percentage = (lost_price*100)/current_price
print(f"Lost percentage: {lost_percentage} %")

today = "lost_percentage"
money = "current_price"

if today == "lost persentage" and money > "current_price":
   print("oh no! loss my buseness")
else:
    print("wow! my buseness grow")



today = "friday"
if today == "friday" :
    print("i am going to be a aleep")
elif taday == "monday":
    print("take your brother to dential hospital")
else:
    print("oh no! school! exam! no oh")
