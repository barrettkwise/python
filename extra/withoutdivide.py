def divide(dividend: int, divisor: int) -> int:
    isNegative = False if
    (dividend < 0) and (divisor > 0): isNegative = True
        
    elif (dividend > 0) and (divisor < 0):
        isNegative = True
    
    if isNegative == True:
        return max(-2**31, math.trunc(dividend/divisor))
    
    return min(2**31-1, dividend//divisor)
