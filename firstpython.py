def bit_length(self):
    s = bin(self)       # binary representation:  bin(-37) --> '-0b100101'
    t = s.lstrip('-0b') # remove leading zeros and minus sign
    return len(t)      
