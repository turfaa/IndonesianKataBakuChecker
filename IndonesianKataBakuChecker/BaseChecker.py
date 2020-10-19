class BaseChecker:
    def __init__(self, desc):
        self.checkerDescription = desc;

    def check(self, text):
        print("Method 'check' not implemented")

class ErrorMessage:
    def __init__(self, checker, original, message):
        self.checkerDescription = checker.checkerDescription
        self.original = original
        self.message = message
