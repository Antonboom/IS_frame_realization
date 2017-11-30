from inspect import isclass


__author__ = 'Anton Telishev'

__all__ = ('Frame', 'Slot')


class Frame:
    """
    Фрейм
    """
    _name_ = 'Фрейм'
    _slots_ = {}

    def __init__(self, name=None, **slot_values):
        self.__slots = dict(self._slots_)
        self._collect_slots()
        self._frame_name = name or self._name_

        for attr_name, params in self.__slots.items():
            if params is None:
                continue
            slot = Slot(*self._get_slot_args(attr_name, params))

            if slot.inheritance_type != Slot.IT_SAME and attr_name in slot_values:
                slot.value = slot_values[attr_name]

            setattr(self, attr_name, slot)
        pass

    def _collect_slots(self):
        parents = self.__class__.__mro__
        for parent in reversed(parents):
            if parent not in (self.__class__, object, type):
                self.__slots.update(parent._slots_)
                for slot_attr, params in parent._slots_.items():
                    if not params:
                        continue
                    name, value, inheritance_type = self._get_slot_args(slot_attr, params)

                    if inheritance_type == Slot.IT_UNIQUE:
                        self.__slots[slot_attr] = (
                            (value.__class__(), inheritance_type)
                            if name in Slot.SYSTEMS_NAMES else
                            (name, value.__class__(), inheritance_type)
                        )

    @staticmethod
    def _get_slot_args(name, params):
        if name in Slot.SYSTEMS_NAMES:
            return name, params[0], params[1]
        return params[0], params[1], params[2]

    @property
    def title(self):
        return self._frame_name

    def serialize(self):
        return {
            attr: getattr(self, attr).value
            for attr in dir(self)
            if isinstance(getattr(self, attr), Slot)
        }

    @classmethod
    def deserialize(cls, data):
        """
        :type data: dict
        """
        frame = cls()

        for key, value in data.items():
            getattr(frame, key).value = value

        return frame


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

    def __init__(self, name, value, inheritance_type):
        self._name = name
        self._type = value.__class__
        self._inheritance_type = inheritance_type
        self._value = value

    def __getattr__(self, attr):
        return getattr(self._value, attr)

    def __iter__(self):
        return iter(self._value)

    @property
    def is_system(self):
        return self._name in self.SYSTEMS_NAMES

    @property
    def inheritance_type(self):
        return self._inheritance_type

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value.value

    # noinspection PyCallingNonCallable
    @value.setter
    def value(self, value):
        self._value.value = value

    @property
    def type(self):
        return self._type
