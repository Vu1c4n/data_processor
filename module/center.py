class Center:
    name:str = None
    content:str = None
    src:[str] = None # Remain None
    url:str = None # Remain None
    part:str = None
    def __init__(self, name) -> None:
        self.name = name