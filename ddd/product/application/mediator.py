class Mediator:
    def __init__(self):
        self.handlers = {}

    def register(self, command_type, handler):
        self.handlers[command_type] = handler

    def execute(self, command):
        handler = self.handlers.get(type(command))
        if handler:
            return handler.execute(command)
        else:
            raise ValueError("No handler found for the command")


mediator = Mediator()