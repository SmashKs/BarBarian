from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class TestData:
    name: str = 'jieyi'
    longitude: float = 33.2
    latitude: float = 11.3
