'''Classes and methods for creating and organizing stories
'''

import os
from pathlib import Path
from typing import List

class StoryManager:
    '''Maintain list of stories and their metadata
    '''
    def __init__(self):
        self.story_list: List[str] = self.get_story_list()
        print(self.story_list)
        return
    
    def get_story_list(self) -> List[str]:
        '''Return a list of all stories
        '''
        dir_program = Path(__file__).resolve().parent.parent
        dir_story = os.path.join(dir_program, 'story')
        story_list = []
        for root, dirs, files in os.walk(dir_story):
            for file in files:
                story_list.append(os.path.join(root, file))
            break

        return story_list


class Story:
    '''An individual story (post to the site)
    '''
    def __init__(self):
        return