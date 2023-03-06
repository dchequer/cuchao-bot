"""
Loads bot configuration from YAML files.
By default, this simply loads the default
configuration located at `config-default.yml`.
However, if a file named `config.yml` is found
in the same directory, it will be loaded and
used to update the default configuration.

"""

from collections.abc import Mapping
from enum import Enum
from pathlib import Path
from typing import List, Callable
import yaml
import os


with open('config-default.yml', encoding='UTF-8') as f:
    _CONFIG_YAML = yaml.safe_load(f)


def _recursive_update(original, new):
    '''
    Helper method which implements a recursive `dict.update`
    method, used for updating the original configuration with
    configuration specified by the user.
    '''

    for key, value in original.items():
        if key not in new:
            continue

        if isinstance(value, Mapping):
            if not any(isinstance(subvalue, Mapping) for subvalue in value.values()):
                original[key].update(new[key])
            _recursive_update(original[key], new[key])
        else:
            original[key] = new[key]

if Path("config.yml").exists():
    print("Found `config.yml` file, loading constants from it.")
    with open("config.yml", encoding="UTF-8") as f:
        user_config = yaml.safe_load(f)
    _recursive_update(_CONFIG_YAML, user_config)


def check_required_keys(keys):
    '''
    Verifies that keys that are set to be required are present in the
    loaded configuration.
    '''
    for key_path in keys:
        lookup = _CONFIG_YAML
        try:
            for key in key_path.split('.'):
                lookup = lookup[key]
                if lookup is None:
                    raise KeyError(key)
        except KeyError:
            raise KeyError(
                f"A configuration for `{key_path}` is required, but was not found. "
                "Please set it in `config.yml` or setup an environment variable and try again."
            )

'''
try:
    required_keys = _CONFIG_YAML['config']['required_keys']
except KeyError:
    pass
else:
    check_required_keys(required_keys)
'''

# The following constants are loaded from the configuration file.
# If you wish to change any of these, you should update the
# `config.yml` file instead of changing them here.

class YAMLGetter(type):
    '''
    Implements a custom metaclass used for accessing
    configuration data by simply accessing class attributes.
    Supports getting configuration from up to two levels
    of nested configuration through `section` and `subsection`.
    `section` specifies the YAML configuration section (or "key")
    in which the configuration lives, and must be set.
    `subsection` is an optional attribute specifying the section
    within the section from which configuration should be loaded.
    
    '''

    subsection = None

    def __getattr__(cls, name):
        name = name.lower()

        try:
            if cls.subsection is not None:
                return _CONFIG_YAML[cls.section][cls.subsection][name]
            return _CONFIG_YAML[cls.section][name]
        except KeyError as e:
            raise AttributeError(f"Configuration value `{name}` not found.") from e
        
    def __setattr__(cls, name, value):
        name = name.lower()

        try:
            if cls.subsection is not None:
                _CONFIG_YAML[cls.section][cls.subsection][name] = value
            else:
                _CONFIG_YAML[cls.section][name] = value
        except KeyError as e:
            raise AttributeError(f"Configuration value `{name}` not found.") from e
    
    def __getitem__(cls, name):
        return cls.__getattr__(name)

    def __iter__(cls):
        '''Return generator of key: value pairs'''
        for name in cls.__annotations__:
            yield name, getattr(cls, name)

# The following classes are used to access configuration data.

# Dataclasses
class Bot(metaclass=YAMLGetter):
    section = 'bot'

    prefix: str
    token: str
    description: str

    status: str
    #presence: List[str]

class Colours(metaclass=YAMLGetter):
    section = 'style'
    subsection = 'colours'

    blue: int
    bright_green: int
    orange: int
    pink: int
    purple: int
    soft_green: int
    soft_orange: int
    soft_red: int
    white: int
    yellow: int

class Emojis(metaclass=YAMLGetter):
    section = 'style'
    subsection = 'emojis'

    agucatatito: str
    pixel_number_one: str
    pixel_number_two: str
    pixel_number_three: str
    pixel_number_four: str
    pixel_number_five: str
    pixel_number_six: str
    pixel_number_seven: str
    goldstar: str
    Villager_Question_What: str
    lock: str
    kheverga: str
    info: str
    overwatch: str

    # animated
    GreenCheckMark: str
    black_and_white_tick: str
    AGENT_Warning: str
    Warning: str
    tick_red: str

class Categories(metaclass=YAMLGetter):
    section = 'guild'
    subsection = 'categories'

    stats: int
    admin: int
    lobby: int
    info: int
    text: int
    voice: int

    overwatch: int

class Channels(metaclass=YAMLGetter):
    section = 'guild'
    subsection = 'channels'

    # General
    rules: int
    announcements: int
    tourney: int
    welcome: int

    # LFT
    lft: int

    # support
    support: int

class Roles(metaclass=YAMLGetter):
    section = 'guild'
    subsection = 'roles'

    # staff team
    leader: int
    staff: int
    developer: int
    mod: int

    # content team
    editor: int
    content_creator: int
    caster: int
    tester: int

    # bots
    pepe: int
    bots: int

    # player type
    contender: int
    player: int

    # game roles
    overwatch: int

class Guild(metaclass=YAMLGetter):
    section = 'guild'

    id: int
    name: str
    invite: str

    moderation_roles: List[int]

class Events(Enum):
    '''
    Defines constants for the different types of events
    that can be triggered by the bot.
    '''
    guild_channel_create = 'guild_channel_create'
    guild_channel_delete = 'guild_channel_delete'
    guild_channel_update = 'guild_channel_update'
    guild_role_create = 'guild_role_create'
    guild_role_delete ='"guild_role_delete'
    guild_role_update = 'guild_role_update'
    guild_update = 'guild_update'

    member_join = 'member_join'
    member_remove = 'member_remove'
    member_ban = 'member_ban'
    member_unban = 'member_unban'
    member_update = 'member_update'

    message_delete = 'message_delete'
    message_edit = 'message_edit'

    voice_state_update = 'voice_state_update'

class Cogs(Enum):
    '''
    Defines constants for the different cogs that can be
    loaded and unloaded by the bot.
    '''
    Help: str = 'Help'
    Tournaments: str = 'Tournaments'
    #general = 'general'
    #help = 'help'
    #info = 'info'
    #moderation = 'moderation'
    #owner = 'owner'
    #stats = 'stats'

    # lft = 'lft'
    # support = 'support'

# Default role IDs for the guild.
MODERATION_ROLES = Guild.moderation_roles

NEGATIVE_REPLIES = [
    'No',
    'Nope',
    'Nah',
    'Nyet',
    'Nuh-uh',
    'No way',
    'That\'s a negative'
]

POSITIVE_REPLIES = [
    'Yes',
    'Yep',
    'Yeah',
    'Yup',
    'Affirmative',
    'Roger that',
    'That\'s affirmative',
    'That\'s a positive'
]

ERROR_REPLIES = [
    'Uh oh',
    'Oh no',
    'Oh dear',
    'That\'s not very poggers'
]