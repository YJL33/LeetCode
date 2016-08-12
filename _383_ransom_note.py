"""
383. Ransom Note

 Given :
an  arbitrary  ransom  note  string, 
and  another  string  containing  letters from  all  the  magazines, 

write  a  function  that:
return  true  if  the  ransom  note  can  be  constructed  from  the  magazines;
otherwise,  it  will  return  false.

Each  letter  in  the  magazine  string  can  only  be  used  once  in  your  ransom  note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dct_m = {}

        for c in magazine:
            if c not in dct_m:
                dct_m[c] = 1
            else:
                dct_m[c] += 1

        for l in ransomNote:
            if l in dct_m:
                dct_m[l] -= 1
                if dct_m[l] == 0: del dct_m[l]
            else:
                return False

        return True