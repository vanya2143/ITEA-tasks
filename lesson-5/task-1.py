# Реализовать пример использования паттерна Singleton


# Список событий
class EventsMeta(type):
    _instance = None

    def __call__(cls):
        if cls._instance is None:
            cls._instance = super().__call__()
        return cls._instance


class Events(metaclass=EventsMeta):
    # __metaclass__ = EventsMeta

    _events_list: list = []

    def add_event(self, event):
        self._events_list.append(event)

    def get_all_events(self):
        return self._events_list

    def read_event(self):
        try:
            return self._events_list.pop()
        except IndexError:
            return


if __name__ == '__main__':

    e1 = Events()
    e2 = Events()
    e3 = Events()

    # print(type(e1), id(e1))
    # print(type(e2), id(e2))

    e1.add_event("test1")
    e1.add_event("test2")
    e2.add_event("test3")
    e3.add_event("test4")
    # e2.get_all_events()

    print(e2.read_event())
    print(e2.read_event())
    print(e2.read_event())
    print(e2.read_event())
    print(e2.read_event())

    print(dir(e1))
