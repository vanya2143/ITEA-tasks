# Реализовать пример использования паттерна Singleton
from random import choice


# Генератор событий
def gen_events(instance, data, count=2):
    for i in range(count):
        event = choice(data)
        instance.add_event(f'Event-{event}-{i}', event)


# Singleton на примере списка событий
class EventsMeta(type):
    _instance = None

    def __call__(cls):
        if cls._instance is None:
            cls._instance = super().__call__()
        return cls._instance


class Events(metaclass=EventsMeta):
    # __metaclass__ = EventsMeta

    _events = {
        'ok': [],
        'info': [],
        'warn': [],
        'error': []
    }

    def get_all_events(self):
        """
        :return: dict with all events and types
        """
        return self._events

    def get_events_count(self, key: str = None):
        """
        :param key: if need count of specific type
        :return: all events count or specific event count if param key: not None
        :rtype: tuple, int
        """
        if key:
            try:
                return len(self._events[key])
                # return key, len(self._events[key])
            except KeyError:
                print('Тип события должен быть ' + ', '.join(self._events.keys()))
                return

        return tuple((event, len(self._events[event])) for event in self._events.keys())

    def add_event(self, event: str, event_type: str):
        """
        :param event: event message
        :param event_type: ok, info, warn, error
        :return: None
        """
        try:
            self._events[event_type].append(event)
        except KeyError:
            print('Тип события должен быть ' + ', '.join(self._events.keys()))

    def read_event(self, event_type: str):
        """
        :param event_type: ok, info, warn, error
        :return: tuple last item of event_type, all count events or None
        """
        try:
            return self._events[event_type].pop(), len(self._events[event_type])
        except IndexError:
            print('Событий больше нет')
            return
        except KeyError:
            print('Указан неверный тип события')
            return

    # Для генератора ))
    @classmethod
    def get_events_types(cls):
        return cls._events.keys()


if __name__ == '__main__':
    event_instance1 = Events()
    event_instance2 = Events()
    event_instance3 = Events()

    print(type(event_instance1), id(event_instance1))
    print(type(event_instance2), id(event_instance2))

    # Генерируем события
    gen_events(event_instance3, list(event_instance3.get_events_types()), 50)

    # Получаем все события
    print(event_instance2.get_all_events())

    # Получаем колличества всех типов событий и обределенного типа
    print(event_instance3.get_events_count())
    print(f"Error: {event_instance3.get_events_count('error')}")

    # Читаем события
    while event_instance3.get_events_count('ok'):
        print(event_instance3.read_event('ok'))
