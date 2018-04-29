# Importing IntentBuilder
from adapt.intent import IntentBuilder
# Importing MycroftSkill class
from mycroft.skills.core import MycroftSkill

# Creating HelloWorldSKill extending MycroftSkill
class HelloWorldSkill(MycroftSkill):
    
    def __init__(self):
        super(HelloWorldSkill, self).__init__("HelloWorldSkill")

    def initialize(self):
        # Creating GreetingsIntent requiring Greetings vocab
        greetings = IntentBuilder("GreetingsIntent")
                           .require("Greetings").build()
        # Associating a callback with the Intent
        self.register_intent(greetings, self.handle_greetings)
        
    def handle_greetings(self):
        # Sending a command to mycroft, speak Greetings Dialog
        self.speak_dialog("Greetings")
        
    def stop(self):
        pass


def create_skill():
return HelloWorldSkill()
