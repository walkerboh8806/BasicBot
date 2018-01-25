import urllib
import requests
import json


def get_raw_tournament(touranment):
    url = "https://api.smash.gg/tournament/"+str(touranment)+"?expand[]=event"
    response = requests.get(url)
    #print(json.loads(response.content.decode('utf-8')))
    return json.loads(response.content.decode('utf-8'))

def get_event_details(eventid):
    url = "https://api.smash.gg/event/"+str(eventid)+"?expand[]=groups"
    #print(url)
    response = requests.get(url)
    #print(json.loads(response.content.decode('utf-8')))
    return json.loads(response.content.decode('utf-8'))

def get_user_data(groupid):
    url = "https://api.smash.gg/phase_group/"+str(groupid)+"?expand[]=entrants&expand[]=seeds&expand[]=sets"
    response = requests.get(url)
    print(url)
    #print(json.loads(response.content.decode('utf-8')))
    return json.loads(response.content.decode('utf-8'))

def get_tournament(name):
    eventid = []
    return eventid

def get_groups(eventid):
    groupid = []
    return groupid

def get_players(groupid):
    players = []
    return players