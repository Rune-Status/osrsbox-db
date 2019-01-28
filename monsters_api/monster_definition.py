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

import os
import json
import datetime
import collections

from monsters_api import monster_stats


def _str_cast(val):
    """Convert value to string."""
    if not val:
        return None
    return str(val)


def _int_cast(val):
    """Convert input to integer."""
    if not val:
        return None
    return int(val)


def _float_cast(val):
    """Convert input to float."""
    if not val:
        return None
    return float(val)


def _bool_cast(val):
    """Convert value to boolean object."""
    if not val:
        return None
    return bool(val)


def _date_cast(val):
    """Check date by converting to datetime object, and convert back to str."""
    if not val:
        return None
    date = datetime.datetime.strptime(val, "%d %B %Y")
    return date.strftime("%d %B %Y")


def _list_cast(val):
    """Check and convert to a list."""
    if not val:
        return None
    return list(val)


class MonsterDefinition:
    """This class defines the object structure and properties for an OSRS monster.

    Attributes:
        monster_id (int) = The ID number of the monster.
        name (str) = The name of the monster.
        members (bool) = If the monster is members only, or not.
        release_date (:obj:`datetime`) = The release date of the monster.
        combat_level (int) = The combat level of the monster.
        examine (str) = The text when examining the monster.
        hit_points (int) = The hit points of the monster.
        max_hit (int) = The maximum hit of the monster.
        aggressive (bool) = If the monster is aggressive, or not.
        poison (bool) = If the monsters poisons, or not.
        weakness (:obj:`list`) = A list of monster weaknesses.
        attack_type (str) = The attack type of the monster.
        attack_style (str) = The attack stype of the monster.
        url (str) = The OSRS Wiki URL of the monster.
        monster_stats (:obj:`MonsterStats`) = An object that represents the stats of the monster.
        json_out (:obj:`OrderedDict`) = All class attributes stored in a dictionary
    """
    def __init__(self):
        self.properties = {
            "monster_id": None,
            "name": None,
            "members": None,
            "release_date": None,
            "combat_level": None,
            "examine": None,
            "hit_points": None,
            "max_hit": None,
            "aggressive": None,
            "poison": None,
            "weakness": None,
            "attack_type": None,
            "attack_style": None,
            "url": None}

        self.monster_id = None
        self.name = None
        self.members = None
        self.release_date = None
        self.combat_level = None
        self.examine = None
        self.hit_points = None
        self.max_hit = None
        self.aggressive = None
        self.poison = None
        self.weakness = None
        self.attack_type = None
        self.attack_style = None
        self.url = None

        self.monster_stats = monster_stats.MonsterStats()

        self.json_out = collections.OrderedDict()

    # Setters and Getters for each monster property
    @property
    def monster_id(self):
        """Get the ID number of the monster."""
        return self._monster_id

    @monster_id.setter
    def monster_id(self, value):
        self._monster_id = _int_cast(value)

    @property
    def name(self):
        """Get the name of the monster."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = _str_cast(value)

    @property
    def members(self):
        """Get if the monster is members only, or not."""
        return self._members

    @members.setter
    def members(self, value):
        self._members = _bool_cast(value)

    @property
    def release_date(self):
        """Get the release date of the monster."""
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        self._release_date = _bool_cast(value)

    @property
    def combat_level(self):
        """Get the combat level of the monster."""
        return self._combat_level

    @combat_level.setter
    def combat_level(self, value):
        self._combat_level = _int_cast(value)

    @property
    def examine(self):
        """Get the monster examine text."""
        return self._examine

    @examine.setter
    def examine(self, value):
        self._examine = _str_cast(value)

    @property
    def hit_points(self):
        """Get the hit points of the monster."""
        return self._hit_points

    @hit_points.setter
    def hit_points(self, value):
        self._hit_points = _int_cast(value)

    @property
    def max_hit(self):
        """Get the max hit of the monster."""
        return self._max_hit

    @max_hit.setter
    def max_hit(self, value):
        self._max_hit = _int_cast(value)

    @property
    def aggressive(self):
        """Get if the monster is aggressive, or not."""
        return self._aggressive

    @aggressive.setter
    def aggressive(self, value):
        self._aggressive = _bool_cast(value)

    @property
    def poison(self):
        """Get if the monster poisons, or not."""
        return self._poison

    @poison.setter
    def poison(self, value):
        self._poison = _bool_cast(value)

    @property
    def weakness(self):
        """Get a list of weaknesses of the monster."""
        return self._weakness

    @weakness.setter
    def weakness(self, value):
        self._weakness = _list_cast(value)

    @property
    def attack_type(self):
        """Get the attack type of the monster."""
        return self._attack_type

    @attack_type.setter
    def attack_type(self, value):
        self._attack_type = _str_cast(value)

    @property
    def attack_style(self):
        """Get the attack style of the monster."""
        return self._attack_style

    @attack_style.setter
    def attack_style(self, value):
        self._attack_style = _str_cast(value)

    @property
    def url(self):
        """Get the OSRS Wiki URL of the monster."""
        return self._url

    @url.setter
    def url(self, value):
        self._url = _str_cast(value)

    def load_monster_definition_from_file(self, monster_data):
        """Load a MonsterDefinition object from an existing JSON file.

        Args:
             monster_data (:obj:`dict`) = TODO
        """
        # Load all monster properties from this class
        for prop in self.properties:
            setattr(self, prop, monster_data[prop])

        # Load all monster stat properties from the MonsterStats class
        monster_data_stats = monster_data["stats"]
        self.monster_stats.monster_data = monster_data_stats
        self.monster_stats.load_monster_stats_from_file()

    def print_json(self, pretty):
        """Output Monster to console.

        Args:
            pretty (bool) = Toggles pretty (indented) JSON output.
        """
        self.construct_json()
        if pretty:
            json_obj = json.dumps(self.json_out, indent=4)
        else:
            json_obj = json.dumps(self.json_out)
        print(json_obj)

    def export_json(self, pretty):
        """Output Monster to JSON file.

        Args:
            pretty (bool) = Toggles pretty (indented) JSON output.
        """
        self.construct_json()
        out_file_name = str(self.monster_id) + ".json"
        out_file_path = os.path.join("items-json", out_file_name)
        with open(out_file_path, "w") as out_file:
            if pretty:
                json.dump(self.json_out, out_file, indent=4)
            else:
                json.dump(self.json_out, out_file)

    def construct_json(self):
        """Construct dictionary/JSON for exporting or printing.

        Returns:
            json_out (:obj:`OrderedDict`) = All class attributes stored in a dictionary
        """
        self.json_out["monster_id"] = self.monster_id
        self.json_out["name"] = self.name
        self.json_out["members"] = self.members
        self.json_out["release_date"] = self.release_date
        self.json_out["combat_level"] = self.combat_level
        self.json_out["examine"] = self.examine
        self.json_out["hit_points"] = self.hit_points
        self.json_out["max_hit"] = self.max_hit
        self.json_out["aggressive"] = self.aggressive
        self.json_out["poison"] = self.poison
        self.json_out["weakness"] = self.weakness
        self.json_out["attack_type"] = self.attack_type
        self.json_out["attack_style"] = self.attack_style
        self.json_out["url"] = self.url
        self.json_out["stats"] = self.monster_stats

        return self.json_out
