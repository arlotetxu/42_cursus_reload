from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    Class representing an elite card that combines combat and magical
    abilities.
    """

    def attack(self, target: Card) -> dict:
        """
        Perform an attack on a target card.

        Args:
            target (Card): The target card to attack.

        Returns:
            dict: A dictionary containing the results of the attack.
        """
        attack_info: dict = {}

        attack_info["attacker"] = self.name
        attack_info["target"] = target.name
        attack_info["damage"] = self._attack
        attack_info["combat_type"] = self.combat_type
        # try:
        #     target.set_health(target.get_health() - self._attack)
        # except (ValueError) as v_e:
        #     raise ValueError(v_e)

        return attack_info

    def defend(self, incoming_damage: int) -> dict:
        """
        Defend against incoming damage using block value.

        Args:
            incoming_damage (int): The amount of damage to defend against.

        Returns:
            dict: A dictionary containing the results of the defense.
        """

        defense_info: dict = {}

        defense_info["defender"] = self.name
        damage = incoming_damage - self.block
        self._health -= damage
        defense_info["damage_taken"] = damage
        defense_info["damage_block"] = self.block
        alive = True if self._health > 0 else False
        defense_info["still_alive"] = alive

        return defense_info

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """
        Cast a spell on multiple targets.

        Args:
            spell_name (str): The name of the spell to cast.
            targets (list): A list of target cards.

        Returns:
            dict: A dictionary containing the results of the spell cast.
        """
        spell_info: dict = {}

        spell_info["caster"] = self.name
        spell_info["spell"] = spell_name
        spell_info["targets"] = [target.name for target in targets]
        spell_info["mana_used"] = self.cost

        return spell_info

    def channel_mana(self, amount: int) -> dict:
        """
        Channel mana to increase the total mana pool.

        Args:
            amount (int): The amount of mana to channel.

        Returns:
            dict: A dictionary containing the results of the mana channeling.
        """
        mana_info: dict = {}

        mana_info["channeled"] = amount
        mana_info["total_mana"] = self.mana + amount

        return mana_info

    def play(self, game_state: dict) -> dict:
        """
        Play the elite card and update the game state.

        Args:
            game_state (dict): The current state of the game.

        Returns:
            dict: The updated game state.
        """
        ...

    def get_combat_stats(self) -> dict:
        """
        Get the combat-related statistics of the elite card.

        Returns:
            dict: A dictionary containing combat statistics.
        """
        ...

    def get_magic_stats(self) -> dict:
        """
        Get the magic-related statistics of the elite card.

        Returns:
            dict: A dictionary containing magic statistics.
        """
        ...
