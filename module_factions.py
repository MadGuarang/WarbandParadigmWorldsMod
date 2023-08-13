from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02),("undeads",-0.1)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(100), 0.5,[("commoners",-0.6),("player_faction",-0.5)], [], 0xd00000),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  ("culture_1",  "Creatures's Democratic Republic of Morlok", 0, 0.9, [], []),
  ("culture_2",  "Necrocorp Syndicate", 0, 0.9, [], []),
  ("culture_3",  "Alien Shogunate", 0, 0.9, [], []),
  ("culture_4",  "Fantasy Magioucracy", 0, 0.9, [], []),
  ("culture_5",  "United States of Renaissance", 0, 0.9, [], []),
  ("culture_6",  "Sanitarium Conspiracy", 0, 0.9, [], []),
  ("culture_7",  "Unholy Alliance", 0, 0.9, [], []),
  ("culture_8",  "BioCorp-Tek", 0, 0.9, [], []),
  ("culture_9",  "Badlands", 0, 0.9, [], []),
 #custom_culture start 
  ("culture_custom",  "New Paradigm", 0, 0.9, [], []),
 #custom_culture_end 
  ("culture_8a",  "{!}culture_6", 0, 0.9, [], []),
  ("culture_9a",  "{!}culture_6", 0, 0.9, [], []),

