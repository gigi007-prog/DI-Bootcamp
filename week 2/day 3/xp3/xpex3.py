#Exercise 1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Currency(self.currency, self.amount + other)
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        raise TypeError("Unsupported type for addition with Currency")

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        else:
            raise TypeError("Unsupported type for in-place addition with Currency")
        return self

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
print(str(c1))  
print(int(c1)) 
print(c1 + 5)  
c1 += 5
print(c1)


