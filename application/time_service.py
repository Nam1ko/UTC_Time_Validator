import re
from datetime import datetime

from domain.utc_timestamp import UtcTimestamp

class TimeService:

    UTC_PATTERN = (
        r"\b\d{4}-(?:0[1-9]|1[0-2])-"
        r"(?:0[1-9]|[12]\d|3[01])T"
        r"(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\dZ\b"
    )

    def validate(self, value):
        if not re.fullmatch(self.UTC_PATTERN, value):
            return False
        try:
            datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
            return True
        except ValueError:
            return False

    def search(self, text):
        matches = re.finditer(self.UTC_PATTERN, text)
        timestamps = []

        for match in matches:
            value = match.group()
            if self.validate(value):
                timestamps.append(UtcTimestamp(value))

        return timestamps