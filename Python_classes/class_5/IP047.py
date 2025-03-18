def whichone(n):
    # Step 1: Precompute the lengths of the words until we reach or exceed position n
    # The lengths of the words follow a Fibonacci sequence
    lengths = [1, 2]  # Lengths for the first two words: 'A' and 'AB'
    
    # Keep calculating the next length until it's equal to or larger than n
    while lengths[-1] < n:
        next_length = lengths[-1] + lengths[-2]  # Next length is sum of the last two lengths
        lengths.append(next_length)
    
    # Step 2: Initialize the index k to point to the last calculated length
    k = len(lengths) - 1  # This tells us at which stage the total length exceeds or equals n
    
    # Step 3: Iteratively find the character at position n
    while k >= 2:
        if n <= lengths[k - 1]:
            # If n is within the length of the previous word, move to that word
            k -= 1
        else:
            # If n is beyond the previous word, adjust n and move two steps back
            n -= lengths[k - 1]
            k -= 2
    
    # Step 4: Determine the character based on the remaining value of k
    if k == 0:
        return 'A'  # The initial word at k=0 is 'A'
    else:
        # At k=1, the word is 'AB', so return 'A' if n==1, else 'B'
        return 'A' if n == 1 else 'B'
