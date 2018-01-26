import subprocess, os

def list_tournaments():
    dir = '/home/samc/Dropbox/PycharmProjects/discord-bot/data/tournaments'
    filenames = os.listdir(dir)
    print(filenames)
    return filenames