from enum import IntEnum


class StatusFlag(IntEnum):
    VALUE_0 = 0
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_NEGATIVE_1 = -1

    def __str__(self) -> str:
        return str(self.value)
