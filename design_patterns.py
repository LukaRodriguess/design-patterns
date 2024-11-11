class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            print("Opening database connection...")
        return cls._instance


class FileSystemComponent:
    def display(self):
        pass


class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"File: {self.name}")


class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.components = []

    def add(self, component):
        self.components.append(component)

    def display(self):
        print(f"Folder: {self.name}")
        for component in self.components:
            component.display()


class SupportHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle_request(self, request):
        pass


class Level1Support(SupportHandler):
    def handle_request(self, request):
        if request == "basic":
            print("Level 1: Handling basic support issue.")
        elif self.next_handler:
            self.next_handler.handle_request(request)


class Level2Support(SupportHandler):
    def handle_request(self, request):
        if request == "intermediate":
            print("Level 2: Handling intermediate support issue.")
        elif self.next_handler:
            self.next_handler.handle_request(request)


class Level3Support(SupportHandler):
    def handle_request(self, request):
        if request == "advanced":
            print("Level 3: Handling advanced support issue.")
        elif self.next_handler:
            self.next_handler.handle_request(request)


print("Testing Singleton Pattern:")
conn1 = DatabaseConnection()
conn2 = DatabaseConnection()
print()

print("Testing Composite Pattern:")
file1 = File("Document.txt")
file2 = File("Image.png")
folder = Folder("Documents")
folder.add(file1)
folder.add(file2)
folder.display()
print()

print("Testing Chain of Responsibility Pattern:")
level1 = Level1Support()
level2 = Level2Support(level1)
level3 = Level3Support(level2)

level3.handle_request("intermediate")
