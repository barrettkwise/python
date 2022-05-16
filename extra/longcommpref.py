class Solution(object):
    def longestCommonPrefix(self, strs):
        ##prefix can only be as large as smallest word
        shortestword = min(strs, key=len)
        length = len(shortestword)
        for word in strs:
            #if the shortest word is not in word, we gotta update it
            if shortestword not in word[:length]:
                index = 0
                
                while index < length:
                #now we're checking each letter
                    if shortestword[index] != word[index]:
                        if index == 0: 
                            return ""
						
                        #if index isn't 0 we update the shortestword
                        shortestword = shortestword[:index]
                        break
                    
                    index += 1
        
        return shortestword