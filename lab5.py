from math import gcd


class Rational:
    def __init__(self, n, d=1):
        if isinstance(n, str):
            if '/' in n:
                parts = n.split('/')
                self._n = int(parts[0])
                self._d = int(parts[1])
            else:
                self._n = int(n)
                self._d = 1
        elif isinstance(n, Rational):
            self._n = n._n
            self._d = n._d
        else:
            self._n = n
            self._d = d

        self.reduce()

    def reduce(self):
        if self._d == 0:
            raise ValueError()
        g = gcd(self._n, self._d)
        self._n = self._n // g
        self._d = self._d // g
        if self._d < 0:
            self._n = -self._n
            self._d = -self._d

    def __str__(self):
        if self._d == 1:
            return str(self._n)
        return f"{self._n}/{self._d}"

    def __repr__(self):
        return f'Rational("{self._n}/{self._d}")'

    def __call__(self):
        return self._n / self._d

    def __getitem__(self, key):
        if key == "n":
            return self._n
        if key == "d":
            return self._d
        raise KeyError()

    def __setitem__(self, key, value):
        if key == "n":
            self._n = value
        elif key == "d":
            self._d = value
        self.reduce()

    def ensure_rational(self, other):
        if isinstance(other, int):
            return Rational(other)
        return other

    def __add__(self, other):
        other = self.ensure_rational(other)
        return Rational(self._n * other._d + self._d * other._n, self._d * other._d)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = self.ensure_rational(other)
        return Rational(self._n * other._d - self._d * other._n, self._d * other._d)

    def __rsub__(self, other):
        other = self.ensure_rational(other)
        return other - self

    def __mul__(self, other):
        other = self.ensure_rational(other)
        return Rational(self._n * other._n, self._d * other._d)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = self.ensure_rational(other)
        return Rational(self._n * other._d, self._d * other._n)

    def __rtruediv__(self, other):
        other = self.ensure_rational(other)
        return other / self


if __name__ == "__main__":
    with open("input01.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            elements = line.split()
            res = []
            for el in elements:
                if el in "+-*/":
                    res.append(el)
                else:
                    res.append(f'Rational("{el}")')

            expr = " ".join(res)
            result = eval(expr)

            print(line)
            print(result)
            print(result())
            print("-" * 30)