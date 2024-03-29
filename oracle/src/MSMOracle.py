from Predictor import Predictor
class MSMOracle(Predictor):

    def __init__(self):
        super().__init__("MSM", "tab")

    def predictNextNumber(self):
        sequence = self.getNumberSequence()
        digits  = len(str(sequence[0]))
        last_number = sequence[-1]
        seed_str = str(last_number**2).zfill(digits*2)
        mid = len(seed_str) // 2
        
        self.setNextNumberPredicted(int(seed_str[mid-digits//2:mid+digits//2]))


# to generate MSQ sequence https://sadale.net/27/online-middle-square-method-generator
