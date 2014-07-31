from django.test import TestCase
from models import *

class GameSetup(TestCase):
    def _create_game(self):
        self.game = Game.objects.create()

    def _create_scenario(self):
        self._create_game()
        self.scenario = Scenario.objects.create(game=self.game)

    def _create_encounter(self):
        self._create_scenario()
        self.encounter = Encounter.objects.create(scenario=self.scenario)

    def _create_player(self):
        self.player = Player.objects.create(name='Chris')

    def _create_player_character(self):
        self._create_player()
        self.player_character = Warrior.objects.create(health=30, max_health=30, game=self.game, player=self.player,
                                                       attack_damage=6)

    def _create_monster(self):
        self._create_encounter()
        self.monster = WildRat.objects.create(health=20, max_health=20, encounter=self.encounter, attack_damage=4)

    def _create_characters(self):
        self._create_monster()
        self._create_player_character()

    def setUp(self):
        self._create_characters()


class EncounterTest(GameSetup):
    def setUp(self):
        """To test a player attacking a monster, a game must first be set up."""
        super(EncounterTest, self).setUp()

    def test_combat(self):
        """Tests that attack arithmetic is correct."""
        player_character = Warrior.objects.get(id=1)
        self.assertEqual(player_character.health, player_character.max_health)

        enemy = WildRat.objects.get(id=1)
        self.assertEqual(enemy.health, enemy.max_health)

        print "\nBefore attack: warrior health: %s, rat health: %s" % (player_character.health, enemy.health)

        player_character.attack(enemy)

        self.assertEqual(enemy.health, enemy.max_health - player_character.attack_damage)

        print "After attack: warrior health: %s, rat health: %s\n" % (player_character.health, enemy.health)
