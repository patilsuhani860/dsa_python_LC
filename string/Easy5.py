class Solution(object):
    def addBinary(self, a, b):
        # Pad the shorter string with leading zeros to make lengths equal
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        result = ""
        c = "0"  # This is your carry variable
        
        # Start adding from right to left using your index style
        for i in range(max_len):
            # single loop replaces nested loop to process matching positions
            bit_a = a[len(a) - 1 - i]
            bit_b = b[len(b) - 1 - i]
            
            # Case 1: Both bits are 0
            if bit_a == "0" and bit_b == "0":
                if c == "1":
                    result = "1" + result
                    c = "0"
                else:
                    result = "0" + result
                    
            # Case 2: One bit is 1, the other is 0
            elif (bit_a == "0" and bit_b == "1") or (bit_a == "1" and bit_b == "0"):
                if c == "1":
                    result = "0" + result
                    c = "1"
                else:
                    result = "1" + result
                    
            # Case 3: Both bits are 1
            else:
                if c == "1":
                    result = "1" + result
                    c = "1"
                else:
                    result = "0" + result
                    c = "1"
                    
        # If a carry remains at the very end, prepend it
        if c == "1":
            result = "1" + result
            
        return result
