from icecream import ic

class Connection:

    def __init__(self, father: str, son: str, max_link_cap: int) -> None:
        self.father = father
        self.son = son
        self.max_link_cap = max_link_cap


