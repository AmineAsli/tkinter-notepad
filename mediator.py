from abc import ABC

class Mediator(ABC):
    
    def notify(self, sender, event, payload):
        pass