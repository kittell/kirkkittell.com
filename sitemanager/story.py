'''Classes and methods for creating and organizing stories
'''

import os
from pathlib import Path
import markdown

from typing import List

class StoryManager:
    '''Maintain list of stories and their metadata
    '''
    def __init__(self):
        self.dir_program = Path(__file__).resolve().parent.parent
        self.dir_story = os.path.join(self.dir_program, 'story')
        self.dir_markdown = os.path.join(self.dir_story, 'markdown')
        self.dir_html = os.path.join(self.dir_story, 'html')

        for d in (self.dir_story, self.dir_markdown, self.dir_html):
            os.makedirs(d, exist_ok=True)

        self.story_list: List[str] = self.get_file_list(self.dir_story)
        self.markdown_list: List[str] = self.get_file_list(self.dir_markdown)

        # TEMP
        self.convert_all_markdown_files()
        self.pack_story_html()
        
        return
    
    def get_file_list(self, path: str) -> List[str]:
        '''Return a list of files in a given directory
        '''
        
        file_list: List[str] = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file_list.append(os.path.join(root, file))
            break

        return file_list
    
    def convert_all_markdown_files(self):
        '''Convert markdown files to html
        '''
        for md in self.markdown_list:
            self.convert_markdown_html(md)

        return
    
    def convert_markdown_html(self, md_path: str) -> None:
        with open(md_path, 'r') as f:
            md_text = f.read()
            html = markdown.markdown(md_text)

            md_filename = os.path.split(md_path)[1]
            file_base = os.path.splitext(md_filename)[0]
            html_file = os.path.join(self.dir_html, file_base + '.html')

            with open(html_file, 'w') as f_html:
                f_html.write(html)

        return
    
    def pack_story_html(self):
        return


class Story:
    '''An individual story (post to the site)
    '''
    def __init__(self):
        self.attachments: List[str] = []
        self.dt: str 
        self.prev: str = ''
        self.next: str = ''
        return