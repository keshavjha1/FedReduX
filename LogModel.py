# Create a model to store the elements of the list
class LogModel:
    def __init__(self, log_level, timestamp, device, component, log_message, json):
        self.log_level = log_level
        self.timestamp = timestamp
        self.device = device
        self.component = component
        self.log_message = log_message
        self.json = json

