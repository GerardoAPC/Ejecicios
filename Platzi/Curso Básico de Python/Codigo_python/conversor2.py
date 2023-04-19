currency = input("Type your country ")
amount = input("Type amount of money ")
amount = int(amount)
if currency == "Argentina":
    dollar_value = 70.22
    dollar_eq = amount / dollar_value
    dollar_eq = float(dollar_eq)
    dollar_eq = round(dollar_eq, 2)
    dollar_eq = str(dollar_eq)
    print("You have U$S " + dollar_eq)
elif currency == 'Chile':
    dollar_value = 786.50
    dollar_eq = amount / dollar_value
    dollar_eq = float(dollar_eq)
    dollar_eq = round(dollar_eq, 2)
    dollar_eq = str(dollar_eq)
    print("You have U$S " + dollar_eq)
else:
    print("Fatal error #1")