from Source import Source

class RandomOrgSource(Source):

    def __init__(self):
        super().__init__("Random Org", "tab")

    def getRandomSequence(self, lengthTab):
        return