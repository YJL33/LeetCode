"""
468
"""
import string
class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        ipv4Cnt, ipv6Cnt, last = 0, 0, ""
        prev = 0
        for i in range(len(IP)):
            if IP[i] == '.':
                if self.checker1(IP[prev:i], ipv6Cnt==0):
                    ipv4Cnt += 1
                    prev = i+1
                else:
                    break
            elif IP[i] == ':':
                if self.checker2(IP[prev:i], ipv4Cnt==0):
                    ipv6Cnt += 1
                    prev = i+1
                else:
                    break
            elif i == len(IP)-1:
                last = IP[prev:]
                if ipv4Cnt == 3 and self.checker1(last, ipv6Cnt==0):
                    return 'IPv4'
                elif ipv6Cnt == 7 and self.checker2(last, ipv4Cnt==0):
                    return 'IPv6'

        return 'Neither'
        
    def checker1(self, x, flag):
        return x.isdigit() and len(str(int(x))) == len(x) and 0 <= int(x) <= 255 and flag
    
    def checker2(self, x, flag):
        return 1 <= len(x) <= 4 and all(c in string.hexdigits for c in x) and flag

print(Solution().validIPAddress("172.16.254.1"))
print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
print(Solution().validIPAddress("256.256.256.256"))
print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334:"))
print(Solution().validIPAddress("1e1.4.5.6"))