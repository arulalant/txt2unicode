txt2unicode
===========
Tamil Text Encode to Unicode Converter.

Don't you know what is your text encode ? Don't worry. This `txt2unicode` will find it & convert to unicode for you :-)


Available Tamil Encode Converters
=================================

| S.No  | எழுத்துரு | Encode Name | To Unicoce Converter | To Encode Convereter |
| ---- | :---------: | :---------: | :---------: | :---------: |
| 1 | அஞ்சல் | Anjal | anjal2unicode | unicode2anjal|
| 2 |  பாமினி | Bamini|  bamini2unicode| unicode2bamini|
| 3 | பூமி  | Boomi  |  boomi2unicode| unicode2boomi| 
| 4 | தினகரன் | Dinakaran |  dinakaran2unicode | unicode2dinakaran|
| 5 | தினமணி  | Dinamani  | dinamani2unicode  | unicode2dinamani ||
| 6 | தினத்தந்தி |Dinathanthy |  dinathanthy2unicode|unicode2dinathanthy|
| 7 |  கவிபிரியா |  Kavipriya  | kavipriya2unicode| unicode2kavipriya|
| 8 | முரசொலி | Murasoli |  murasoli2unicode | unicode2murasoli |
| 9 | மலை  |  Mylai    |mylai2unicode      | unicode2mylai|
| 10| நக்கீரன்  |Nakkeeran|     nakkeeran2unicode| unicode2nakkeeran|
| 11| ரோமன்   | Roman   | roman2unicode  | unicode2roman |
| 12| டேப்    | Tab  | tab2unicode  | unicode2tab|
| 13| டாம்   |  Tam  |tam2unicode | unicode2tam|
| 14| டிஸ்கி |Tscii  |    tscii2unicode|   unicode2tscii|
| 15| கண்டுபுடி| AutoFind | **auto2unicode**|      --   |


Auto Find Input Encode & Convert to Unicode
===========================================

  `auto2unicode` function will try to find encode of input text. If it is found, then it will convert input text to unicode using appropriate encode converters among available encode converters.
  
  Out of 14 encodes, 11 encodes can be found by this `auto2unicode`. 
  
  Except `dinamani`, `nakkeeran` & `tam` encodes, `auto2unicode` function can find input text's encode and will convert it into unicode. [Why?](example/encodes_chars/README.md)
  
  Look at demo for [auto2unicode](example/demo_auto2utf8.py)
  
  Look at limitation of `auto2unicode` [here](example/encodes_chars/README.md)
  
  
Convert From Unicode to Encode
==============================
  Here reverse engine of `encode2unicode` used to convert back to encode from unicode.
  Look at above table for available `unicode2encode` functions.
  Look demo for `unicode2tscii` converter [here](example/demo_utf8_2_tscii.py)
  

Test Status:
===========
  1. auto2unicode works
  2. tscii2unicode works
  3. unicode2tscii works
   


Todo:
====
  * Need to test all the above encodes
  * Need to add fonts2unicode converter for the above encodings
  

Credits:
=======
  Thanks to http://kandupidi.com/converter/ online tool.
  
Regards,

Arulalan.T
  
