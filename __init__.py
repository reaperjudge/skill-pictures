# Importing IntentBuilder
from adapt.intent import IntentBuilder
# Importing MycroftSkill class
from mycroft.skills.core import MycroftSkill
import os
__author__ = 'reaperjudge'

# Creating Backtalk extending MycroftSkill
class Backtalk(MycroftSkill):
    def __init__(self):
        super(Backtalk, self).__init__(name="Backtalk")

    def initialize(self):
        # Creating GreetingsIntent requiring Greetings vocab
        shutdown_intent = IntentBuilder("shutdownIntent").\
            require("shutdown").build()
        self.register_intent(shutdown_intent,
                               self.handle_shutdown_intent)

        restart_intent = IntentBuilder("restartIntent").\
            require("restart").build()
        self.register_intent(restart_intent,
                             self.handle_restart_intent)
        
    def handle_shutdown_intent(self, message):
        self.speak("shutting Down")
        os.system("systemctl poweroff")

    def handle_restart_intent(self, message):
        self.speak("restarting")
        os.system("systemctl reboot")
        
    def stop(self):
        pass

def create_skill():
    return Backtalk()
