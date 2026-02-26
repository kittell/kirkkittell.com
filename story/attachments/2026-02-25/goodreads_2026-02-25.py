from pathlib import Path
import pandas as pd
from typing import Dict, Hashable, Any

class Library:
    def __init__(self):

        return
    
    def import_from_goodreads(self, file_path: Path) -> None:
        self.df: pd.DataFrame = pd.read_csv(file_path)
        return
    
    def find_random_book(
            self, 
            read: bool = False
            ) -> Book:
        '''
        Pick a random book from the library

        read: bool = True, if book is on read shelf; False, if book is on to-read shelf
        '''
        book: Book = Book()
        exclusive_shelf: str = 'to-read'
        if read:
            exclusive_shelf = 'read'

        entry = self.df[self.df['Exclusive Shelf'] == exclusive_shelf].sample(n=1).iloc[0].to_dict()
        book.from_goodreads_export(entry)

        return book
    
class Book:
    def __init__(self):
        self.title: str = ''
        return
    
    def __str__(self) -> str:
        output: str = ''
        output = f'{self.title}'
        return output
    
    def from_goodreads_export(self, entry: Dict[Hashable, Any]) -> None:
        self.goodreads_entry = entry
        self.title = self.goodreads_entry['Title']
        return
    

base_dir: Path = Path(__file__).parent
export_file: str = 'goodreads_library_export_2026-02-12.csv'
export_filepath: Path = base_dir / export_file 

library = Library()
library.import_from_goodreads(export_filepath)
random_book: Book = library.find_random_book()
print(random_book)