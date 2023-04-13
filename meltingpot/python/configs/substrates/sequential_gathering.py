from typing import Any, Dict, Mapping, Sequence

from ml_collections import config_dict

from meltingpot.python.utils.substrates import colors
from meltingpot.python.utils.substrates import game_object_utils
from meltingpot.python.utils.substrates import shapes
from meltingpot.python.utils.substrates import specs

PrefabConfig = game_object_utils.PrefabConfig

ASCII_MAP = """
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WHHHHHHHHHHHHHHHHHHHHHHHHHHHHW
WHHHHHHHHHHHHHHHHHHHHHHHHHHHHW
WHHHHHHHHHHHHHHHHHHHHHHHHHHHHW
W==============+~fHHHHHHf====W
W   P    P      ===+~SSf     W
W     P     P   P  <~Sf  P   W
W             P   P<~S>      W
W   P    P         <~S>   P  W
W            a  P  <~S>P     W
W     P   b       P<~S>      W
W           P c    <~S> P    W
W  P             P <~S>      W
W^T^T^T^T^T^T^T^T^T;~S,^T^T^TW
WssssssssssssssssssssssssssssW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
"""
SPRITE_SIZE = 1

# Map a character to the prefab it represents in the ASCII map.
CHAR_PREFAB_MAP = {
    "W": "wall",
    " ": "sand",
    "P": {"type": "all", "list": ["sand", "spawn_point"]},
    "s": {"type": "all", "list": ["grass", "shadow_n"]},
    "+": {"type": "all", "list": ["sand", "shadow_e", "shadow_n"]},
    "f": {"type": "all", "list": ["sand", "shadow_w", "shadow_n"]},
    ";": {"type": "all", "list": ["sand", "grass_edge", "shadow_e"]},
    ",": {"type": "all", "list": ["sand", "grass_edge", "shadow_w"]},
    "^": {"type": "all", "list": ["sand", "grass_edge",]},
    "=": {"type": "all", "list": ["sand", "shadow_n",]},
    ">": {"type": "all", "list": ["sand", "shadow_w",]},
    "<": {"type": "all", "list": ["sand", "shadow_e",]},
    "~": {"type": "all", "list": ["river", "shadow_w",]},
    "T": {"type": "all", "list": ["sand", "grass_edge"]},
    "S": "river",
    "H": {"type": "all", "list": ["river"]},
    "a": "target_0",
    "b": "target_1",
    "c": "target_2",
}

_COMPASS = ["N", "E", "S", "W"]

SAND = {
    "name": "sand",
    "components": [
        {
            "component": "StateManager",
            "kwargs": {
                "initialState": "sand",
                "stateConfigs": [{
                    "state": "sand",
                    "layer": "background",
                    "sprite": "Sand",
                }],
            }
        },
        {
            "component": "Appearance",
            "kwargs": {
                "renderMode": "ascii_shape",
                "spriteNames": ["Sand"],
                "spriteShapes": [shapes.GRAINY_FLOOR],
                "palettes": [{"+": (222, 221, 189, 255),
                              "*": (219, 218, 186, 255)}],
                "noRotates": [False]
            }
        },
        {
            "component": "Transform",
        },
    ]
}

GRASS = {
    "name": "grass",
    "components": [
        {
            "component": "StateManager",
            "kwargs": {
                "initialState": "grass",
                "stateConfigs": [{
                    "state": "grass",
                    "layer": "background",
                    "sprite": "Grass",
                }],
            }
        },
        {
            "component": "Appearance",
            "kwargs": {
                "renderMode": "ascii_shape",
                "spriteNames": ["Grass"],
                "spriteShapes": [shapes.GRASS_STRAIGHT],
                "palettes": [{"*": (164, 189, 75, 255),
                              "@": (182, 207, 95, 255),
                              "x": (0, 0, 0, 0)}],
                "noRotates": [False]
            }
        },
        {
            "component": "Transform",
        },
    ]
}

GRASS_EDGE = {
    "name": "grass_edge",
    "components": [
        {
            "component": "StateManager",
            "kwargs": {
                "initialState": "grass_edge",
                "stateConfigs": [{
                    "state": "grass_edge",
                    "layer": "lowerPhysical",
                    "sprite": "GrassEdge",
                }],
            }
        },
        {
            "component": "Appearance",
            "kwargs": {
                "renderMode": "ascii_shape",
                "spriteNames": ["GrassEdge"],
                "spriteShapes": [shapes.GRASS_STRAIGHT_N_EDGE],
                "palettes": [{"*": (164, 189, 75, 255),
                              "@": (182, 207, 95, 255),
                              "x": (0, 0, 0, 0)}],
                "noRotates": [False]
            }
        },
        {
            "component": "Transform",
        },
    ]
}

