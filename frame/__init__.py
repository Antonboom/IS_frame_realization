import inspect


__author__ = 'Anton Telishev'

__all__ = ('Frame', 'Slot')


class Frame:
    """
    Фрейм
    """
    _name_ = 'Фрейм'
    _slots_ = {}

    def __init__(self, name=None):
        self._collect_slots()
        self._frame_name = name or self._name_

        for attr_name, params in self._slots_.items():
            if isinstance(params, (list, tuple)):
                slot = self._get_slot(params[0], params[1])
                setattr(self, attr_name, slot)

            else:
                slot = self._get_slot(attr_name, params)
                setattr(self, attr_name, slot)

    def _collect_slots(self):
        parents = self.__class__.__mro__
        for parent in parents:
            if parent not in (self.__class__, object):
                self._slots_.update(parent._slots_)

    @staticmethod
    def _get_slot(name, value):
        return (
            Slot(name=name, _type=value)
            if inspect.isclass(value) else
            Slot(name=name, _type=value.__class__, value=value)
        )

    @property
    def title(self):
        return self._frame_name


class Slot:
    """
    Слот
    """
    # Имена системных слотов
    SYSTEMS_NAMES = ('IS_A', 'PART_OF')

    # Указатель наследования
    IT_UNIQUE = 'UNIQUE'
    IT_RANGE = 'RANGE'
    IT_SAME = 'SAME'
    INHERITANCE_TYPES = (IT_UNIQUE, IT_RANGE, IT_SAME)

    def __init__(self, name, _type, inheritance_type=None, value=None):
        """
        :type name: str
        :type _type: frame.slot_types.SlotType
        """
        self._name = name
        self._type = _type
        self._value = value or self._type()

    def __getattr__(self, attr):
        return getattr(self._value, attr)

    def __iter__(self):
        return iter(self._value)

    @property
    def is_system(self):
        return self._name in self.SYSTEMS_NAMES

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value and self._value.value

    # noinspection PyCallingNonCallable
    @value.setter
    def value(self, value):
        self._value = self._type(value)

    @property
    def type(self):
        return self._type
