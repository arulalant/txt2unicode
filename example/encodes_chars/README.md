For better understanding, you better look at this [README.md](README.md) file in **vim** or **gedit** or **Emacs** text editor, **not in web browser** !

Look at all available files of `encodes_chars` directory [here]() 

`all.encodes.common.chars.txt` files contains commonly available 773 characters 
among all encodings.

So if your input text fully falls only unders the characters of 
[all.encodes.common.chars.txt](all.encodes.common.chars.txt), then auto2unicode will fails.


Look at the files `dinamani2utf8.unique.chars.txt` and `nakkeeran2utf8.unique.chars.txt`

It seems these two encodes characters are fully falls under commonly available
773 characters [all.encodes.common.chars.txt](all.encodes.common.chars.txt)


**Tip** : If you need to find auto encode of your input text, then make sure that
atleast one char from encode_name.unique.chars.txt file available in your 
input text.


eg 1:
====

```python
>>> text = """¾¢ÕÅûÙÅ÷ 
«ÕÇ¢Â ¾¢ÕìÌÈû  """

>>> uni = tscii2unicode(text)
>>> print uni
```
திருவள்ளுவர் 
அருளிய திருக்குறள்

*unicode for above tscii characters are as shown above*

  


eg 2:
=====

```python
>>> text = """¾¢ÕÅûÙÅ÷ 
«ÕÇ¢Â ¾¢ÕìÌÈû  """

>>> uni = auto2unicode(text)
>>> print uni
```

**"Need more words to find unique encode out of 773 chars"**

*It print above msg and return None.*




eg 3:
=====

```python
>>> text = """¾¢ÕÅûÙÅ÷ 
«ÕÇ¢Â ¾¢ÕìÌÈû  """

>>> uni = auto2unicode(text)
>>> print uni
```

**"Whola! found encode :  tscii2utf8"**

*It print above msg and return converted unicode characters.*

திருவள்ளுவர் அருளிய திருக்குறள்  ௭

*unicode for above tscii characters are as shown above*


Look closely at last char of input & output of `eg 1` & `eg 3` in **vim** or **gedit** or **Emacs** text editor, **not in web browser** !


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





