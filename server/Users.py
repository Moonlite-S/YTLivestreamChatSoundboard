import vlc
import os
import threading
import sqlite3

from config import EXTENSION, COOLDOWN, VOLUME, REQUIRE_PREFIX


class YTUser:
    ''' A user object of the stream. '''
    def __init__(self, name: str, id: int):
        self.onCooldown: bool = False
        self.timer = None
        self.id: int = id
        self.name: str = name

    def summonSound(self, sound: str):
        '''Plays the sound from the sfx folder. Make sure the name of the sound is the same as the trigger.'''
        print("Trying to play sound: " + sound + "...")

        file = sound + EXTENSION

        for filename in os.listdir("sfx"):
            if filename == file:
                p = vlc.MediaPlayer("sfx/" + file)
                p.audio_set_volume(VOLUME)
                p.play()
                self.onCooldown = True
                self.timer = threading.Timer(COOLDOWN, self.__commandCooldown).start()
                return
            
        print("\nSound not found." + "\n")

    def searchForSound(self, chatMessage: str):
        '''The message needs to contain ONLY the trigger word (and the prefix if REQUIRE_PREFIX is True)'''
        if self.onCooldown:
            print("Can't accept inputs right now. Cooldown in effect. \n")
            return
        
        self.onCooldown = False
        chatMessage = chatMessage.lower()

        if REQUIRE_PREFIX[0] and chatMessage.startswith(REQUIRE_PREFIX[1]):
            print("Prefix command found. Searching for sound...")
            self.summonSound(chatMessage[len(REQUIRE_PREFIX[1]):])
            return
        elif REQUIRE_PREFIX[0] and not chatMessage.startswith(REQUIRE_PREFIX[1]):
            print("Prefix command not found. Ignoring...")
            return
        else:
            print(chatMessage + " was sent. Searching for sound...")
            self.summonSound(chatMessage)

    def __commandCooldown(self):
        print("Accepting Inputs Again for: " + self.name + "\n")
        self.onCooldown = False

def GetUser(c: sqlite3.Cursor, name: str) -> bool:
    ''' Find User in local database by name. Returns True if found. '''
    c.execute("SELECT name FROM users WHERE name = ?", (name,))

    try: 
        result = c.fetchone()[0]
        print("Person found: " + result)
        return True
    except TypeError:
        print("User not found.")
        return False
    
def AddUser(name: str) -> YTUser:
    ''' Add User to local database and returns a YTUser object. '''
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    
    if GetUser(c, name) == False:
        print("Adding user: " + name)
        c.execute("INSERT INTO users (name) VALUES (?)", (name,))

    user_id = c.execute("SELECT user_id FROM users WHERE name = ?", (name,))
    print("Seleted user: " + name + " with id: " + str(user_id.fetchone()[0]))

    user = YTUser(name, user_id.fetchone())

    conn.commit()
    conn.close()

    return user
