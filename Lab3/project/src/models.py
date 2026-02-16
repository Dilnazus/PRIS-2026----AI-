from dataclasses import dataclass
from typing import List


@dataclass
class Disease:
    name: str
    symptoms: List[str]
    medicines: List[str]
    severity: float = 0.0

    def __str__(self):
        return f"{self.name} (Симптомы: {', '.join(self.symptoms)})"
