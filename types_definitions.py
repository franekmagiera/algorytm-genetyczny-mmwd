from enum import Enum, auto


class Selection_type(Enum):
    PROPORTIONATE = auto()
    TOURNAMENT = auto()
    TRUNCATION = auto()


class Crossover_type(Enum):
    OX = auto()
    PMX = auto()
    OX_PMX = auto()


class Mutation_type(Enum):
    SWAP = auto()
    INVERSION = auto()
    SCRAMBLE = auto()

