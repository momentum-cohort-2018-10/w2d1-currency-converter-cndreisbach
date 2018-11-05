def convert(rates, value, current, to):
    if current == to:
        return value

    # rates = [("USD", "EUR", 0.74), ('EUR', 'JPY', 100)]
    for conversion in rates:
        # conversion = ("USD", "EUR", 0.74)
        if current == conversion[0] and to == conversion[1]:
            return value * conversion[2]
        if current == conversion[1] and to == conversion[0]:
            return value / conversion[2]

    raise ValueError(f"can't convert from {current} to {to}")
