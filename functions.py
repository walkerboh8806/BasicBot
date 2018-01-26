import subprocess, os

def list_tournaments():
    dir = '/home/samc/Dropbox/PycharmProjects/discord-bot/data/tournaments'
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