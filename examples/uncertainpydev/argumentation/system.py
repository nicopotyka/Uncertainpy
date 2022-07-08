class System:
    def __init__(self, model=None, approximation=None, BAG=None) -> None:
        self.model = model
        self.approximation = approximation
        self.BAG = BAG

    def __str__(self) -> str:
        return f"System with:\nmodel {self.model}\napproximation {self.approximation}\nBAG {self.BAG}"

    def __repr__(self) -> str:
        return f"System({self.model}, {self.approximation}, {self.BAG})"