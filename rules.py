__author__ = 'johnny'

class Rule:
    def action(self, block, handler):
        handler.start(self.type)
        handler.end(self.type)
        handler.feed(block)
        return True

class HeadingRule(Rule):
    """
    标题是一个最多70个字符的行，不以冒号结束
    """
    type = 'heading'
    def condition(self, block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

class TitleRule(HeadingRule):
    """
    题目是文档的第一个块，作为标题存在
    """
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first: return False
        self.first = False
        return HeadingRule.conditon(self, block)

class ListItemRule(Rule):
    