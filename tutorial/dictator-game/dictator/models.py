from otree.api import BaseConstants, BaseSubsession, BaseGroup, BasePlayer, models


class C(BaseConstants):
    NAME_IN_URL = "choice_task"
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    DICTATOR_ROLE = "dictator"
    RECEIVER_ROLE = "receiver"

    INITIAL_ENDOWMENTS = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    allocated_amount = models.IntegerField(
        min=0,
        max=C.INITIAL_ENDOWMENTS,  # 10
    )


class Player(BasePlayer):

    def set_payoff(self):
        allocated_amount = self.group.allocated_amount
        if self.role == C.DICTATOR_ROLE:
            self.payoff = C.INITIAL_ENDOWMENTS - allocated_amount

        else:
            self.payoff = allocated_amount
