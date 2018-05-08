# Importing IntentBuilder
from adapt.intent import IntentBuilder
# Importing MycroftSkill class
from mycroft.skills.core import MycroftSkill
import os
from time import sleep
from picamera import PiCamera
__author__ = 'reaperjudge'
# Creating Backtalk extending MycroftSkill
class Picture(MycroftSkill):
    camera = PiCamera()
    camera.resolution = (1024, 768)

    def __init__(self):
        super(Picture, self).__init__(name="Picture")

    def initialize(self):
        # Creating GreetingsIntent requiring Greetings vocab
        picture_intent = IntentBuilder("Intent").\
            require("shutdown").build()
        self.register_intent(picture_intent,
                               self.handle_intent)     
    def handle_intent(self, message):
        self.speak("taking picture")
        camera.start_preview()
        # Camera warm-up time
        sleep(2)
        camera.capture('foo.jpg')
        self.speak("finished taking picture"
        # html image search
   
    def stop(self):
        pass

def create_skill():
    return Picture()
