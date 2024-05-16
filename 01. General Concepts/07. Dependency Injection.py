class Logger:
    def log(self, message):
        raise NotImplementedError("Subclasses must implement this method")

# ConsoleLogger implementation of Logger
class ConsoleLogger(Logger):
    def log(self, message):
        print(f"ConsoleLogger: {message}")

# Service that depends on a logger
class Service:
    def __init__(self, logger: Logger):
        self.logger = logger

    def perform_task(self):
        self.logger.log("Performing a task")

if __name__ == "__main__":
    # Injecting ConsoleLogger dependency into Service
    logger = ConsoleLogger()
    service = Service(logger)
    service.perform_task()
