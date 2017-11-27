from frame import Frame, Slot
from frame.slot_types import FramePtrList, Integer, Real, Text, Bool, Table
from .scheme import Scheme


class Component(Frame):

    _name_ = 'Электронный компонент'
    _slots_ = {
        'IS_A':     None,
        'PART_OF':  (FramePtrList(Scheme), Slot.IT_OVERRIDE),

        'name':                 ('Наименование',            Text, Slot.IT_UNIQUE),
        'is_active':            ('Активный?',               Bool, Slot.IT_UNIQUE),
        'symbolic_designation': ('Символьное обозначение',  Text, Slot.IT_UNIQUE),
        'graphic_designation':  ('Графическое обозначение', Text, Slot.IT_UNIQUE),
    }

    def __repr__(self):
        return '<{} "{}">'.format(self._frame_name, self.symbolic_designation)


class ActiveComponent(Component):

    _name_ = 'Активный компонент'
    _slots_ = {
        'IS_A':      (FramePtrList(Component), Slot.IT_UNIQUE),
        'is_active': ('Активный?', Bool(True), Slot.IT_SAME),
    }


class PassiveComponent(Component):

    _name_ = 'Пассивный компонент'
    _slots_ = {
        'IS_A':      (FramePtrList(Component),  Slot.IT_UNIQUE),
        'is_active': ('Активный?', Bool(False), Slot.IT_SAME),
    }


class Diod(ActiveComponent):

    _name_ = 'Диод'
    _slots_ = {
        'IS_A': (FramePtrList(ActiveComponent), Slot.IT_SAME),

        'vac':                      ('ВАХ',                              Table, Slot.IT_UNIQUE),
        'operating_switching_freq': ('Рабочая частота переключения, Гц', Real,  Slot.IT_UNIQUE),
    }


class Transistor(ActiveComponent):

    _name_ = 'Транзистор'
    _slots_ = {
        'IS_A': (FramePtrList(ActiveComponent), Slot.IT_SAME),

        'transition_type':                         ('Тип перехода',                 Text, Slot.IT_OVERRIDE),
        'current_transfer_ratio':                  ('Коэффициент передачи по току', Real, Slot.IT_UNIQUE),
        'reverse_collector_current':               ('Обратный ток коллектора, А',   Real, Slot.IT_UNIQUE),
        'input_resistance':                        ('Входное сопротивление, Ом',    Real, Slot.IT_UNIQUE),
        'limit_freq_base_current_transfer_factor': ('Предельная частота коэффициента '
                                                    'передачи тока базы, Гц',       Real, Slot.IT_UNIQUE),
    }


class Resistor(PassiveComponent):

    _name_ = 'Резистор'
    _slots_ = {
        'IS_A': (FramePtrList(ActiveComponent), Slot.IT_SAME),

        'rated_resistance':             ('Номинальное сопротивление, Ом',           Integer, Slot.IT_UNIQUE),
        'limiting_operating_voltage':   ('Предельное рабочее напряжение, В',        Real,    Slot.IT_UNIQUE),
        'resistance_temperature_coeff': ('Температурный коэффициент сопротивления', Real,    Slot.IT_UNIQUE),
    }

    def __repr__(self):
        return '< {} "{}" ({} Ом)>'.format(self._frame_name, self.name.value, self.rated_resistance.value)


class Capacitor(PassiveComponent):

    _name_ = 'Конденсатор'
    _slots_ = {
        'IS_A': (FramePtrList(ActiveComponent), Slot.IT_SAME),

        'capacity':          ('Ёмкость',                Integer, Slot.IT_UNIQUE),
        'specific_capacity': ('Удельная ёмкость',       Real,    Slot.IT_UNIQUE),
        'rated_voltage':     ('Номинальное напряжение', Real,    Slot.IT_UNIQUE),
    }

    def __repr__(self):
        return '< {} "{}" ({} мкФ)>'.format(self._frame_name, self.name.value, self.capacity.value)


class Inductance(PassiveComponent):

    _name_ = 'Катушка индуктивности'
    _slots_ = {
        'IS_A': (FramePtrList(ActiveComponent), Slot.IT_SAME),

        'inductance':      ('Индуктивность, Гн',        Integer, Slot.IT_UNIQUE),
        'loss_resistance': ('Сопротивление потерь, Ом', Real,    Slot.IT_UNIQUE),
        'q_factor':        ('Добротность',              Real,    Slot.IT_UNIQUE),
    }
