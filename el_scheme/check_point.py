from frame import Frame
from frame.slot_types import FramePtrList, Text, Real
from .scheme import Scheme


class CheckPoint(Frame):

    _name_ = 'Контрольная точка'
    _slots_ = {
        'IS_A':     None,
        'PART_OF':  FramePtrList(Scheme),

        'name':                 ('Наименование', Text),
        'permissible_voltage':  ('Допустимое напряжение, В', Real),
        'error':                ('Погрешность', Real),
    }
