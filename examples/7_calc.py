# Build a tax calculator!
print("Tax Calculator Application")
# input is default string type
price = input("Enter price of purchase: ")
tax_rate = input("Enter tax rate: ")

tax_amount = float(price) * float(tax_rate)
print("Tax: $" + str(tax_amount))
total_amount = float(price) + float(tax_amount)
print("Total: $" + str(total_amount))
