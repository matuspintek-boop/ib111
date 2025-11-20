class Polynomial:
    def __init__(self, coefs: list[int]) -> None:
        self.coefs = coefs.copy()
        self.coefs.reverse()
        self.normalize()

    def normalize(self) -> None:
        while len(self.coefs) > 1 and not self.coefs[-1]:
            self.coefs.pop()

    def add(self, other: 'Polynomial') -> 'Polynomial':
        result = Polynomial([])
        result.coefs = [0 for _ in range(max(len(self.coefs),
                                             len(other.coefs)))]

        for i in range(len(self.coefs)):
            result.coefs[i] += self.coefs[i]

        for i in range(len(other.coefs)):
            result.coefs[i] += other.coefs[i]

        return result

    def invert(self) -> 'Polynomial':
        result = Polynomial([])
        result.coefs = [-x for x in self.coefs]
        return result

    def subtract(self, other: 'Polynomial') -> 'Polynomial':
        return self.add(other.invert())

    def multiply(self, other: 'Polynomial') -> 'Polynomial':
        result = Polynomial([])
        result.coefs = [0 for i in range(len(self.coefs) *
                                         len(other.coefs))]

        for i in range(len(self.coefs)):
            for j in range(len(other.coefs)):
                result.coefs[i + j] += self.coefs[i] * other.coefs[j]

        result.normalize()
        return result

    def get_coefs(self) -> list[int]:
        coefs = self.coefs.copy()
        coefs.reverse()
        return coefs
