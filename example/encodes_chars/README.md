
Look at all available files of `encodes_chars` directory [here]() 

`all.encodes.common.chars.txt` files contains **commonly available 580 compound characters among all encodings**.

So if your input text fully falls only under the compund characters of 
[all.encodes.common.chars.txt](all.encodes.common.chars.txt), then auto2unicode will fails. :-(


Look at the files `dinamani2utf8.unique.chars.txt` and `nakkeeran2utf8.unique.chars.txt`. There are fully empty.

It seems these two encodes characters are fully falls under commonly available
580 compound characters [all.encodes.common.chars.txt](all.encodes.common.chars.txt).

So there is **zero %** chance to identify `dinamani` and `nakkeeran` encodes using `auto2ecnode` function.

Look at the file [tam2utf8.unique.chars.txt](tam2utf8.unique.chars.txt), it has only one unique compound characters.

So there is (1/580)x100 = **0.1724137931034483 %** chances to indetify `tam` encode using `auto2ecnode` function.


**Tip** : If you need to find auto encode of your input text, then make sure that
atleast one compund characters from encode_name.unique.chars.txt file available in your 
input text. Find your encode unique compound characters [here]() 


#eg 1:#


```python
>>> text = """¾¢ÕÅûÙÅ÷ 
«ÕÇ¢Â ¾¢ÕìÌÈû  """

>>> uni = tscii2unicode(text)
>>> print uni
```
திருவள்ளுவர் அருளிய திருக்குறள்  

*unicode for above tscii characters are as shown above*


#eg 2:#

```python
>>> text = """¾¢ÕÅûÙÅ÷ 
«ÕÇ¢Â ¾¢ÕìÌÈû  """

>>> uni = auto2unicode(text)
>>> print uni
```

**"Whola! found encode :  tscii2utf8"**

*It print above msg and return converted unicode characters.*

திருவள்ளுவர் அருளிய திருக்குறள்  

*unicode for above tscii characters are as shown above*


#eg 3:#

```python
>>> text = """ù£tPùP\[tI
è£n\[nwh ùSô ªþ£ ùaô """

>>> uni = auto2unicode(text)
>>> print uni
```

**"Sorry, couldn't find encode :-(**

**Need more words to find unique encode out of 580 common compound characters"**

*It print above msg and return None.*


Look closely at characters of input & output of `eg 2` & `eg 3` 

In `eg 2` input text has atleast one / more compound characters from [tsciiutf8.unique.chars.txt](tscii2utf8.unique.chars.txt).

But in `eg 3` input fully falls only under the compund characters of 
[all.encodes.common.chars.txt](all.encodes.common.chars.txt). So it couldn't find correct encodes of input text ! 

For other encodes user need to look at this `encodes_chars` [directory]() files &
identigy atleast one unique char, incert in input text. so that auto2unicode
can identiy encode for you ! 


Regards,

Arulalan.T 

Date : 05.08.2014





