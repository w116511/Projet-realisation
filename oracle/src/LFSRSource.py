from Source import Source

class LFSRSource(Source):

    def __init__(self):
        super().__init__("LFSR", "tab")

    def getRandomSequence(self, lengthTab):
        return