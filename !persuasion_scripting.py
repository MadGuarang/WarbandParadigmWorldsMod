                            ########. 1            POPULAR BLOCK




#1. Persuasion attempt

[anyone,"lady_proposal_refused_persuade_check",
    [
	],
    "What do you have to say?", "lady_proposal_refused_persuade_player_response",[
	
	(assign, reg4, 70),   ##relation needed for auto success
	(call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", "trp_player"),
	(assign, ":cur_relation", reg0),
	(assign, reg5, ":cur_relation"),
	(assign, reg9, 10),    ## how many relation points is at stake
    #player gather power
    (store_attribute_level, ":charisma", "trp_player", ca_charisma),
    (store_skill_level, ":pro_level", "skl_trainer", "trp_player"),
    (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
	(store_sub, ":difference", 70, ":cur_relation"),    #70 is relation needed for autosuccess
	(val_div, ":charisma", 3), 
	(val_mul, ":persuasion_level", 2), 
	(val_add, ":persuasion_level", ":pro_level"), 
    
    # persuaded troop gather power
    (store_attribute_level, ":troop_charisma", "$g_talk_troop", ca_charisma),
    (store_skill_level, ":troop_pro_level", "skl_trainer", "$g_talk_troop"),
    (store_skill_level, ":troop_persuasion_level", "skl_persuasion", "$g_talk_troop"),
    (val_div, ":troop_charisma", 3), 
	(val_mul, ":troop_pro_level", 2), 
	(val_add, ":troop_persuasion_level", ":troop_pro_level"), 
    
    (try_begin), #if player is in good relation than it is just question of individual speaker inertia (1/3), if in bad relations than oppose with all power
    	(gt, ":cur_relation", 75),
        (val_div, ":troop_persuasion_level",4), 
        (else_try),
        (gt, ":cur_relation", 50),
        (val_div, ":troop_persuasion_level",3), 
        (else_try),
        (gt, ":cur_relation", 0),
        (val_div, ":troop_persuasion_level",2), 
        (else_try),
        (gt, ":cur_relation", -20),
        (val_mul, ":troop_persuasion_level",2), 
        (val_div, ":troop_persuasion_level",3), 
        (else_try),
        (gt, ":cur_relation", -40),
        (val_mul, ":troop_persuasion_level",1), 
        (else_try), 
        (gt, ":cur_relation", -60),
        (val_mul, ":troop_persuasion_level",3), 
        (val_div, ":troop_persuasion_level",2), 
        (else_try), 
        (val_mul, ":troop_persuasion_level",2),  
    (try_end),    
    
    (val_mul, ":troop_persuasion_level", -1), 
	(val_add, ":persuasion_level", ":troop_persuasion_level"), 
    
	(try_begin),
		(gt, ":difference", ":persuasion_level"),
		(assign, "$g_persuasion_failure_chance", 100),
	(else_try),
		(store_mul, "$g_persuasion_failure_chance", ":difference", 100),
		(val_div, "$g_persuasion_failure_chance", ":persuasion_level"),
	(try_end),
	(assign, reg8, "$g_persuasion_failure_chance"),
	(store_sub, reg7, 100, "$g_persuasion_failure_chance"),
	(dialog_box, "str_persuasion_opportunity"),

    ]],	
	
  [anyone|plyr,"lady_proposal_refused_persuade_player_response",
    [
	],
    "Love is as a rose, my lady. Left unplucked, it may wither.", "lady_proposal_refused_persuade_result",[
    ]],	
	
  [anyone|plyr,"lady_proposal_refused_persuade_player_response",
    [],
    "Oh, never mind.", "lady_pretalk",
    []],	
	
	
  [anyone,"lady_proposal_refused_persuade_result",
    [
	(store_random_in_range, ":random", 0, 100),
	(lt, ":random", "$g_persuasion_failure_chance"),
	],
    "Enough, sir! I shall not be rushed into marriage, with you or with anyone else! You have made me very cross. Please, leave me alone for a while. I shall let you know when I am ready to speak to you again.", "close_window", [
	(call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "trp_player", -1),
	(jump_to_menu, "mnu_town"),
	(finish_mission),
	]],	


  [anyone,"lady_proposal_refused_persuade_result",
    [
	(call_script, "script_get_kingdom_lady_social_determinants", "$g_talk_troop"),
	(assign, ":guardian", reg0),
	(troop_slot_eq, ":guardian", slot_lord_granted_courtship_permission, -1),
	(str_store_troop_name, s4, reg0),	
	(call_script, "script_troop_get_family_relation_to_troop", ":guardian", "$g_talk_troop"),
	],
    "Oh {playername}, I could never allow that to happen! Oh, if only we could be wed! But my family would never agree... Perhaps it is best that we part...", "lady_betrothed", [
	(call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "trp_player", 5),
	]],	
    
  ###
#random global  
(store_random_in_range, "$g_random", 0, 100),
	(lt, ":random", "$g_persuasion_failure_chance"),
    (assign,"$g_persuasion_failure_chance",-1),
    
    
   #2 #relation
    
    	(try_begin),
				(call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", "trp_player"),
				(le, reg0, 20),
				(ge, reg0, -50),
				(call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "trp_player", -5),
			(try_end),
	
    
    
    #troop_slots
     (troop_get_slot, ":last_persuasion_time", "trp_player", slot_troop_last_persuasion_time),
      (troop_set_slot, "trp_player", slot_troop_last_persuasion_time, ":last_persuasion_time"), 
      
      
      
#script_inflict_casualties_to_party:





 (try_for_parties, ":party_no"),
        (party_is_active, ":party_no"),
        (party_get_slot, ":cur_party_type", ":party_no", slot_party_type),
        (store_faction_of_party, ":cur_faction", ":party_no"),
        (eq, ":cur_party_type", ":party_type"),
        (eq, ":cur_faction", ":faction_no"),
        (val_add, reg0, 1),
      (try_end),



(party_set_banner_icon, ":center_no", 0),#Removing banner
		





 (try_begin), ###BANNER for village?
      		(party_slot_eq, ":center_no", slot_party_type, spt_village),
		(gt, ":lord_troop_id", -1),
		
#normal_banner_begin
        (troop_get_slot, ":cur_banner", ":lord_troop_id", slot_troop_banner_scene_prop),
        (gt, ":cur_banner", 0),
        (val_sub, ":cur_banner", banner_scene_props_begin),
        (val_add, ":cur_banner", banner_map_icons_begin),
        
                ####banner-bug madg
                 (try_begin), 
  (this_or_next|is_between, ":lord_troop_id", active_npcs_4_banners_end , active_npcs_end),  
  (gt, ":cur_banner", "icon_banner_136"),
  
 (faction_get_slot, ":cur_banner", ":lord_troop_faction", slot_faction_banner),
 
                    
                ####banner-bug
         
         
        (party_set_banner_icon, ":center_no", ":cur_banner"),
# custom_banner_begin
#        (troop_get_slot, ":flag_icon", ":lord_troop_id", slot_troop_custom_banner_map_flag_type),
#        (ge, ":flag_icon", 0),
#        (val_add, ":flag_icon", custom_banner_map_icons_begin),
#        (party_set_banner_icon, ":center_no", ":flag_icon"),
    (try_end),
    
    
(try_begin),
        (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
        (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
			(party_slot_eq, ":center_no", slot_party_type, spt_castle),
		(gt, ":lord_troop_id", -1),
		
#normal_banner_begin
        (troop_get_slot, ":cur_banner", ":lord_troop_id", slot_troop_banner_scene_prop),
        (gt, ":cur_banner", 0),
        (val_sub, ":cur_banner", banner_scene_props_begin),
        (val_add, ":cur_banner", banner_map_icons_begin),
        
          ####banner-bug madg
                 (try_begin), 
  (this_or_next|is_between, ":lord_troop_id", active_npcs_4_banners_end , active_npcs_end),  
  (gt, ":cur_banner", "icon_banner_136"),
  
 (faction_get_slot, ":cur_banner", ":lord_troop_faction", slot_faction_banner),
               
                ####banner-bug
                
                
        (party_set_banner_icon, ":center_no", ":cur_banner"),
# custom_banner_begin
#        (troop_get_slot, ":flag_icon", ":lord_troop_id", slot_troop_custom_banner_map_flag_type),
#        (ge, ":flag_icon", 0),
#        (val_add, ":flag_icon", custom_banner_map_icons_begin),
#        (party_set_banner_icon, ":center_no", ":flag_icon"),
    (try_end),