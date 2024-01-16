"""Print out some stuff from the settings."""
import sys

print(sys.path)

from pkg_shared.settings import CAPTAIN_BLACK

print(CAPTAIN_BLACK.app_name)
print(CAPTAIN_BLACK.redis_address)
print(CAPTAIN_BLACK.greeting)
