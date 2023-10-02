from dataclasses import dataclass

@dataclass
class Immutable:
    value1: str = "Value1"
    value2: int = 0


obj = Immutable()
print(obj.value1)