import vlc
import os
import threading
import sqlite3

import config

class YTUser:
    ''' A user of the stream. '''
    def __init__(self, name: str) -> None:
        self.onCooldown = False
        self.timer = None
        self.name = name

    def summonSound(self, sound):
        '''Plays the sound from the sfx folder. Make sure the name of the sound is the same as the trigger.'''
        print("Playing sound " + sound + "...")

        file = sound + config.EXTENSION

        for filename in os.listdir("sfx"):
            if filename == file:
                p = vlc.MediaPlayer("sfx/" + file)
                p.audio_set_volume(config.VOLUME)
                p.play()
                self.onCooldown = True
                self.timer = threading.Timer(config.COOLDOWN, self.__commandCooldown).start()
                return
            
        print("\nSound not found." + "\n")
        
    def __commandCooldown(self):
        print("Accepting Inputs Again\n")
        self.onCooldown = False

    def searchForSound(self, chatMessage):
        '''The message needs to contain ONLY the trigger word (and the prefix if REQUIRE_PREFIX is True)'''
        if self.onCooldown:
            print("Can't accept inputs right now. Cooldown in effect. \n")
            return
        
        self.onCooldown = False
        chatMessage = chatMessage.lower()

        if config.REQUIRE_PREFIX[0] and chatMessage.startswith(config.REQUIRE_PREFIX[1]):
            print("Prefix command found. Searching for sound...")
            self.summonSound(chatMessage[len(config.REQUIRE_PREFIX[1]):])
            return
        elif config.REQUIRE_PREFIX[0] and not chatMessage.startswith(config.REQUIRE_PREFIX[1]):
            print("Prefix command not found. Ignoring...")
            return
        else:
            print(chatMessage + " was sent. Searching for sound...")
            self.summonSound(chatMessage)

def findUser(name: str) -> YTUser | None:
    ''' Find User in local database by name. '''
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT name FROM users WHERE name = ?", (name,))
    result = c.fetchone()
    conn.close()

    if result == None:
        return None
    else:
        return YTUser(result[0])