SHADOW_W = {
    "name": "shadow_w",
    "components": [
        {
            "component": "StateManager",
            "kwargs": {
                "initialState": "shadow_w",
                "stateConfigs": [{
                    "state": "shadow_w",
                    "layer": "upperPhysical",
                    "sprite": "ShadowW",
                }],
            }
        },
        {
            "component": "Appearance",
            "kwargs": {
                "renderMode": "ascii_shape",
                "spriteNames": ["ShadowW"],
                "spriteShapes": [shapes.SHADOW_W],
                "palettes": [shapes.SHADOW_PALETTE],
                "noRotates": [False]
            }
        },
        {
            "component": "Transform",
        },
    ]
}

SHADOW_E = {
    "name": "shadow_e",
    "components": [
        {
            "component": "StateManager",
            "kwargs": {
                "initialState": "shadow_e",
                "stateConfigs": [{
                    "state": "shadow_e",
                    "layer": "upperPhysical",
                    "sprite": "ShadowE",
                }],
            }
        },
        {
            "component": "Appearance",
            "kwargs": {
                "renderMode": "ascii_shape",
                "spriteNames": ["ShadowE"],
                "spriteShapes": [shapes.SHADOW_E],
                "palettes": [shapes.SHADOW_PALETTE],
                "noRotates": [False]
            }
        },
        {
            "component": "Transform",
        },
    ]
}

SHADOW_N = {
    "name": "shadow_n",
    "components": [
        {
            "component": "StateManager",
            "kwargs": {
                "initialState": "shadow_n",
                "stateConfigs": [{
                    "state": "shadow_n",
                    "layer": "overlay",
                    "sprite": "ShadowN",
                }],
            }
        },
        {
            "component": "Appearance",
            "kwargs": {
                "renderMode": "ascii_shape",
                "spriteNames": ["ShadowN"],
                "spriteShapes": [shapes.SHADOW_N],
                "palettes": [shapes.SHADOW_PALETTE],
                "noRotates": [False]
            }
        },
        {
            "component": "Transform",
        },
    ]
}

WALL = {
    "name": "wall",
    "components": [
        {
            "component": "StateManager",
            "kwargs": {
                "initialState": "wall",
                "stateConfigs": [{
                    "state": "wall",
                    "layer": "superOverlay",
                    "sprite": "Wall",
                }],
            }
        },
        {
            "component": "Appearance",
            "kwargs": {
                "renderMode": "ascii_shape",
                "spriteNames": ["Wall"],
                "spriteShapes": [shapes.WALL],
                "palettes": [{"*": (95, 95, 95, 255),
                              "&": (100, 100, 100, 255),
                              "@": (109, 109, 109, 255),
                              "#": (152, 152, 152, 255)}],
                "noRotates": [False]
            }
        },
        {
            "component": "Transform",
        },
        {
            "component": "BeamBlocker",
            "kwargs": {
                "beamType": "zapHit"
            }
        },
        {
            "component": "BeamBlocker",
            "kwargs": {
                "beamType": "cleanHit"
            }
        },
    ]
}

SPAWN_POINT = {
    "name": "spawnPoint",
    "components": [
        {
            "component": "StateManager",
            "kwargs": {
                "initialState": "spawnPoint",
                "stateConfigs": [{
                    "state": "spawnPoint",
                    "layer": "logic",
                    "groups": ["spawnPoints"]
                }],
            }
        },
        {
            "component": "Transform",
        },
    ]
}

# Primitive action components.
# pylint: disable=bad-whitespace
# pyformat: disable
NOOP        = {"move": 0, "turn":  0, "fireZap": 0}
FORWARD     = {"move": 1, "turn":  0, "fireZap": 0}
STEP_RIGHT  = {"move": 2, "turn":  0, "fireZap": 0}
BACKWARD    = {"move": 3, "turn":  0, "fireZap": 0}
STEP_LEFT   = {"move": 4, "turn":  0, "fireZap": 0}
TURN_LEFT   = {"move": 0, "turn": -1, "fireZap": 0}
TURN_RIGHT  = {"move": 0, "turn":  1, "fireZap": 0}
# PICKUP      = {"move": 0, "turn":  0, "fireZap": 1}
# pyformat: enable
# pylint: enable=bad-whitespace

ACTION_SET = (
    NOOP,
    FORWARD,
    BACKWARD,
    STEP_LEFT,
    STEP_RIGHT,
    TURN_LEFT,
    TURN_RIGHT,
)

