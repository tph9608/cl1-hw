# Author: YOUR NAME HERE
# Date: DATE SUBMITTED

# Use word_tokenize to split raw text into words
from string import punctuation
import string
import nltk
from nltk.tokenize import word_tokenize

class LimerickDetector:

    def __init__(self):
        """
        Initializes the object to have a pronunciation dictionary available
        """
        self._pronunciations = nltk.corpus.cmudict.dict()
#        print(self._pronunciations["tree"])
#        print(self._pronunciations["debris"])
    def num_syllables(self, word):
        """
        Returns the number of syllables in a word.  If there's more than one
        pronunciation, take the shorter one.  If there is no entry in the
        dictionary, return 1.
        """
        
        if word in self._pronunciations.keys():
            A = self._pronunciations[word]
            min_length_a = []
            min_length = 1e3
            for a in A:
                if len(a)<min_length:
                    min_length = len(a)
                    min_length_a = a
            count = len([p for p in min_length_a if p[-1].isdigit()])
            return count
            
        return 1

    def rhymes(self, a, b):
        """
        Returns True if two words (represented as lower-case strings) rhyme,
        False otherwise.
        """
        
        for pa in self._pronunciations[a]:
            for pb in self._pronunciations[b]:
  
                index_a = -1
                index_b = -1
                
                for index in range(len(pa)):
                    p = pa[index]
                    if p[-1].isdigit():
                        index_a = index
                        break
                        
                for index in range(len(pb)):
                    p = pb[index]
                    if p[-1].isdigit():
                        index_b = index
                        break
#
#                print("pa:",pa)
#                print("pb:",pb)
#                print(len(pb)-index_a+1)
#                print("pa[index_a:end]:",pa[index_a:])
#                print("pb(...):end]:",pb[len(pb)-len(pa[index_a:]):])
#
        #        print(pb[len(pb)-index_a+1:])
                if len(pa)<len(pb) and pa[index_a:]==pb[len(pb)-len(pa[index_a:]):]:
                    return True
                elif len(pa)>len(pb) and pa[len(pa)-len(pb[index_b:]):]==pb[index_b:]:
                    return True
                elif len(pa)==len(pb) and pa[index_a:]==pb[index_b:]:
                    return True
                
        return False

    def is_limerick(self, text):
        """
        Takes text where lines are separated by newline characters.  Returns
        True if the text is a limerick, False otherwise.

        A limerick is defined as a poem with the form AABBA, where the A lines
        rhyme with each other, the B lines rhyme with each other (and not the A
        lines).

        (English professors may disagree with this definition, but that's what
        we're using here.)
        """
        
        indexes = []
        for i,t in enumerate(text):
            if t == "\n":
                indexes.append(i)
#        print("indexes:",indexes)
        lastwords = []
        

        for k, index in enumerate(indexes):
            words = []
#            print("k:",k)
            if k==0:
                words = word_tokenize(text[:index])
                words=[word.lower() for word in words if word.isalpha()]
#                print("words:",words);
                if words:
                    lastwords.append(words[-1])
                    
            elif k == len(indexes)-1:
                words = word_tokenize(text[indexes[k-1]:index])
                words=[word.lower() for word in words if word.isalpha()]
#                print("words:",words);
                if words:
                    lastwords.append(words[-1])
                words = word_tokenize(text[index:])
                words=[word.lower() for word in words if word.isalpha()]
#                print("words:",words);
                if words:
                    lastwords.append(words[-1])
            else:
                words = word_tokenize(text[indexes[k-1]:indexes[k]])
                words=[word.lower() for word in words if word.isalpha()]
#                print("words:",words);
                if words:
                    lastwords.append(words[-1])
            
#            print("last words:",lastwords)
            
        if len(lastwords)!=5:
            return False
        else:
            A = []
            B = []
            A.append(lastwords[0])
            A.append(lastwords[1])
            A.append(lastwords[4])
                
            B.append(lastwords[2])
            B.append(lastwords[3])
                
                
        returned = True
        for i in range(len(A)-1):
            if not self.rhymes(A[i],A[i+1]):
                returned = False
        for i in range(len(B)-1):
            if not self.rhymes(B[i],B[i+1]):
                returned = False
#
        return returned

if __name__ == "__main__":

    ld = LimerickDetector()
#    print(ld.num_syllables("asdf"))
    
    g = """There was a young lady one fall
    Who wore a newspaper dress to a ball.
    The dress caught fire
    And burned her entire
    Front page, sporting section and all."""
    
    print(ld.is_limerick(g))
    
#    print(ld.rhymes("tree", "debris"))
   
#    buffer = ""
#    inline = " "
#    while inline != "":
#        buffer += "%s\n" % inline
#        inline = input()
#
#    ld = LimerickDetector()
#
#
#    print("%s\n-----------\n%s" % (buffer.strip(), ld.is_limerick(buffer)))
