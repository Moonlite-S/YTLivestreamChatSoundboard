import os
import config

from Users import YTUser, GetUser

def createSoundList():
    '''Optional: This creates a text file with all the current sound triggers. This is useful for the viewers to know what sounds they can trigger. 
    '''
    sfxDir = "sfx"

    with open("soundList.txt", "w") as f:
        f.write("Possible sound commands:\n\n")
        for filename in os.listdir(sfxDir):
            if filename.endswith(config.EXTENSION):
                filename = filename[:-4]
                f.write(filename + "\n")

def testUsers():
    '''Optional: Test if the YTUser object is working.'''
    testList: YTUser = []

    testUser = GetUser(testList, "test")
    testUser2 = GetUser(testList, "test2")
    testUser3 = GetUser(testList, "test3")

    assert testUser.name == "test"
    assert testUser2.name == "test2"
    assert testUser3.name == "test3"

    assert len(testList) == 3

    assert testUser.onCooldown == False
    assert testUser2.onCooldown == False
    assert testUser3.onCooldown == False

    testUser.searchForSound("hi")
    testUser2.searchForSound("hi")
    testUser3.searchForSound("hi")

    assert testUser.onCooldown == True
    assert testUser2.onCooldown == True
    assert testUser3.onCooldown == True

    testUser.searchForSound("hi")
    testUser2.searchForSound("hi")
    testUser3.searchForSound("hi")

    print("All tests passed!")