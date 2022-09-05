"""
Now coin price is 100 taka.
30 minus ago its down to 80 taka and 10 minutes ago its highest price was 120 taka.
How much percentage the price goes and down?
"""
# TODO : Use input for high_price and low_price
current_price = int(input("What is current_price?:"))
high_price = int(input("What is high price ? :"))
low_price = int(input("What is low price ? :"))


price_increase = high_price-current_price
high_percentage = (price_increase*100)/current_price
print(f"Height percentage: {high_percentage} %")


lost_price = low_price-current_price
lost_percentage = (lost_price*100)/current_price
print(f"Lost percentage: {lost_percentage} %")

today = "high_percentage:"
if today == "high_persentage" :
    print("wow! my buseness grow")
if today == "lost_percentage" :
    print("oh no! loss my buseness")
elif today == "high_percentage" :
    print("wow! grow our buseness")
else:
    print("oh no! loss my project")



today = (input("what is dotay? : "))
if today == "sunday" :
    print("i am going to be a aleep")
if today == "friday":
    print("my holiday!")
elif today == "monday":
    print("take your brother to dential hospital")
else:
    print("oh no! school! exam! no oh")
