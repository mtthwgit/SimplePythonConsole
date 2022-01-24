# This is a simple text based game made to test user
# interactivity.

class textGame:
    def __init__(self):
        self.currentScene = None
        self.actions = ["move", "punch", "talk", "stop game"]

    def parseAction(self, text):
        textL = " " + text.lower() + " "
        noAction = True
        global playing
        for action in self.actions:
            if textL.find(" " + action + " ") != -1:
                if action == "move":
                    noAction = False
                    self.currentScene.move(textL)
                    break
                elif action == "talk":
                    noAction = False
                    self.currentScene.talk(textL)
                    break
                elif action == "punch":
                    noAction = False
                    self.currentScene.punch(textL)
                    break
                elif action == "stop game":
                    noAction = False
                    playing = False
                    break
        if noAction:
            print("That action is not recognized. Recognized actions are: move, punch, talk, and 'stop game'.")

    def setScene(self, scene):
        self.currentScene = scene

# Living room
class Scene1:
    def __init__(self, tg):
        print("You are in your living room with your couch and tv. Your kitchen and bedroom are nearby.\n")
        self.punchedTv = False
        self.punchSelfCounter = 0
        self.tg = tg

    def punch(self, text):
        things = ["tv", "couch", "self"]
        punched = False
        for item in things:
            if text.find(item) != -1:
                punched = True
                if item == "tv":
                    if not self.punchedTv:
                        print("You punch your tv in a fit of primal rage. The screen cracks\n and your fist"
                              " hurts. You wonder why you just did that.\n")
                    else:
                        print("You already punched your tv. Like, chill out, man.\n")
                elif item == "couch":
                    print("You punch your fluffy couch. There is no apparent damage.\n")
                elif item == "self":
                    if self.punchSelfCounter == 0:
                        print("OUCH! Now why would you do that? Don't do that again.\n")
                        self.punchSelfCounter += 1
                    elif self.punchSelfCounter == 1:
                        print("AGAIN? Your face is really hurting now.\n")
                        self.punchSelfCounter += 1
                    elif self.punchSelfCounter == 2:
                        print("You continue beating yourself. You are definitely gonna be sore tomorrow. "
                              "You should stop.\n")
                        self.punchSelfCounter += 1
                    elif self.punchSelfCounter == 3:
                        print("Since you are so determined to beat yourself, you punch yourself so hard"
                              " that you\ndie. There, you killed yourself, happy? Try actually playing the game now\n")
                        self.tg.setScene(Scene1(self.tg))
        if not punched:
            print("Action failed, specify what you are punching\n")

    def talk(self, text):
        things = ["tv","couch"]
        talked = False
        for item in things:
            if text.find(item) != -1:
                talked = True
                if item == "tv":
                    print("You talk to the tv. It doesn't respond.\n")
                if item == "couch":
                    print("You say some kind words to your couch.\n")
        if not talked:
            print("Action failed, specify what you are talking to\n")

    def move(self, text):
        things = ["kitchen", "bedroom", "outside"]
        moved = False
        for item in things:
            if text.find(item) != -1:
                moved = True
                if item == "kitchen":
                    print("You move to the kitchen where your fridge and pantry are.\n")
                    self.tg.setScene(kitchen(self.tg))
                elif item == "bedroom":
                    print("You go to your bedroom.\n")
                    self.tg.setScene(bedroom(self.tg))
                elif item == "outside":
                    print("You go outside your apartment.\n")
                    print("You walk outside of your apartment into a formless void. You fall into it. As you fall you "
                          "somehow\n"
                          "know that your fate was decided by a lazy computer science student who didn't want\n"
                          "to code an entire open world in a text based game. You curse him and his laziness.\n"
                          "You find yourself standing back inside your living room.")
        if not moved:
            print("Action failed. Specify where you are moving.\n")

