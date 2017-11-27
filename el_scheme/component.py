from frame import Frame
from frame.slot_types import FramePtrList, Integer, Real, Text, Bool, Table
from .scheme import Scheme


class Component(Frame):

    _name_ = 'Электронный компонент'
    _slots_ = {
        'IS_A':     None,
        'PART_OF':  FramePtrList(Scheme),

        'name':                 ('Наименование', Text),
        'is_active':            ('Активный?', Bool),
        'symbolic_designation': ('Символьное обозначение', Text),
        'graphic_designation':  ('Графическое обозначение', Text),
    }

    def __repr__(self):
        return '<{} "{}">'.format(self._frame_name, self.symbolic_designation)


class ActiveComponent(Component):

    _name_ = 'Активный компонент'
    _slots_ = {
        'IS_A': FramePtrList(Component),
        'is_active': ('Активный?', Bool(True)),
    }


class PassiveComponent(Component):

    _name_ = 'Пассивный компонент'
    _slots_ = {
        'IS_A': FramePtrList(Component),
        'is_active': ('Активный?', Bool(False)),
    }


class Diod(ActiveComponent):

    _name_ = 'Диод'
    _slots_ = {
        'IS_A': FramePtrList(ActiveComponent),

        'vac':                      ('ВАХ', Table),
        'operating_switching_freq': ('Рабочая частота переключения, Гц', Real),
    }


class Transistor(ActiveComponent):

    _name_ = 'Транзистор'
    _slots_ = {
        'IS_A': FramePtrList(ActiveComponent),

        'transition_type':                         ('Тип перехода', Text),
        'current_transfer_ratio':                  ('Коэффициент передачи по току', Real),
        'reverse_collector_current':               ('Обратный ток коллектора, А', Real),
        'input_resistance':                        ('Входное сопротивление, Ом', Real),
        'limit_freq_base_current_transfer_factor': ('Предельная частота коэффициента передачи тока базы, Гц', Real),
    }


class Resistor(PassiveComponent):

    _name_ = 'Резистор'
    _slots_ = {
        'IS_A': FramePtrList(PassiveComponent),

        'rated_resistance':             ('Номинальное сопротивление, Ом', Integer),
        'limiting_operating_voltage':   ('Предельное рабочее напряжение, В', Real),
        'resistance_temperature_coeff': ('Температурный коэффициент сопротивления', Real),
    }

    def __repr__(self):
        return '< {} "{}" ({} Ом)>'.format(self._frame_name, self.name.value, self.rated_resistance.value)


class Capacitor(PassiveComponent):

    _name_ = 'Конденсатор'
    _slots_ = {
        'IS_A': FramePtrList(PassiveComponent),

        'capacity':          ('Ёмкость', Integer),
        'specific_capacity': ('Удельная ёмкость', Real),
        'rated_voltage':     ('Номинальное напряжение', Real),
    }

    def __repr__(self):
        return '< {} "{}" ({} мкФ)>'.format(self._frame_name, self.name.value, self.capacity.value)


class Inductance(PassiveComponent):

    _name_ = 'Катушка индуктивности'
    _slots_ = {
        'IS_A': FramePtrList(PassiveComponent),

        'inductance':      ('Индуктивность, Гн', Integer),
        'loss_resistance': ('Сопротивление потерь, Ом', Real),
        'q_factor':        ('Добротность', Real),
    }