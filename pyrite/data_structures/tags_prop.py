# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

from post_properties import PostProperty 

def parse(tags_raw): 
    return Tags(tags.split(","))

class Tags(PostProperty):
    """
    Stores a list of topic-tags
    """
    def __init__(self, tags):
        """
        Constructor should only be accessed by parse method.
        """
        PostProperty.__init__(self, "post_tags")
        self.tags = tags

    def compile(self):
        output = ""
        for item in self.tags:
          output += PostProperty.compile(self, item)
        return output