#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),              !!!!WARNING CONSTANT =        npc_kingdoms_4_banners_end = "fac_kingdom_7"

  ("player_faction","Player Faction",0, 0.9, [], [],0x2ccb4a),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.5),("mountain_bandits", -0.05),("forest_bandits", -0.05),("doomsday_cultists",-1.0)], [], 0x6fcb2c), #changed name so that can tell difference if shows up on map
  ("kingdom_1",  "Creatures's Democratic Republic of Morlok", 0, 0.9, [("undeads",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.25),("forest_bandits", 0.2)], [], 0x4c473d),
  ("kingdom_2",  "Necrocorp Syndicate",    0, 0.9, [("weimear_rebellion",-0.25),("undeads",0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x35c191),
  ("kingdom_3",  "Alien Shogunate", 0, 0.9, [("weimear_rebellion",-0.2),("manhunters",-0.3),("undeads",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x339bdd),
  ("kingdom_4",  "Fantasy Magioucracy",    0, 0.9, [("weimear_rebellion",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", 0.25),("forest_bandits", -0.05)], [], 0xCC99FF),
  ("kingdom_5",  "United States of Renaissance",  0, 0.9, [("undeads",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05)], [], 0xff4e00),
  ("kingdom_6",  "Sanitarium Conspiracy",  0, 0.9, [("undeads",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("desert_abominations", 0.2)], [], 0xDDDD33),
  ("kingdom_7",  "Unholy Alliance",  0, 0.9, [("forest_bandits", 0.25),("stargate", -0.4),("commoners", -0.15),("undeads",0.75),("outlaws",-0.05),("crazy_pikt", -0.2),("peasant_rebels", -0.1),("deserters", -0.02)], [], 0x111212),
  ("kingdom_8",  "BioCorp-Tek",  0, 0.9, [("forest_bandits",0.05),("desert_abominations",0.05),("outlaws",0.05),("peasant_rebels", -0.1),("deserters", -0.02)], [], 0x77ff1d),
  ("kingdom_9",  "Badlands",  0, 0.9, [("forest_bandits",0.05),("desert_abominations",0.02),("outlaws",0.35),("peasant_rebels", -0.1),("weimear_rebellion",0.25),("doomsday_cultists",-1.0)], [], 0xff00ff),
  
 # ("kingdom_10",  "Badlands",  0, 0.9, [("doomsday_cultists",0.1),("undeads",0.25),("commoners",-0.2),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02)], [], 0x214058),
 # ("kingdom_11",  "Pagan Alliance",  0, 0.9, [("doomsday_cultists",0.1),("undeads",0.25),("commoners",-0.2),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02)], [], 0x214058),
 # ("kingdom_12",  "Slavers",  0, 0.9, [("doomsday_cultists",0.1),("undeads",0.25),("commoners",-0.2),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02)], [], 0x214058),

##  ("kingdom_1_rebels",  "Swadian rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_2_rebels",  "Vaegir rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_3_rebels",  "Khergit rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_4_rebels",  "Nord rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_5_rebels",  "Rhodok rebels",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  

##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  ("manhunters","Justice League", 0, 0.5,[("kingdom_3", -0.05),("undeads",-0.75),("deserters", -0.5),("outlaws",-0.6),("player_faction",0.1)], [], 0x608cfc),
  ("rogue_manhunters","Rogue Pirate Hunters", 0, 0.5,[("doomsday_cultists",-0.1),("kingdom_6",0.2),("manhunters",-0.3),("undeads",-0.05),("kingdom_3",-0.05),("outlaws",-0.6),("player_faction",0.1)], [], 0x0036ff),
  ("deserters","Deserters", 0, 0.5,[("commoners",-0.7),("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x1c7011),
  ("mountain_bandits","Scoiatael Commando", 0, 0.5,[("deserters", -0.05),("kingdom_2", -0.2),("kingdom_5", -0.2),("kingdom_4", 0.2),("weimear_rebellion", -0.2)], [], 0x237733),
  ("weimear_rebellion","Weimear Rebellion", 0, 0.5,[("deserters", -0.15),("commoners",0.2),("kingdom_2", -1.0),("kingdom_5", 0.3),("kingdom_4", 0.2),("forest_bandits", 0.2)], [], 0x116ab6),
  ("forest_bandits","Zona Adventurers", 0, 0.5,[("deserters", -0.05),("kingdom_1", 0.2),("kingdom_3", 0.2),("doomsday_cultists", -0.2),("commoners", -0.2),("weimear_rebellion", 0.3)], [], 0xffb464),
  #like fantasy
  ("undeads","Undeads", 0, 0.5, [("lost_legion",-0.2),("commoners",-0.3),("player_faction",-0.2),("deserters", -0.05),("merchants",-0.5),("manhunters", -0.05),("forest_bandits", -0.05)],[], 0x52245d),
  #like morlok
  ("doomsday_cultists","Doomsday Cultists", 0, 0.5,[("stargate", -0.2),("old_gods", -0.9),("outlaws",0.2),("player_faction", -1.00),("commoners",-0.2),("kingdom_1", 0.2),("kingdom_2", -0.2),("kingdom_3", -0.2),("kingdom_4", -0.4),("kingdom_5", -0.2),("kingdom_6", -0.2),("kingdom_7", -0.2),("kingdom_8", -0.2),("kingdom_9", 0.0)], [], 0xe97257),
  #like alien  
  ("stargate","Star Gate Expedition", 0, 0.5,[("doomsday_cultists", -0.2),("undeads", -0.2),("crazy_pikt", -0.1),("desert_abominations", -0.15),("player_faction", -0.15),("kingdom_6", 0.2),("commoners",-0.7)], [], 0x924c19), 
  #neutral good don't like medievals
  ("techno_mages","Engineers", 0, 0.5,[("deserters", -0.2),("old_gods", -0.3),("crazy_pikt", -0.2),("desert_abominations", -0.2)], [], 0x00fff6),  
  #neutral good like renaissance
  #("merc_companions","Mercenary Companions", 0, 0.5,[("commoners",0.3),("merchants",0.7),("monsters",-0.6),("lost_legion",-0.6),("kingdom_1", 0.2),("kingdom_2", 0.2),("kingdom_3", 0.2),("kingdom_4", 0.2),("kingdom_5", 0.2),("kingdom_6", 0.2),("undeads",-0.3),("outlaws",0.1),("stargate", -0.7),("deserters", -0.05),("techno_mages", 0.1)], [], 0xde00ff),
  #neutral good like renaissance
  ("old_gods","Old Gods Crusaders", 0, 0.5,[("doomsday_cultists",-1.0),("undeads",-0.3),("outlaws",-0.5),("crazy_pikt", -0.2),("deserters", -0.5),("kingdom_2", 0.1),("techno_mages", -0.1)], [], 0xffffff),
  #neutral good like Renaissance
  ("lost_legion","New Legion Assimilators", 0, 0.5, [("undeads", -0.2),("crazy_pikt", -0.4),("deserters", -0.45),("merchants",-0.5),("kingdom_5",0.2)],[], 0xff0048),
  #neutral evil, like bandits, outlaws
 # ("monsters","Monsters", 0, -0.1,[("commoners",-0.2),("lost_legion",-0.2),("forest_bandits",-0.2),("manhunters", -0.2),("stargate", -0.2),("player_faction",-0.2),("outlaws",-0.2),("kingdom_1", -0.2),("kingdom_2", -0.2),("kingdom_3", -0.3),("kingdom_4", -0.1),("kingdom_5", -0.2),("kingdom_6", -0.2),("crazy_pikt", 0.2),("techno_mages", 0.05),("desert_abominations", 0.2)], [], 0x073900),
  ("crazy_pikt","Crazy Pikts", 0, 0.5,[("player_faction",-0.2),("outlaws",0.2),("kingdom_1", -0.2),("kingdom_2", -0.2),("kingdom_3", -0.2),("kingdom_4", -0.2),("kingdom_5", 0.2),("kingdom_6", -0.2)], [], 0xff4800),
  ("desert_abominations","Monsters", 0, 0.5,[("stargate",-0.2),("undeads",0.6),("crazy_pikt", -0.1),("player_faction", -0.15),("commoners",-0.7),("techno_mages", -0.2),("kingdom_6", 0.2)], [], 0x5c1800), 
  #minor_factions_end
  #("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
  
  #
  
  #minor cultures start
  ###########ORDER ORDERS
  ("order_le",  "Longbeard Engineeers", 0, 0.5,[("player_faction",0.01),("doomsday_cultists",-0.5),], [], 0xbed4ba),     #1
  ("order_fl",  "Fallen Legion", 0, 0.5,[("player_faction",0.01),("doomsday_cultists",-0.5),], [], 0xc1bad4),            #2
  ("order_tdo", "Tao Dimension Order", 0, 0.5,[("player_faction",0.01),("doomsday_cultists",-0.5),], [], 0xe0e0e0),      #3
  ("order_dig", "Digital Legion", 0, 0.5,[("player_faction",0.01),("doomsday_cultists",-0.5),], [], 0x739e9a),           #4
  ("order_cb",  "Crimson Brothers", 0, 0.5,[("player_faction",0.01),("doomsday_cultists",-0.5),], [], 0x87051f),         #5
  ("order_unk", "Unknown Experiment Narvik", 0, 0.5,[("player_faction",0.01),("doomsday_cultists",-0.5),], [], 0xffb8c6),#6
 
 #change new orders in cons ORDERS_BEGIN, ORDER_END
   ("orders_end","{!}orders_end", 0, 0,[], []),
  
# ("culture_7",  "{!}culture_7", 0, 0.9, [], []),
# ("culture_8",  "{!}culture_8", 0, 0.9, [], []),
   
  
  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

 
]
# modmerger_start version=201 type=4
try:
    component_name = "factions"
    var_set = { "factions":factions,"default_kingdom_relations":default_kingdom_relations, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