# Remove the first entry from human_readable_colors after using it for the self
# color to prevent it from being used again as another avatar color.
human_readable_colors = list(colors.human_readable)
TARGET_SPRITE_SELF = {
    "name": "Self",
    "shape": shapes.CUTE_AVATAR,
    "palette": shapes.get_palette(human_readable_colors.pop(0)),
    "noRotate": True,
}

def get_water():
  """Get an animated water game object."""
  layer = "background"
  water = {
      "name": "water_{}".format(layer),
      "components": [
          {
              "component": "StateManager",
              "kwargs": {
                  "initialState": "water_1",
                  "stateConfigs": [
                      {"state": "water_1",
                       "layer": layer,
                       "sprite": "water_1",
                       "groups": ["water"]},
                      {"state": "water_2",
                       "layer": layer,
                       "sprite": "water_2",
                       "groups": ["water"]},
                      {"state": "water_3",
                       "layer": layer,
                       "sprite": "water_3",
                       "groups": ["water"]},
                      {"state": "water_4",
                       "layer": layer,
                       "sprite": "water_4",
                       "groups": ["water"]},
                  ]
              }
          },
          {"component": "Transform",},
          {
              "component": "Appearance",
              "kwargs": {
                  "renderMode": "ascii_shape",
                  "spriteNames": ["water_1", "water_2", "water_3", "water_4"],
                  "spriteShapes": [shapes.WATER_1, shapes.WATER_2,
                                   shapes.WATER_3, shapes.WATER_4],
                  "palettes": [{
                      "@": (66, 173, 212, 255),
                      "*": (35, 133, 168, 255),
                      "o": (34, 129, 163, 255),
                      "~": (33, 125, 158, 255),}] * 4,
              }
          },
          {
              "component": "Animation",
              "kwargs": {
                  "states": ["water_1", "water_2", "water_3", "water_4"],
                  "gameFramesPerAnimationFrame": 2,
                  "loop": True,
                  "randomStartFrame": True,
                  "group": "water",
              }
          },
      ]
  }
  return water

def get_sequential_pickup(lua_idx: int) -> Dict[str, Any]:
    prefab = {
        "name": "sequential_pickup",
        "components": [
            {
                "component": "StateManager",
                "kwargs": {
                    "initialState": "active",
                    "stateConfigs": [{
                        "state": "active",
                        "layer": "background",
                        "sprite": "Active",
                    }],
                }
            },
            {
                "component": "Appearance",
                "kwargs": {
                    "renderMode": "ascii_shape",
                    "spriteNames": ["Active"],
                    "spriteShapes": [shapes.DIAMOND],
                    "palettes": [{
                                    "x": (0, 0, 0, 0),
                                    "a": (252, 252, 252, 255),
                                    "b": (255, 0, 0, 255),
                                    "c": (155, 0, 0, 255),
                                    "d": (255, 0, 0, 255)
                                }],
                    "noRotates": [False]
                }
            },
            {
                "component": "Transform",
            },
            {
                "component": "PickUp",
                "kwargs": {"idx": lua_idx}
            },
        ]
    }
    return prefab


def create_prefabs() -> PrefabConfig:
  """Returns the prefabs.

  Prefabs are a dictionary mapping names to template game objects that can
  be cloned and placed in multiple locations accoring to an ascii map.
  """
  prefabs = {
      "wall": WALL,
      "sand": SAND,
      "grass": GRASS,
      "grass_edge": GRASS_EDGE,
      "shadow_w": SHADOW_W,
      "shadow_e": SHADOW_E,
      "shadow_n": SHADOW_N,
      "spawn_point": SPAWN_POINT,
      "river": get_water(),
      "target_0": get_sequential_pickup(lua_idx=1),
      "target_1": get_sequential_pickup(lua_idx=2),
      "target_2": get_sequential_pickup(lua_idx=3),
  }
  return prefabs


def create_scene():
  """Create the scene object, a non-physical object to hold global logic."""
  scene = {
      "name": "scene",
      "components": [
          {
              "component": "StateManager",
              "kwargs": {
                  "initialState": "scene",
                  "stateConfigs": [{
                      "state": "scene",
                  }],
              }
          },
          {
              "component": "Transform",
          },
          {
              "component": "StochasticIntervalEpisodeEnding",
              "kwargs": {
                  "minimumFramesPerEpisode": 1000,
                  "intervalLength": 100,  # Set equal to unroll length.
                  "probabilityTerminationPerInterval": 0.2
              }
          },
      ]
  }
  return scene


