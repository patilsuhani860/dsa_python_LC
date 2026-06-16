class Solution(object):
    def isNumber(self, s):
        s = s.strip()  # Clean whitespaces (your s.split() intended this)
        if not s:
            return False

        # Helper function to validate a pure integer (with optional leading sign)
        def isInteger(string):
            if not string:
                return False
            if string[0] in ["+", "-"]:
                string = string[1:]
            return string.isdigit()

        # Helper function to validate a decimal number (with optional leading sign)
        def isDecimal(string):
            if not string:
                return False
            if string[0] in ["+", "-"]:
                string = string[1:]
            
            if string.count(".") != 1:
                return False
                
            l, r = string.split(".", 1)
            # Valid: "1.2", "1.", ".2" but NOT "."
            if not l and not r:
                return False
            if l and not l.isdigit():
                return False
            if r and not r.isdigit():
                return False
            return True

        # 1. Logic for Exponent ("e" or "E")
        if "e" in s or "E" in s:
            # Handle both lowercase 'e' and uppercase 'E'
            char = "e" if "e" in s else "E"
            if s.count(char) != 1:
                return False
                
            l, r = s.split(char, 1)
            # Left side must be a Decimal OR an Integer. Right side must be an Integer.
            return (isDecimal(l) or isInteger(l)) and isInteger(r)

        # 2. Logic for Decimals and Integers without exponents
        if "." in s:
            return isDecimal(s)
        
        return isInteger(s)
