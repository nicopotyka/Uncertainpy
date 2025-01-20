class Support:
    def __init__(self, supporter, supported, weight=1) -> None:
        self.supporter = supporter
        self.supported = supported
        self.weight = weight

    def get_supporter(self):
        return self.supporter

    def get_supported(self):
        return self.supported

    def get_weight(self):
        return self.weight

    def __repr__(self) -> str:
        return f"Support({self.supporter}, {self.supported}, weight={self.weight})"

    def __str__(self) -> str:
        return (
            f"Support by {self.supporter} to {self.supported} with weight {self.weight}"
        )
