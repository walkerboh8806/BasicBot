#!/usr/bin/python

import json
import operator
import argparse
import os
import pysmash

parser = argparse.ArgumentParser(description="Pull Tournament Results")
parser.add_argument('tournament', type=str)
args = parser.parse_args()

smash = pysmash.SmashGG()

tournament = args.tournament

events = smash.tournament_show_events(tournament)

directory = '../fgcbot/data/tournaments/' + tournament
os.mkdir(directory)
for event in events['events']:
    os.mkdir(directory+'/'+event)
    sets = smash.tournament_show_players(tournament, event)
    sets.sort(key=operator.itemgetter('final_placement'))
    with open('../fgcbot/data/tournaments'+'/'+tournament+'/'+event+'/results.json', 'w+') as f:
        json.dump(sets, f)

