import json, smashgg
from pprint import pprint

#def tournament_add(tournament):
    #add tournament to list

#def tournament_remove(tournament):
    #remove tournament from list

def tournament_list():
    with open("tournaments.json", "r") as myfile:
        output = "```"
        for line in myfile:
            output = output + line + "\r\n"
        output = output + "```"
        return output

def get_eventids(tournament):
    raw = smashgg.get_raw_tournament(tournament)
    eventids = raw['entities']['tournament']['eventIds']
    return eventids

def get_groupids(eventids):
    groupids = []
    for id in eventids:
        event_detail = smashgg.get_event_details(id)
        groupid = event_detail['entities']['groups'][0]['id']
        groupids.append(groupid)
    return groupids

def get_player_standing(groupids):
    player_results = []
    for id in groupids:
        player_raw = smashgg.get_user_data(id)
        print(player_raw)
        player_results.append(player_raw)
    return player_results