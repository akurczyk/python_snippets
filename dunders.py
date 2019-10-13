import copy


class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def __repr__(self):
        return f'Account({self.name}, start_balance={self.balance})'

    def __str__(self):
        return f'{self.name} account - balance: {self.balance}'

    def __hash__(self):
        # WARNING: MUTABLE OBJECT - SHOULD NOT BE HASHABLE!
        return hash(self.name) ^ hash(self.balance)

    # abs(SELF)
    def __abs__(self):
        return abs(self.balance)

    # if SELF
    def __bool__(self):
        return self.balance != 0

    # len(SELF)
    def __len__(self):
        return len(self._transactions)

    #
    # SELF[key]
    #

    def __setitem__(self, key, value):
        if type(key) != int and not 0 <= key < len(self._transactions):
            raise ValueError

        self._transactions[key] = value

    def __getitem__(self, key):
        if type(key) != int:
            raise ValueError

        return self._transactions[key]

    # for i in SELF, iter(SELF), list(SELF)...
    def __iter__(self):
        for element in self._transactions:
            yield element

    #
    # > < >= <= == !=
    #

    def __gt__(self, other):
        if type(other) != Account:
            raise ValueError
        return self.balance > other.balance

    def __lt__(self, other):
        if type(other) != Account:
            raise ValueError
        return self.balance < other.balance

    def __ge__(self, other):
        if type(other) != Account:
            raise ValueError
        return self.balance >= other.balance

    def __le__(self, other):
        if type(other) != Account:
            raise ValueError
        return self.balance <= other.balance

    def __eq__(self, other):
        if type(other) != Account:
            raise ValueError
        return self.balance == other.balance

    def __ne__(self, other):
        if type(other) != Account:
            raise ValueError
        return self.balance != other.balance

    #
    # + - * / // % **
    #

    def __add__(self, other):
        if type(other) not in (int, float, Account):
            raise ValueError

        new = copy.deepcopy(self)
        if isinstance(other, int) or isinstance(other, float):
            new._transactions.append(other)
        elif isinstance(other, Account):
            new._transactions.extend(other._transactions)
        return new

    def __sub__(self, other):
        if type(other) not in (int, float):
            raise ValueError

        new = copy.deepcopy(self)
        new._transactions.append(-other)
        return new

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __pow__(self, other):
        pass

    #
    # += -= *= /= //= %= **=
    #

    def __iadd__(self, other):
        if type(other) not in (int, float):
            raise ValueError

        self._transactions.append(other)
        return self

    def __isub__(self, other):
        if type(other) not in (int, float):
            raise ValueError

        self._transactions.append(-other)
        return self

    def __imul__(self, other):
        pass

    def __idiv__(self, other):
        pass

    def __ifloordiv__(self, other):
        pass

    def __imod__(self, other):
        pass

    def __ipow__(self, other):
        pass

    #
    # (VALUE) + - * / // % ** (THIS)
    #

    def __radd__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __rdiv__(self, other):
        pass

    def __rfloordiv__(self, other):
        pass

    def __rmod__(self, other):
        pass

    def __rpow__(self, other):
        pass
