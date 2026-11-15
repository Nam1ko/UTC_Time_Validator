from dataclasses import dataclass

@dataclass(frozen=True)
class UtcTimestamp:
    value: str

    def __str__(self):
        return self.value