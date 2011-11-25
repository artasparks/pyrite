# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

import properties 

class Parser(object):
    def __init__(self, parse_type, css_class):
        self.css_class = css_class

    def parse(self, string): 
        return Title(string, self.css_class)

class Title(object):
    def __init__(self, title, css_class):
        """
        Constructor should be only accessed by parse method.
        """
        self.css_class = css_class
        self.title = title

    def to_string(self):
        return self.title

    def display_ast(self, indents):
        indenting = indents * "  "
        return indenting + "Title:" + self.to_string() + "\n"

    def generate(self):    # self.divId is the name of the HTML class
        return properties.generate_html(
            self.css_class, self.render_content())

    def render_content(self): 
        return self.title
