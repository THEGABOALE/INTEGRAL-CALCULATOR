from model.integral_model import Integral_Model

class IntegralController:
    def __init__(self):
        self.model = Integral_Model()
    
    def calculate(self, expresion, method, lower_limit = None, upper_limit = None):
        try:
            a = float(lower_limit) if lower_limit else None
            b = float(upper_limit) if upper_limit else None
            
            steps, result = self.model.solve_integral(expresion, method, a, b)
            return steps, str(result)
        except Exception as e:
            return "Error during calculations", str(e)