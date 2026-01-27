from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.Card import Card, Card_Rarity, Creatures, Spells, Artifacts
from random import randint, choice
from icecream import ic


class FantasyCardFactory(CardFactory):

    rarity_list = [rare.value for rare in Card_Rarity]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:

        return CreatureCard(
            name=name_or_power,
            cost=randint(1, 5),
            rarity=FantasyCardFactory.rarity_list[
                randint(0, len(FantasyCardFactory.rarity_list) - 1)
                ],
            attack=randint(1, 3),
            health=randint(5, 10)
        )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:

        return SpellCard(
            name=name_or_power,
            cost=randint(1, 5),
            rarity=FantasyCardFactory.rarity_list[
                randint(0, len(FantasyCardFactory.rarity_list) - 1)
                ],
            effect_type="spell??"
        )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:

        return ArtifactCard(
            name=name_or_power,
            cost=randint(1, 5),
            rarity=FantasyCardFactory.rarity_list[
                randint(0, len(FantasyCardFactory.rarity_list) - 1)
                ],
            durability=randint(1, 3),
            effect="artifact???"
        )

    def create_themed_deck(self, size: int) -> dict:
        self.deck = Deck()  # Dependency injection

        n_creatures = int(round(size * 0.6, ndigits=0))
        n_spells = int(round(size * 0.2, ndigits=0))
        n_artifacts = int(size - n_creatures - n_spells)

        for _ in range(0, n_creatures):
            self.deck.add_card(self.create_creature(choice(list(Creatures)).value))
        for _ in range(0, n_spells):
            self.deck.add_card(self.create_spell(choice(list(Spells)).value))
        for _ in range(0, n_artifacts):
            self.deck.add_card(self.create_artifact(choice(list(Artifacts)).value))

        self.my_deck = {}
        self.my_deck["creatures"] = [card.name for card in self.deck.my_cards if isinstance(card, CreatureCard)]
        self.my_deck["spells"] = [card.name for card in self.deck.my_cards if isinstance(card, SpellCard)]
        self.my_deck["artifacts"] = [card.name for card in self.deck.my_cards if isinstance(card, ArtifactCard)]

        return self.my_deck


    def get_supported_types(self) -> dict:
        ...
