import subprocess, os, json

gameids = {
    "sfv": "7",
    "mkx": "",
    "t7": "17",
    "mvci": "",
    "dbfz": "287",
    "gg": "36",
    "i2": "35",
}


def list_tournaments():
    dir = '/home/samc/Dropbox/PycharmProjects/discord-bot/data/tournaments'
    filenames = os.listdir(dir)
    message = discordify(filenames)
    return message

def list_players():
    dir = '/home/samc/Dropbox/PycharmProjects/discord-bot/data/players_master'
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


#def generate_results(group_obj):

#Looks up gameid from game name
def get_gameid(game_name):
    try:
        gameid = gameids['gamename']
        return gameid
    except KeyError:
        return "Game not found"


