`all.encodes.common.chars.txt` files contains commonly available 773 characters 
among all encodings.

So if your input text fully falls only unders the characters of 
[all.encodes.common.chars.txt](all.encodes.common.chars.txt), then auto2unicode will fails.


Look at the files `dinamani2utf8.unique.chars.txt` and `nakkeeran2utf8.unique.chars.txt'

It seems these two encodes characters are fully falls under commonly available
773 characters `[all.encodes.common.chars.txt](all.encodes.common.chars.txt)


**Tip** : If you need to find auto encode of your input text, then make sure that
atleast one char from encode_name.unique.chars.txt file available in your 
input text.


eg 1:
====

text = """¾¢ÕÅûÙÅ÷ 
«ÕÇ¢Â ¾¢ÕìÌÈû  """

uni = tscii2unicode(text)

unicode for above tscii characters are as below

திருவள்ளுவர் 
அருளிய திருக்குறள்  


eg 2:
=====
text = """¾¢ÕÅûÙÅ÷ 
«ÕÇ¢Â ¾¢ÕìÌÈû  """

uni = auto2unicode(text)

*It print follow msg and return None.*

**"Need more words to find unique encode out of 773 chars"**


eg 3:
=====
text = """¾¢ÕÅûÙÅ÷ 
«ÕÇ¢Â ¾¢ÕìÌÈû  """

uni = auto2unicode(text)

*It print follow msg and return converted unicode characters.*

**"Whola! found encode :  tscii2utf8"**

unicode for above tscii characters are as below

திருவள்ளுவர் அருளிய திருக்குறள்  ௭


note the last char '' in above tscii variable string in eg3 is added compare
with eg2, because to make distingush from available common chars among all 
encodings in `all.encodes.common.chars.txt`.  

'' char works for 'tscii' encode.
for other encodes user need to look at this `encodes_chars` directory files &
identigy atleast one unique char, incert in input text. so that auto2unicode
can identiy encode for you ! 


Regards,

Arulalan.T 

Date : 04.08.2014





