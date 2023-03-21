from enum import IntEnum


class UserFlag(IntEnum):
    VALUE_0 = 0
    VALUE_2 = 2
    VALUE_1026 = 1026
    VALUE_1049602 = 1049602
    VALUE_1125899907892226 = 1125899907892226
    VALUE_NEGATIVE_1 = -1

    def __str__(self) -> str:
        return str(self.value)
