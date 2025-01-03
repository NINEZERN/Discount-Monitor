class Product:
    def __init__(self, current_price: float, old_price: float, discount_percent: int, store: str, title: str, description: str) -> None:
        self.current_price = current_price
        self.old_price = old_price
        self.discount_percent = discount_percent
        self.store = store
        self.title = title
        self.description = description

    def __repr__(self) -> str:
        return f"{self.title}\n {self.current_price} {self.old_price} -{self.discount_percent}% | {self.store}\n{self.description}"
