"""
10 — Metaclasses (Introduction)

THEORY
------
What: A metaclass is the class of a class — it controls how classes are created, like
      type() or a custom metaclass overriding __call__ or __init__.
Why:  Frameworks use metaclasses for registration, singletons, and interface enforcement.
Key rules:
  - type(name, bases, namespace) creates a class dynamically.
  - Metaclass __call__ intercepts instance creation (Singleton pattern).
  - Metaclass __init__ runs when a subclass is defined (plugin registry).
When to use: ORM model registration, plugin systems, enforcing API contracts — rarely in app code.
Common mistakes: Overusing metaclasses when decorators or __init_subclass__ suffice;
                 metaclass conflicts with multiple inheritance; debugging difficulty.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/10_metaclasses_intro.py
"""


class SingletonMeta(type):  # metaclass ensuring one instance per class
    _instances = {}  # cache of singleton instances by class

    def __call__(cls, *args, **kwargs):  # intercept instance construction
        if cls not in cls._instances:  # create instance only once per class
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]  # return cached singleton instance


class Database(metaclass=SingletonMeta):  # class using singleton metaclass
    def __init__(self):  # expensive one-time initialization
        print("  Initializing Database connection...")


class PluginMeta(type):  # metaclass that registers concrete plugin subclasses
    registry = {}  # mapping of plugin name to class

    def __init__(cls, name, bases, namespace):  # run when each class is created
        super().__init__(name, bases, namespace)  # standard class initialization
        if name != "Plugin":  # skip abstract base class itself
            PluginMeta.registry[name] = cls  # register concrete plugin class


class Plugin(metaclass=PluginMeta):  # base plugin class with auto-registration
    pass


class EmailPlugin(Plugin):  # concrete email plugin
    def run(self):  # execute plugin action
        return "Sending email"


class LogPlugin(Plugin):  # concrete logging plugin
    def run(self):  # execute plugin action
        return "Writing log"


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — type() creates classes dynamically")  # section header
    print("=" * 50)  # close header divider
    Dog = type("Dog", (), {"species": "Canis", "speak": lambda self: "Woof!"})  # runtime class
    dog = Dog()  # instantiate dynamically created class
    print(f"{Dog.__name__}: {dog.speak()}")  # call method on dynamic instance

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Singleton metaclass")  # section header
    print("=" * 50)  # close header divider
    db1 = Database()  # first construction runs __init__
    db2 = Database()  # second call returns same instance without re-init
    print(f"Same instance: {db1 is db2}")  # verify identity equality

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Plugin registry metaclass")  # section header
    print("=" * 50)  # close header divider
    print(f"Registered plugins: {list(PluginMeta.registry.keys())}")  # show registered names
    for name, cls in PluginMeta.registry.items():  # iterate registered plugin classes
        print(f"  {name}: {cls().run()}")  # instantiate and run each plugin


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
