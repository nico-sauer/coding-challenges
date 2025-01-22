price = float(input("Enter price of item: "))

discountRate = int(input("Enter the percentage discount: "))

discount = price * discountRate/100

discountedPrice = price - discount
print("Price Before Discount= {}€\nDiscount Rate= {}%\nDiscount= {}€\nPrice After Discount= {}€".format (price, discountRate, discount, discountedPrice))
