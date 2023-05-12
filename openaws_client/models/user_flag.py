from enum import IntEnum


class UserFlag(IntEnum):
    VALUE_2 = 2

    def __str__(self) -> str:
        return str(self.value)
