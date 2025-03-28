import logging
import math
from typing import List

from boxing.models.boxers_model import Boxer, update_boxer_stats
from boxing.utils.logger import configure_logger
from boxing.utils.api_utils import get_random


logger = logging.getLogger(__name__)
configure_logger(logger)


class RingModel:
    """
    A class that models a fight between 2 boxers. 
    """
    def __init__(self):
        """
        Constructor for an instance of RingModel. Makes a list that contains Boxer objects. 
        """
        self.ring: List[Boxer] = []

    def fight(self) -> str:
        """
        Initiate a fight between 2 boxers. Choose a winner and update the boxer's records based on the results of the fight. 
        Clear the ring to prepare it for the next fight. 

        Raises:
            ValueError: If there aren't enough boxers to start the fight (must have two). 

        Returns:
            str: The name of the winning boxer. 
        """
        if len(self.ring) < 2:
            raise ValueError("There must be two boxers to start a fight.")

        boxer_1, boxer_2 = self.get_boxers()

        skill_1 = self.get_fighting_skill(boxer_1)
        skill_2 = self.get_fighting_skill(boxer_2)

        # Compute the absolute skill difference
        # And normalize using a logistic function for better probability scaling
        delta = abs(skill_1 - skill_2)
        normalized_delta = 1 / (1 + math.e ** (-delta))

        random_number = get_random()

        if random_number < normalized_delta:
            winner = boxer_1
            loser = boxer_2
        else:
            winner = boxer_2
            loser = boxer_1

        update_boxer_stats(winner.id, 'win')
        update_boxer_stats(loser.id, 'loss')

        self.clear_ring()

        return winner.name

    def clear_ring(self):
        """
        Check if the ring is empty and clear it if it isn't. 
        """
        if not self.ring:
            return
        self.ring.clear()

    def enter_ring(self, boxer: Boxer):
        """
        Add a boxer to the ring. 

        Args:
            boxer (Boxer): Boxer that needs to be added to the ring. 

        Raises:
            TypeError: If trying to add anything other than an object of type Boxer. 
            ValueError: If the ring alredy contains two boxers. 
        """
        if not isinstance(boxer, Boxer):
            raise TypeError(f"Invalid type: Expected 'Boxer', got '{type(boxer).__name__}'")

        if len(self.ring) >= 2:
            raise ValueError("Ring is full, cannot add more boxers.")

        self.ring.append(boxer)

    def get_boxers(self) -> List[Boxer]:
        """
        Return a list representation of the boxing ring. 

        Returns:
            List[Boxer]: A list of the current boxers in the ring. 
        """
        if not self.ring:
            pass
        else:
            pass

        return self.ring

    def get_fighting_skill(self, boxer: Boxer) -> float:
        """
        Calculate the skill of a boxer based on some arbitrary metrics. 

        Args:
            boxer (Boxer): The boxer you want to get the skill level for. 

        Returns:
            float: Skill number. 
        """
        # Arbitrary calculations
        age_modifier = -1 if boxer.age < 25 else (-2 if boxer.age > 35 else 0)
        skill = (boxer.weight * len(boxer.name)) + (boxer.reach / 10) + age_modifier

        return skill
