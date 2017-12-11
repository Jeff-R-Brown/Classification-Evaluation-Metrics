
class CMatrix:
    
    def __init__(self):
        self.TP = 0.0
        self.FP = 0.0
        self.TN = 0.0
        self.FN = 0.0
        self.F1 = 0.0
        self.Accuracy = 0.0
        self.Sensitivity = 0.0      # Recall or true positive rate
        self.Specificity = 0.0      # True negative rate
        self.Precision = 0.0        # Positive predictive power
    
    def evaluate(self, y_hats, y_true):
        i = 0
        for y in y_true.iteritems():
            if(y_hats[i] == 1 and y[1] == 1):
                # True Positive
                 self.TP += 1
            if(y_hats[i] == 1 and y[1] == 0):
                # False Positive
                self.FP += 1
            if(y_hats[i] == 0 and y[1] == 0):
                # True Negative
                self.TN += 1
            if(y_hats[i] == 0 and y[1] == 1):
                # False Negative
                self.FN += 1
            i += 1
            
        # Calculates Accuracy Score
        self.Accuracy = (self.TP + self.TN) / len(y_true)
        
        # Calculates Sensitivity
        if self.TP == 0:
            self.Sensitivity = 0
        else:
            self.Sensitivity = self.TP / (self.TP + self.FN)
         
        # Calculates Precision
        if self.TP == 0 and self.FP == 0:
            self.Precision = 1
        else:
            self.Precision = self.TP / (self.TP + self.FP)
        
        # Calculates F1 Score
        if self.Precision == 0 and self.Sensitivity == 0:
            self.F1 = 0
        else:
            self.F1 = 2 * (self.Precision * self.Sensitivity) / \
            (self.Precision + self.Sensitivity)


        
        # Calculatates Specificity
        self.Specificity = self.TN / (self.TN + self.FP)    
        
