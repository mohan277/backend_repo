from enum import Enum

class ReactionChoices(Enum):
    WOW = 'WOW'
    LIT = 'LIT'
    LOVE = 'LOVE'
    HAHA = 'HAHA'
    THUMBS_UP = 'THUMBS-UP'
    THUMBS_DOWN = 'THUMBS-DOWN'
    ANGRY = 'ANGRY'
    SAD = 'SAD'


class PositiveReactions(Enum):
    WOW = 'WOW'
    LIT = 'LIT'
    LOVE = 'LOVE'
    HAHA = 'HAHA'
    THUMBS_UP = 'THUMBS-UP'


class NegativeReactions(Enum):
    THUMBS_DOWN = 'THUMBS-DOWN'
    ANGRY = 'ANGRY'
    SAD = 'SAD'
