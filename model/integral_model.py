from sympy import symbols, integrate, simplify, apart, diff
from sympy.parsing.sympy_parser import parse_expr

x, u = symbols("x u")

class Integral_Model:
    def solve_integral(self, expr_str, method, a = None, b = None):
        expr = simplify(parse_expr(expr_str))
        
        if method == 'indefinite':
            result = integrate(expr, x)
            steps = f"Indefinite integral of {expr} with respect to x."
            
        elif method == 'definite':
            if a is None or b is None:
                raise ValueError("Limits must be provided for definite integral.")
            result = integrate(expr(x, a, b))
            steps = f"Definite integral of {expr} from {a} to {b}."
        
        elif method == 'by parts':
            if expr.is_Mul:
                u_expr = expr.args[0]
                dv_expr = expr / u_expr
            else:
                u_expr = x
                dv_expr = expr
            
            v_expr = integrate(dv_expr, x)
            du_expr = diff(u_expr, x)
            result = u_expr * v_expr - integrate(v_expr * du_expr, x)
            steps = f"Integration by parts with u  = {u_expr}, dv = {dv_expr}."
            
        elif method == 'substitution':
            substituted_expr = expr.subs(x, u)
            result_u = integrate(substituted_expr, x)
            result = result_u.subs(u, x)
            steps = f"Substitution method with u = x: integral becomes ∫({substituted_expr}) du = {result_u}."
            
        elif method == 'partial fractions':
            partials = apart(expr, x)
            result = integrate(partials, x)
            steps = f"Partial fraction descomposition = {partials}."
            
        else:
            raise ValueError(f"Unknown integration method: {method}")
        
        return steps, result
                