"""03 — Metaclasses (Introduction)"""

# type() creates classes dynamically
Dog = type("Dog", (), {"species": "Canis", "speak": lambda self: "Woof!"})
dog = Dog()
print(f"{Dog.__name__}: {dog.speak()}")

# Metaclass controls class creation
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("  Initializing Database connection...")

db1 = Database()
db2 = Database()
print(f"Same instance: {db1 is db2}")

# Register subclasses automatically
class PluginMeta(type):
    registry = {}

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        if name != "Plugin":
            PluginMeta.registry[name] = cls

class Plugin(metaclass=PluginMeta):
    pass

class EmailPlugin(Plugin):
    def run(self):
        return "Sending email"

class LogPlugin(Plugin):
    def run(self):
        return "Writing log"

print(f"\nRegistered plugins: {list(PluginMeta.registry.keys())}")
for name, cls in PluginMeta.registry.items():
    print(f"  {name}: {cls().run()}")

# When to use metaclasses:
# - Frameworks (Django ORM, SQLAlchemy)
# - Enforcing interfaces on subclasses
# - Most apps should use simpler patterns instead
