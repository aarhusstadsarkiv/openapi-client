from enum import IntEnum


class StatusFlag(IntEnum):
    VALUE_2 = 2
    VALUE_4 = 4

    def __str__(self) -> str:
        return str(self.value)
