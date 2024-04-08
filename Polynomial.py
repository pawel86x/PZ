class Polynomial:

    def __init__(self, *cfs):
        self.__cfs = [float(i) for i in cfs]

    def __str__(self):
        pol = "".join([self.__cfs_str(self.__cfs[i]) + self.__power_str(self.__cfs[i], i)
                     for i in range(len(self.__cfs))])
        return pol[1:] if pol[0] == "+" else pol

    def __repr__(self):
        return "Polynomial" + str(tuple(self.__cfs))

    def __getitem__(self, i: int):
        return self.__cfs[i]

    def __setitem__(self, i: int, value: float):
        self.__cfs[i] = float(value)

    def __add__(self, other):
        if isinstance(other, Polynomial):
            min_deg = min(self.degree(), other.degree())
            pol = ([self.__cfs[i] + other.__cfs[i] for i in range(min_deg+1)] +
               [i for i in self.__cfs[min_deg + 1:]] + [i for i in other.__cfs[min_deg + 1:]])
            return Polynomial(*pol)
        elif isinstance(other, (int, float)):
            return Polynomial(*[self.__cfs[0] + other if i == 0 else
                                self.__cfs[i] for i in range(len(self.__cfs))])
        else:
            return NotImplemented

    def __radd__(self, other):
        if type(other) in (int, float):
            return Polynomial(*[self.__cfs[0] + other if i == 0 else
                                self.__cfs[i] for i in range(len(self.__cfs))])
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, (Polynomial, int, float)):
            return self+(-other)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return self+(-other)
        else:
            return NotImplemented

    def __neg__(self):
        return Polynomial(*[-i for i in self.__cfs])

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            pol = [(self.__cfs[i] * other.__cfs[j], i+j)
                   for i in range(len(self.__cfs)) for j in range(len(other.__cfs))]
            pol = [sum([a[0] if a[1] == i else 0 for a in pol]) for i in range(self.degree() + other.degree() + 1)]
            return Polynomial(*pol)
        elif isinstance(other, (int, float)):
            return Polynomial(*[other*i for i in self.__cfs])
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Polynomial(*[other * i for i in self.__cfs])
        else:
            return NotImplemented

    def degree(self):
        return len(self.__cfs) - 1

    def derivative(self):
        if len(self.__cfs) > 1:
            return Polynomial(*[self.__cfs[i]*i for i in range(1, len(self.__cfs))])
        else:
            return Polynomial(0)

    @staticmethod
    def __power_str(c, p):
        """Format potęgi do funkcji __str__"""
        return "" if c == 0 or p == 0 else f"x^{p}"

    @staticmethod
    def __cfs_str(c):
        """Format współczynnika do funkcji __str__"""
        if c == 0:
            return ""
        else:
            return str(c) if c < 0 else f"+{c}"
