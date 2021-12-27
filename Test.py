


ticker = "TSLA"

currency = "USD"

if ticker[-4] == "-":
    if ticker[-3:] != "USD":
        currency = ticker[-3:]

print(currency)