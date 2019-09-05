# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 18:30:26 2019

@author: Arjan
"""

class oneAway:
    def __init__(self, origin, modified):
        self.origin = origin
        self.modified = modified
        
    def isInserted(self):
        remainder = len(self.origin) - len(self.modified)
        newModified = self.modified + ("0" * remainder)
        skips = 0
        j = 0
        for i in range(0, len(self.origin)):
            if skips >= 1:
                    return False
            if self.origin[i] != newModified[j]:
                j = j + 1
                skips = skips + 1
            j = j + 1
        return True        
    
    def isDeleted(self):
        remainder = len(self.modified) - len(self.origin)
        newOrigin = self.origin + ("0" * remainder)
        skips = 0
        j = 0
        for i in range(0, len(self.modified)):
            if skips >= 1:
                    return False
            if self.modified[i] != newOrigin[j]:
                j = j + 1
                skips = skips + 1
            j = j + 1
        return True   
    
    def isReplaced(self): #last test
        mistakes = 0
        for i in range(0, len(self.origin)):
            if self.origin[i] != self.modified[i]:
                mistakes = mistakes + 1
        if mistakes > 1:
            return False
        else:
            return True
        
    def isOneAway(self):
        if len(self.origin) > len(self.modified):
            if self.isInserted():
                return True
        elif len(self.origin) < len(self.modified):
            if self.isDeleted():
                return True
        elif len(self.origin) == len(self.modified):
            if self.isReplaced():
                return True
        return False
                
stringTest = oneAway("pale", "pals")
print(stringTest.isOneAway())