def create_avatar_object(player_idx: int,
                         target_sprite_self: Dict[str, Any]) -> Dict[str, Any]:
  """Create an avatar object that always sees itself as blue."""
  # Lua is 1-indexed.
  lua_index = player_idx + 1

  # Setup the self vs other sprite mapping.
  source_sprite_self = "Avatar" + str(lua_index)
  custom_sprite_map = {source_sprite_self: target_sprite_self["name"]}

  live_state_name = "player{}".format(lua_index)
  avatar_object = {
      "name": f"avatar{lua_index}",
      "components": [
          {
              "component": "StateManager",
              "kwargs": {
                  "initialState": live_state_name,
                  "stateConfigs": [
                      # Initial player state.
                      {"state": live_state_name,
                       "layer": "superOverlay",
                       "sprite": source_sprite_self,
                       "contact": "avatar",
                       "groups": ["players"]},

                      # Player wait type for times when they are zapped out.
                      {"state": "playerWait",
                       "groups": ["playerWaits"]},
                  ]
              }
          },
          {
              "component": "Transform",
          },
          {
              "component": "Appearance",
              "kwargs": {
                  "renderMode": "ascii_shape",
                  "spriteNames": [source_sprite_self],
                  "spriteShapes": [shapes.CUTE_AVATAR],
                  "palettes": [shapes.get_palette(
                      human_readable_colors[player_idx])],
                  "noRotates": [True]
              }
          },
          {
              "component": "AdditionalSprites",
              "kwargs": {
                  "renderMode": "ascii_shape",
                  "customSpriteNames": [target_sprite_self["name"]],
                  "customSpriteShapes": [target_sprite_self["shape"]],
                  "customPalettes": [target_sprite_self["palette"]],
                  "customNoRotates": [target_sprite_self["noRotate"]],
              }
          },
          {
              "component": "Avatar",
              "kwargs": {
                  "index": lua_index,
                  "aliveState": live_state_name,
                  "waitState": "playerWait",
                  "spawnGroup": "spawnPoints",
                  "actionOrder": ["move",
                                  "turn"],
                  "actionSpec": {
                      "move": {"default": 0, "min": 0, "max": len(_COMPASS)},
                      "turn": {"default": 0, "min": -1, "max": 1},
                  },
                  "view": {
                      "left": 5,
                      "right": 5,
                      "forward": 9,
                      "backward": 1,
                      "centered": False
                  },
                  "spriteMap": custom_sprite_map,
              }
          },
          {
              "component": "SequentialCollection",
              "kwargs": {
                  # These are lua indexes (count from 1 not from 0!)
                  "sequence": [1, 2, 3],
              } 
          },
      ]
  }

  return avatar_object


def create_avatar_objects(num_players):
  """Returns list of avatar objects of length 'num_players'."""
  avatar_objects = []
  for player_idx in range(0, num_players):
    game_object = create_avatar_object(player_idx,
                                       TARGET_SPRITE_SELF)
    avatar_objects.append(game_object)

  return avatar_objects


def get_config():
  """Default configuration for the clean_up level."""
  config = config_dict.ConfigDict()

  # Action set configuration.
  config.action_set = ACTION_SET
  # Observation format configuration.
  config.individual_observation_names = [
      "RGB",
  ]
  config.global_observation_names = [
      "WORLD.RGB",
  ]

  # The specs of the environment (from a single-agent perspective).
  config.action_spec = specs.action(len(ACTION_SET))
  config.timestep_spec = specs.timestep({
      "RGB": specs.OBSERVATION["RGB"],
      "READY_TO_SHOOT": specs.OBSERVATION["READY_TO_SHOOT"],
      # Global switching signals for puppeteers.
      "NUM_OTHERS_WHO_CLEANED_THIS_STEP": specs.float64(),
      # Debug only (do not use the following observations in policies).
      "WORLD.RGB": specs.world_rgb(ASCII_MAP, SPRITE_SIZE),
  })

  # The roles assigned to each player.
  config.valid_roles = frozenset({"default"})
  config.default_player_roles = ("default",) * 2  # This ends up controlling the number of players.

  return config

def build(
    roles: Sequence[str],
    config: config_dict.ConfigDict,
) -> Mapping[str, Any]:
  """Build the clean_up substrate given roles."""
  del config
  num_players = len(roles)
  # Build the rest of the substrate definition.
  substrate_definition = dict(
      levelName="sequential_gathering",
      levelDirectory="meltingpot/lua/levels",
      numPlayers=num_players,
      # Define upper bound of episode length since episodes end stochastically.
      maxEpisodeLengthFrames=5000,
      spriteSize=SPRITE_SIZE,
      topology="BOUNDED",  # Choose from ["BOUNDED", "TORUS"],
      simulation={
          "map": ASCII_MAP,
          "gameObjects": create_avatar_objects(num_players),
          "scene": create_scene(),
          "prefabs": create_prefabs(),
          "charPrefabMap": CHAR_PREFAB_MAP,
      },
    )
  return substrate_definition