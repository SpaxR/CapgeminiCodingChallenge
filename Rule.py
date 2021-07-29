from abc import ABC, abstractmethod


class Rule(ABC):
    """Class for the rules of evaluation of current office state"""

    # checks whether for a given rule current state is optimal
    @abstractmethod
    def state_optimal(self, rooms, building):
        pass

    # gives out list of strings on how to change
    @abstractmethod
    def path_to_opt(self, rooms, building):
        pass
