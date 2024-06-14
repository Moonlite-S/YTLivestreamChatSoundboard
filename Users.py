import vlc
import os
import threading

from config import EXTENSION, COOLDOWN, VOLUME, REQUIRE_PREFIX

class YTUser:
    ''' A user object of the stream. '''
    def __init__(self, name: str):
        self.onCooldown: bool = False
        self.timer = None
        self.name: str = name

    def searchForSound(self, chatMessage: str):
        '''The message needs to contain ONLY the trigger word (and the prefix if REQUIRE_PREFIX is True)'''
        if self.onCooldown:
            print("Can't accept inputs right now. Cooldown in effect. \n")
            return
        
        self.onCooldown = False
        chatMessage = chatMessage.lower().strip()

        if REQUIRE_PREFIX[0] and chatMessage.startswith(REQUIRE_PREFIX[1]):
            print("Prefix command found. Searching for sound...")
            self.__summonSound(chatMessage[len(REQUIRE_PREFIX[1]):])
            return
        elif REQUIRE_PREFIX[0] and not chatMessage.startswith(REQUIRE_PREFIX[1]):
            print("Prefix command not found. Ignoring...")
            return
        else:
            print(chatMessage + " was sent. Searching for sound...")
            self.__summonSound(chatMessage)

    def __commandCooldown(self):
        print("Accepting Inputs Again for: " + self.name + "\n")
        self.onCooldown = False

    def __summonSound(self, sound: str):
        '''Plays the sound from the sfx folder. Make sure the name of the sound is the same as the trigger.'''
        print("Trying to play sound: " + sound + "...")

        file = sound + EXTENSION

        for filename in os.listdir("sfx"):
            if filename == file:
                print("Sound found. Playing...")
                p = vlc.MediaPlayer("sfx/" + file)
                p.audio_set_volume(VOLUME)
                p.play()
                self.onCooldown = True
                self.timer = threading.Timer(COOLDOWN, self.__commandCooldown).start()
                return
            
        print("\nSound not found." + "\n")

def GetUser(activeUsers: list, name: str) -> YTUser: 
    ''' Returns the user object with the given name. If the user is not found, creates a new one. '''
    for i in range(len(activeUsers)):
        if activeUsers[i].name == name:
            print("User " + name + " is already in active users.")
            user = activeUsers[i]
            return user

    user: YTUser = YTUser(name)
    activeUsers.append(user)
    print("Active users: " + str(activeUsers))

    return user