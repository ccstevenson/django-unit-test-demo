from django.db import models
from abc import ABCMeta, abstractmethod


class Game(models.Model):
    pass


class Scenario(models.Model):
    game = models.ForeignKey(Game)


class Encounter(models.Model):
    scenario = models.ForeignKey(Scenario)


class Player(models.Model):
    name = models.CharField(max_length=25)


class Character(models.Model):
    health = models.IntegerField()
    max_health = models.IntegerField()
    attack_damage = models.IntegerField()

    class Meta:
        abstract = True

    @abstractmethod
    def attack(self, target):
        """Later, characters will attack in different ways depending on their types/weapons.
        Because of this, we'll leave the implementation up to the derived classes."""
        pass


class Monster(Character):
    encounter = models.ForeignKey(Encounter)

    class Meta:
        abstract = True


class PlayerCharacter(Character):
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Player)

    class Meta:
        abstract = True


class WildRat(Monster):
    def attack(self, target):
        target.health -= self.attack_damage


class RatKing(Monster):
    def attack(self, target):
        target.health -= self.attack_damage


class Warrior(PlayerCharacter):
    def attack(self, target):
        target.health -= self.attack_damage


class Mage(PlayerCharacter):
    def attack(self, target):
        target.health -= self.attack_damage

