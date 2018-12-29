from enum import Enum, auto


class SelectionType(Enum):
    PROPORTIONATE = auto()
    TOURNAMENT = auto()
    TRUNCATION = auto()


class CrossoverType(Enum):
    OX = auto()
    PMX = auto()
    OX_PMX = auto()


class MutationType(Enum):
    SWAP = auto()
    INVERSION = auto()
    SCRAMBLE = auto()


class SuccessionType(Enum):
    CHILDREN_ONLY = auto()
    MIXED = auto()

