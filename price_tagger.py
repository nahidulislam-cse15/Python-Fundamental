prices = [100, 250, 400, 50]
def GetDiscountPrices(prices,DiscountPercent):
    discounted_prices = [p - p*DiscountPercent/100 for p in prices]
    print(f"Discounted Price:{discounted_prices}")
print(f"Original Price:{prices}")
GetDiscountPrices(prices,10)