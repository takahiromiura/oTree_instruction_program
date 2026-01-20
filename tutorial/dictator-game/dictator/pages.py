from otree.api import Page, WaitPage
from .models import C


class Introduction(Page):
    pass


class Offer(Page):
    form_model = "group"
    form_fields = ["allocated_amount"]

    def is_displayed(self):
        return self.player.role == C.DICTATOR_ROLE


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for player in self.group.get_players():
            player.set_payoff()


class Results(Page):
    pass


page_sequence = [Introduction, Offer, ResultsWaitPage, Results]
