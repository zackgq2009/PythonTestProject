__author__ = 'johnny'
import re

from project001.util import blocks


class Parser:
    """
    A Parser reads a text file. applying rules and controlling a handler
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filter = []
    def addRule(self, rule):
        self.rules.append(rule)
    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)
    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')