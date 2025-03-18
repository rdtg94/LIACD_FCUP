def approximate_sqrt(x, max_error):
    # Initial estimate
    y_prev = x / 2
    
    while True:
        # Calculate next estimate using the formula
        y_next = 0.5 * (y_prev + x / y_prev)
        
        # Calculate error (difference between consecutive estimates)
        error = abs(y_next - y_prev)
        
        # Check if error is within acceptable threshold
        if error <= max_error:
            return y_next
            
        # Update previous estimate for next iteration
        y_prev = y_next

print( round(approximate_sqrt(2, 0.1),      16) )
print( round(approximate_sqrt(2, 0.05),     16) )
print( round(approximate_sqrt(2, 0.001),    16) )
print( round(approximate_sqrt(2, 0.000001), 16) )