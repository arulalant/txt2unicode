#!"usr"bin"env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
from txt2unicode import auto2unicode

# note the last char '' in below tscii variable string is added compare
# to demo_tscii2utf8.py, because to make distingush from available common
# chars among all encodings.  

# '' char works for 'tscii' encode.
# for other encodes user need to look at encodes_chars directory files and
# identigy atleast one unique char, incert in input text. so that auto2unicode
# can identiy encode for you ! 

tscii = """¾¢ÕÅûÙÅ÷ 
«ÕÇ¢Â ¾¢ÕìÌÈû  """

uni = auto2unicode(tscii)
f = open('unicode-result.txt', 'w')
f.write(uni)
f.close()

print "tscii", tscii
print "unicode", uni 
print "converted unicode stored in 'unicode-result.txt' file"

