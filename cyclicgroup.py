# Operator overloading
# Practice using the __add__ method

from __future__ import annotations

class Dummy:
    # Dummy class used in testing
    def __init__(self):
        self.mod = 421
        self.val = 70

class CyclicGroupElement:
    def __init__(self, val: int, mod: int):
        self.mod = mod
        self.val = val

    def __add__(self, other: CyclicGroupElement) -> CyclicGroupElement:
        # Check other is of CyclicGroupElement class
        try:
            assert isinstance(other, CyclicGroupElement)

        except AssertionError:
            raise TypeError(f"Unsupported operand types: {type(self)} and {type(other)}")

        # Check other is from the same group
        try:
            assert other.mod == self.mod

        except AssertionError:
            raise TypeError(f"Objects from different groups: C{self.mod} and C{other.mod}")

        # Calculate
        new_val = (self.val + other.val) % self.mod

        return CyclicGroupElement(new_val, self.mod)


##
fake = Dummy()
h7 = CyclicGroupElement(7, 12)
g2 = CyclicGroupElement(2, 5)
g3 = CyclicGroupElement(3, 5)

##
print((g2+g3).val)

##
print((g2 + fake).val)

##
print((g2 + h7).val)
