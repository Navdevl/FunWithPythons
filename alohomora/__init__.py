# -*- encoding: utf-8 -*-
# Alohomora is a spell used in HarryPotter that can open any sealed doors.!

import sys
from urllib2 import urlopen
from collections import Counter

# Modify the tracebacklimit to 1 if you want to see the whole error statements
# I hide those traceback statements because I find it annoying NOW. Just Now..!
sys.tracebacklimit = 0

class Alohomora():

    def magic(self, str1, str2):
        if str1 is None or str2 is None :
            raise ValueError('Input(s) should not be empty')

        # Checking for ? to handle blank tiles in the same program.
        wild_char_count = str1.count('?')
        intersection = Counter(str1) & Counter(str2)
        if len(list(intersection.elements())) + wild_char_count >= len(str2):
            return 1
        else:
            return 0

    def longest(self,string):
        if string is None :
            raise ValueError('Input should not be empty')
        longest_str=""
        dictionary = urlopen("https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/dotnetperls-controls/enable1.txt").read()
        for word in dictionary.split():
            # Using the same algorith used in MAGIC. DRY - Do Not Repeat,dude.!
            if self.magic(string,word):
                if len(longest_str)<len(word):
                    longest_str = word
        return longest_str
