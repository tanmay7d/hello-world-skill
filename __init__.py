from mycroft import MycroftSkill, intent_file_handler


class HelloWorld(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('world.hello.intent')
    def handle_world_hello(self, message):
        self.speak_dialog('world.hello')


def create_skill():
    return HelloWorld()

