"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
A Python script to build the monster database using the data extracted
from the OSRS Wiki and OSRS client cache data.

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

from monsters_api import monster_definition


# This will be the primary entry point for building the monster database
# Need to dump OSRS Wiki content before continuing development
print("Starting")
md = monster_definition.MonsterDefinition()
print(md)
print(md.aggressive)
ms = monster_definition.monster_stats.MonsterStats()
print(ms)
print(ms.attack_accuracy)

PRIMARY_CATEGORY = "monster"
TEXT_FILE_NAME = "extract_page_text" + PRIMARY_CATEGORY + ".json"
TEXT_FILE_PATH = os.path.join("extraction_tools_wiki", TEXT_FILE_NAME)
