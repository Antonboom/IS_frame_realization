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
            if params is None:
                continue

            if attr_name in Slot.SYSTEMS_NAMES:
                name, value, inheritance_type = attr_name, params[0], params[1]
            else:
                name, value, inheritance_type = params[0], params[1], params[2]

            slot = self._get_slot(name, value, inheritance_type)
            setattr(self, attr_name, slot)

    def _collect_slots(self):
        parents = self.__class__.__mro__
        for parent in parents:
            if parent not in (self.__class__, object):
                self._slots_.update(parent._slots_)

    @staticmethod
    def _get_slot(name, value, inheritance_type):
        return (
            Slot(name=name, _type=value, inheritance_type=inheritance_type)
            if inspect.isclass(value) else
            Slot(name=name, _type=value.__class__, value=value, inheritance_type=inheritance_type)
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

    # -*- Указатели наследования -*-
    # Значение слота наследуется
    IT_SAME = 'SAME'
    # Значение слота не наследуется
    IT_UNIQUE = 'UNIQUE'
    # При отсутствии значения в текущем слоте оно наследуется из фрейма верхнего уровня,
    # однако в случае определения значения текущего слота оно может быть уникальным
    IT_OVERRIDE = 'OVERRIDE'

    def __init__(self, name, _type, inheritance_type=None, value=None):
        """
        :type name: str
        :type _type: frame.slot_types.SlotType
        """
        self._name = name
        self._type = _type
        self._inheritance_type = inheritance_type
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
