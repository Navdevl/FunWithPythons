# -*- encoding: utf-8 -*-
# Alohomora is a spell used in HarryPotter that can open any sealed doors.!

import sys
from urllib2 import urlopen
import re

# Modify the tracebacklimit to 1 if you want to see the whole error statements
# I hide those traceback statements because I find it annoying NOW. Just Now..!
sys.tracebacklimit = 0

class Alohomora():
    def __init__(self, collection=None, word=None):
        self.collection = collection
        self.word = word

    def magic(self):
        if self.collection is None or self.word is None:
            raise ValueError('Input(s) should not be empty')

        if len(self.collection) < len(self.word):
            return False

        for character in self.word:
            if re.search(character, self.collection) is not None:
                # Remove the character from collection
                # This helps in the time where there are characters repeated
                # Without third parameter in replace(), it replaces all occurrences.
                # I commented about the replace() because, I had hard time finding why all my occurrences are replaced.

                self.collection = self.collection.replace(character, '', 1)

            elif re.search('\?', self.collection) is not None:
                # Same as above. Removing '?' Now
                self.collection = self.collection.replace('?','', 1)

            else:
                # Bad Luck. No matches found. Bye Bye. Say 'False' to everyone
                return False

        return True

    def longest(self):
        if self.collection is None:
            raise ValueError('Input should not be empty')
        longest_string = ""
        # Our Magic function overwrites on collection. So having a temporary hold to it here.
        # I could have made temporary either on Magic() or Longest(). I preferred Longest(). Nothing Special
        collection = self.collection
        dictionary = urlopen("https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/dotnetperls-controls/enable1.txt").read()
        for word in dictionary.split():
            self.collection = collection
            self.word = word
            # Using the same algorithm used in MAGIC. DRY - Do Not Repeat,dude.!
            if self.magic():
                if len(longest_string)<len(word):
                    longest_string = word
        return longest_string
