import threading


class Singleton:
    instance = None
    lock = threading.RLock()

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        # 返回空对象
        if cls.instance:
            return cls.instance

        with cls.lock:
            if cls.instance:
                return cls.instance
            cls.instance = object.__new__(cls)
            return cls.instance


obj1 = Singleton("Goin")
print(obj1)
obj2 = Singleton("Sophie")
print(obj2)