class kitchen:
    def __init__(self, tg):
        print("You are in your kitchen with your living room behind you. You "
              "think about checking the pantry or the fridge.\n")
        self.tg = tg

    def punch(self, text):
        things = ["fridge", "pantry"]
        punched = False
        for item in things:
            if text.find(item) != -1:
                punched = True
                if item == "fridge":
                    print("You punch your fridge. Ouch.\n")
                elif item == "pantry":
                    print("You punch your pantry doors. Your fist hurts.\n")
        if not punched:
            print("Action failed. Specify what you are punching.\n")

    def talk(self, text):
        things = ["fridge", "pantry"]
        talked = False
        for item in things:
            if text.find(item) != -1:
                talked = True
                if item == "fridge":
                    print("You talk to your fridge. Unfortunately it isn't a smart fridge.\n")
                if item == "pantry":
                    print("You are pretty much talking to a wall. You need help.\n")
        if not talked:
            print("Action failed. Specify what you are talking to\n")

    def move(self, text):
        things = ["fridge", "pantry", "living room"]
        moved = False
        for item in things:
            if text.find(item) != -1:
                moved = True
                if item == "fridge":
                    print("You move to your fridge.\n")
                    self.tg.setScene(fridge(self.tg))
                elif item == "pantry":
                    print("You move to your pantry.\n")
                    print("You move to the pantry and open the door. There is nothing except for a \n"
                          "void. You somehow get the feeling that the further you get from the\n"
                          "living room the less detailed your world will be. You go back into the kitchen\n")
                elif item == "living room":
                    print("You move to your living room.\n")
                    self.tg.setScene(Scene1(self.tg))
        if not moved:
            print("Action failed. Specify where you are moving.\n")

class fridge:
    def __init__(self, tg):
        print("You are in front of your open fridge with your kitchen behind you. Inside your fridge is"
              " a half eaten pizza\nand a jar of pickles.\n")
        self.tg = tg

    def punch(self, text):
        things = ["pizza", "pickle"]
        punched = False
        for item in things:
            if text.find(item) != -1:
                punched = True
                if item == "pizza":
                    print("You violently grab a slice pizza and shove it into your mouth. Tasty.\n")
                if item == "pickle":
                    print("You shove your entire fist into the pickle jar and shove one into your mouth.\n")
        if not punched:
            print("Action failed, specify what you are punching.\n")

    def talk(self, text):
        things = ["pizza", "pickle"]
        talked = False
        for item in things:
            if text.find(item) != -1:
                talked = True
                if item == "pickle":
                    print("You talk to the pickles. To your surprise, one of the pickles replies. The pickle\n"
                          "says 'I'm the smartest guy alive and I turned myself into a\npickle.' "
                          "It's the funniest thing you've ever seen.\n")
                if item == "pizza":
                    print("You talk to the pizza. You stare into the pizza. The pizza stares back.\n")
        if not talked:
            print("Action failed. Specify what you are talking to")

    def move(self, text):
        things = ["kitchen"]
        moved = False
        for item in things:
            if text.find(item) != -1:
                moved = True
                if item == "kitchen":
                    print("You move back to the kitchen.\n")
                    self.tg.setScene(kitchen(self.tg))
        if not moved:
            print("Action failed. Specify where you are moving.\n")

class bedroom:
    def __init__(self, tg):
        print("You are in your bedroom with your living room behind"
              " you. Your comfy bed sits in the corner.")
        self.tg = tg

    def punch(self, text):
        things = ["bed"]
        punched = False
        for item in things:
            if text.find(item) != -1:
                punched = True
                if item == "bed":
                    print("You punch your bed. I wonder what the source of your rage is. Perhaps\n"
                          "you've been sleeping poorly and have some kind of misplaced anger\n"
                          "towards your bed because of it. Maybe you should just go to bed earlier.\n")
        if not punched:
            print("Action failed. Specify what you are punching.\n")

    def talk(self, text):
        things = ["bed"]
        talked = False
        for item in things:
            if text.find(item) != -1:
                talked = True
                if item == "bed":
                    print("You talk to your bed. While talking to it you realize\n"
                          "that this bed has been there for you through so much, always"
                          " there for you to lay\ndown on. You are more appreciative"
                          " of your bed now.\n")
        if not talked:
            print("Action failed. Specify what you are talking to.\n")

    def move(self, text):
        things = ["bed", "living room"]
        global playing
        moved = False
        for item in things:
            if text.find(item) != -1:
                moved = True
                if item == "bed":
                    print("You get into your bed. It is warm and comfy. Goodnight.\n\nYou win!")
                    playing = False
                if item == "living room":
                    print("You decide to go back to the living room.\n")
                    self.tg.setScene(Scene1(self.tg))
        if not moved:
            print("Action failed. Specify where you are moving.\n")

if __name__ == '__main__':
    global playing
    playing = True
    game = textGame()
    print("Welcome to my simple text game. The end goal of the game is to go to \nbed, but there are a lot"
          " of other things you can do before doing that! \n")
    print("Recognized verbs are: move, punch, talk, and 'stop game'\n")
    print("You are sitting in your apartment on the couch watching tv after a long hard day of work."
          "\nYou feel a little peckish and could go for some food, but you also kind of want a"
          " redbull from the gas\nstation around the corner\n")
    game.setScene(Scene1(game))
    while playing:
        userAction = input("What do you do: ")
        game.parseAction(userAction)

    print("Thanks for playing!")
    pass
