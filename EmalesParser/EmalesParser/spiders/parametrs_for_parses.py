from dataclasses import dataclass


@dataclass
class ParamsForParser:
    name: str
    url: str
    allowed_domains: str
    item_link: str
    pagen: str
    item_header: dict
