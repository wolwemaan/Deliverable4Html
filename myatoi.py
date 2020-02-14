
import re
import math
class Solution:
    def myAtoi(self, str: str) -> int:
        max=2147483648
        #p = re.compile("\s*([-+]?\d+).*")
        #str="sas42"
        #str="-91283472332"
        #str="456 with words"
        #str="-2147483647"
        j = re.match( r'\s*([-+]?\d+)\D*', str, re.M)
        if j:
            m = j.group(1)
            result = int(m)
            if result >= max-1:
                return max-1
            elif result <= 0-max:
                return 0-max
        try:
            return result
        except:
            return 0 
