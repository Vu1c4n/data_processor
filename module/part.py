class Part:
    name:str = None
    centers:[str] = None
    content:str = None
    src:[str] = None # Remain None 
    
    def __init__(self, name) -> None:
        self.name = name