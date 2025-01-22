starRating = int(input("Enter a star rating between 0 and 5 stars: "))

while starRating < 0 or starRating > 5:
    if starRating < 0 or starRating > 5:
        retry = int(input("Invalid Star Rating. Try again!\n>"))
        starRating = retry
print("Thank you!")