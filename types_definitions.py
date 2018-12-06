from enum import Enum, auto

class Selection_type(Enum):
    PROPORTIONAL = auto()
    RANKING_LINEAR = auto()
    RANKING_NON_LINEAR = auto()
    TOURNAMENT = auto()
    THRESHOLD = auto()

class Crossover_type(Enum):
    OX = auto()
    PMX = auto()
    OX_PMX = auto()

class Mutation_type(Enum):
    SWAP = auto()
    SHIFT = auto()
    SHUFFLE = auto()

class Succession_type(Enum):
    ELITE = auto()
    CLEAN = auto()

