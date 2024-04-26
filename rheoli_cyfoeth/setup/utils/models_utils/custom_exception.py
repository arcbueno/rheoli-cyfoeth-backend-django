from dataclasses import dataclass
from typing import Dict

@dataclass
class CustomException:
    message: Dict
    status_code: int