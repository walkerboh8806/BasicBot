#!/usr/bin/python3

import subprocess, os, json, string

gameids = {
    "sfv": "7",
    "mkx": "",
    "t7": "17",
    "mvci": "",
    "dbfz": "287",
    "gg": "36",
    "i2": "35",
}



def add_tournament(tournament_name):
    results_script ='python ../smashgg/results.py '+tournament_name
    process = subprocess.Popen(results_script, shell=True, stdout=subprocess.PIPE)
    return process

def list_tournaments():
    dir = 'data/tournaments'
    filenames = os.listdir(dir)
    message = discordify(filenames)
    return message


def discordify(message):
    base = "```"+"\r\n"
    for item in message:
        base = base + str(item) + "\r\n"
    final = base + "\r\n" +"```"
    return final

def combine_discordify(messages):
    final = ""
    for message in messages:
        final = final + message + "\r\n"
    return final

def get_results(tournament_name, event):
    try:
        with open('data/tournaments/'+tournament_name+'/'+event+'/'+'results.json') as f:
            results = json.load(f)
            output = []
            player = ""
            for item in results:
                gamertag = str(item['tag'])
                final_placement = str(item['final_placement'])
                player = final_placement+". "+gamertag
                output.append(player)
        return output
    except FileNotFoundError:
        return ["Problem finding event.  Try `-fgc add tournament <tournament-name>`"]


def event_shorthand(event):
    event_translate = {
        "sfv": "street-fighter-v-singles",
        "mvci": "mvci-singles",
        "t7": "tekken-7-singles",
        "ggxrd": "rev-2-singles",
        "i2": "injustice-2-singles",
        "dbfz": "dbfz"
    }
    event_full = event_translate[event]
    print(event_full)
    return event_full

def get_event_list(tournament_name):
    dir = 'data/tournaments/'+tournament_name
    filenames = os.listdir(dir)
    titles = []
    for folder in filenames:
        titles.append(folder)
    return titles

def pretty_name(name):
    #print(string.capwords(name.replace('-', ' ')))
    return string.capwords(name.replace('-', ' '))

def get_all_results(tournament_name):
    events = get_event_list(tournament_name)
    results = []
    for event in events:
        #print(event)
        results.append(pretty_name(event))
        event_result = discordify((get_results(tournament_name, event)))
        results.append(event_result)
    print(results)
    return results