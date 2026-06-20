from .story import StoryManager

class Application:
    _name = 'Site Manager'

    def __init__(self):
        self.story_manager = StoryManager()
        return