"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Copyright (c) 2019, PH01L

###############################################################################
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
"""

import collections


def _int_cast(val):
    """Convert input to integer."""
    if not val:
        return None
    return int(val)


def _str_cast(val):
    """Convert value to string."""
    if not val:
        return None
    return str(val)


class MonsterStats:
    """This class defines the object structure and stats for an OSRS monster.

    Attributes:
        attack_level (int) = The attack level of the monster.
        strength_level (int) = The strength level of the monster.
        defence_level (int) = The defence level of the monster.
        magic_level (int) = The magic level of the monster.
        ranged_level (int) = The ranged level of the monster.
        attack_stab (int) = The stab attack bonus of the monster.
        attack_slash (int) = The slash attack bonus of the monster.
        attack_crush (int) = The crush attack bonus of the monster.
        attack_magic (int) = The magic attack bonus of the monster.
        attack_ranged (int) = The ranged attack bonus of the monster.
        defence_stab (int) = The stab defence bonus of the monster.
        defence_slash (int) = The slash defence bonus of the monster.
        defence_crush (int) = The crush defence bonus of the monster.
        defence_magic (int) = The magic defence bonus of the monster.
        defence_ranged (int) = The ranged defence bonus of the monster.
        attack_accuracy (int) = The attack accuracy bonus of the monster.
        melee_strength (int) = The melee strength bonus of the monster.
        ranged_strength (int) = The ranged strength bonus of the monster.
        magic_damage (int) = The magic damage bonus of the monster.
        json_out (:obj:`OrderedDict`) = All class attributes stored in a dictionary
    """
    def __init__(self):
        self.properties = [
            "attack_level",
            "strength_level",
            "defence_level",
            "magic_level",
            "ranged_level",
            "attack_stab",
            "attack_slash",
            "attack_crush",
            "attack_magic",
            "attack_ranged",
            "defence_stab",
            "defence_slash",
            "defence_crush",
            "defence_magic",
            "defence_ranged",
            "attack_accuracy",
            "melee_strength",
            "ranged_strength",
            "magic_damage"]

        self.attack_level = None
        self.strength_level = None
        self.defence_level = None
        self.magic_level = None
        self.ranged_level = None
        self.attack_stab = None
        self.attack_slash = None
        self.attack_crush = None
        self.attack_magic = None
        self.attack_ranged = None
        self.defence_stab = None
        self.defence_slash = None
        self.defence_crush = None
        self.defence_magic = None
        self.defence_ranged = None
        self.attack_accuracy = None
        self.melee_strength = None
        self.ranged_strength = None
        self.magic_damage = None

        self.monster_data = dict()
        self.json_out = collections.OrderedDict()

    # Setters and Getters for combat levels
    @property
    def attack_level(self):
        """Get the attack level of the monster."""
        return self._attack_level

    @attack_level.setter
    def attack_level(self, value):
        self._attack_level = _int_cast(value)

    @property
    def strength_level(self):
        """Get the strength level of the monster."""
        return self._strength_level

    @strength_level.setter
    def strength_level(self, value):
        self._strength_level = _int_cast(value)

    @property
    def defence_level(self):
        """Get the defence level of the monster."""
        return self._defence_level

    @defence_level.setter
    def defence_level(self, value):
        self._defence_level = _int_cast(value)

    @property
    def magic_level(self):
        """Get the magic level of the monster."""
        return self._magic_level

    @magic_level.setter
    def magic_level(self, value):
        self._magic_level = _int_cast(value)

    @property
    def ranged_level(self):
        """Get the ranged level of the monster."""
        return self._ranged_level

    @ranged_level.setter
    def ranged_level(self, value):
        self._ranged_level = _int_cast(value)

    # Setters and Getters for attacking stats
    @property
    def attack_stab(self):
        """Get the stab attack bonus of the monster."""
        return self._attack_stab

    @attack_stab.setter
    def attack_stab(self, value):
        self._attack_stab = _int_cast(value)

    @property
    def attack_slash(self):
        """Get the slash attack bonus of the monster."""
        return self._attack_slash

    @attack_slash.setter
    def attack_slash(self, value):
        self._attack_slash = _int_cast(value)

    @property
    def attack_crush(self):
        """Get the crush attack bonus of the monster."""
        return self._attack_crush

    @attack_crush.setter
    def attack_crush(self, value):
        self._attack_crush = _int_cast(value)

    @property
    def attack_magic(self):
        """Get the magic attack bonus of the monster."""
        return self._attack_magic

    @attack_magic.setter
    def attack_magic(self, value):
        self._attack_magic = _int_cast(value)

    @property
    def attack_ranged(self):
        """Get the ranged attack bonus of the monster."""
        return self._attack_ranged

    @attack_ranged.setter
    def attack_ranged(self, value):
        self._attack_ranged = _int_cast(value)

    # Setters and Getters for defensive stats
    @property
    def defence_stab(self):
        """Get the stab defence bonus of the monster."""
        return self._defence_stab

    @defence_stab.setter
    def defence_stab(self, value):
        self._defence_stab = _int_cast(value)

    @property
    def defence_slash(self):
        """Get the slash defence bonus of the monster."""
        return self._defence_slash

    @defence_slash.setter
    def defence_slash(self, value):
        self._defence_slash = _int_cast(value)

    @property
    def defence_crush(self):
        """Get the crush defence bonus of the monster."""
        return self._defence_crush

    @defence_crush.setter
    def defence_crush(self, value):
        self._defence_crush = _int_cast(value)

    @property
    def defence_magic(self):
        """Get the magic defence bonus of the monster."""
        return self._defence_magic

    @defence_magic.setter
    def defence_magic(self, value):
        self._defence_magic = _int_cast(value)

    @property
    def defence_ranged(self):
        """Get the ranged defence bonus of the monster."""
        return self._defence_ranged

    @defence_ranged.setter
    def defence_ranged(self, value):
        self._defence_ranged = _int_cast(value)

    # Setters and Getters for bonus stats
    @property
    def attack_accuracy(self):
        """Get the attack accuracy bonus of the monster."""
        return self._attack_accuracy

    @attack_accuracy.setter
    def attack_accuracy(self, value):
        self._attack_accuracy = _int_cast(value)

    @property
    def melee_strength(self):
        """Get the melee strength bonus of the monster."""
        return self._melee_strength

    @melee_strength.setter
    def melee_strength(self, value):
        self._melee_strength = _int_cast(value)

    @property
    def ranged_strength(self):
        """Get the ranged strength bonus of the monster."""
        return self._ranged_strength

    @ranged_strength.setter
    def ranged_strength(self, value):
        self._ranged_strength = _int_cast(value)

    @property
    def magic_damage(self):
        """Get the magic damage bonus of the monster."""
        return self._magic_damage

    @magic_damage.setter
    def magic_damage(self, value):
        self._magic_damage = _int_cast(value)

    def load_monster_stats_from_file(self):
        """Load a MonsterDefinition object from an existing JSON file.

        Args:
             monster_data (:obj:`dict`) = TODO
        """
        # Load all monster properties from this class
        for prop in self.properties:
            setattr(self, prop, self.monster_data[prop])

    def construct_json(self):
        """Construct dictionary/JSON for exporting or printing.

        Returns:
            json_out (:obj:`OrderedDict`) = All class attributes stored in a dictionary
        """
        self.json_out["attack_level"] = self.attack_level
        self.json_out["strength_level"] = self.strength_level
        self.json_out["defence_level"] = self.defence_level
        self.json_out["magic_level"] = self.magic_level
        self.json_out["ranged_level"] = self.ranged_level
        self.json_out["attack_stab"] = self.attack_stab
        self.json_out["attack_slash"] = self.attack_slash
        self.json_out["attack_crush"] = self.attack_crush
        self.json_out["attack_magic"] = self.attack_magic
        self.json_out["attack_ranged"] = self.attack_ranged
        self.json_out["defence_stab"] = self.defence_stab
        self.json_out["defence_slash"] = self.defence_slash
        self.json_out["defence_crush"] = self.defence_crush
        self.json_out["defence_magic"] = self.defence_magic
        self.json_out["defence_ranged"] = self.defence_ranged
        self.json_out["attack_accuracy"] = self.attack_accuracy
        self.json_out["melee_strength"] = self.melee_strength
        self.json_out["ranged_strength"] = self.ranged_strength
        self.json_out["magic_damage"] = self.magic_damage
        return self.json_out
