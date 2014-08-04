#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
#                                                                            #
# Author : Arulalan.T <arulalant@gmail.com>                                  #
# Date : 04.08.2014                                                          #
#                                                                            #
# This file is part of txt2uni                                               #
#                                                                            #
# txt2uni is free software: you can redistribute it and/or                   #  
# modify it under the terms of the GNU General Public License as published by#
# the Free Software Foundation, either version 3 of the License, or (at your #
# option) any later version. This program is distributed in the hope that it #
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty#
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General#
# Public License for more details. You should have received a copy of the GNU#
# General Public License along with this program. If not, see                #  
# <http://www.gnu.org/licenses/>.                                            #  
#                                                                            #
############################################################################## 

from encode2utf8 import anjal2utf8, bamini2utf8, boomi2utf8, \
    dinakaran2utf8, dinamani2utf8, dinathanthy2utf8, \
    kavipriya2utf8, murasoli2utf8, mylai2utf8, nakkeeran2utf8, \
    roman2utf8, tab2utf8, tam2utf8, tscii2utf8

_all_encodes_ = {'anjal2utf8' : anjal2utf8, 'bamini2utf8' : bamini2utf8,
     'boomi2utf8': boomi2utf8, 'dinakaran2utf8' : dinakaran2utf8,
     'dinamani2utf8': dinamani2utf8, 'dinathanthy2utf8': dinathanthy2utf8, 
     'kavipriya2utf8': kavipriya2utf8, 'murasoli2utf8': murasoli2utf8,
     'mylai2utf8': mylai2utf8, 'nakkeeran2utf8': nakkeeran2utf8, 
     'roman2utf8': roman2utf8, 'tab2utf8': tab2utf8, 
     'tam2utf8': tam2utf8, 'tscii2utf8': tscii2utf8}

def convert2unicode(text, charmap):
    
    if isinstance(text, (list, tuple)):
        unitxt = ''
        for line in text:
            for key,val in charmap.iteritems():
                line = line.replace(key, val)
            unitxt += line
        # end of for line in text: 
        return unitxt
    elif isinstance(text, str):        
        for key,val in charmap.iteritems():
            text = text.replace(key, val)
        # end of for key,val in charmap.iteritems():
        return text
    # end of if isinstance(text, (list, tuple)):
# end of def convert2unicode(text, charmap):

def anjal2unicode(text):
    return convert2unicode(text, anjal2utf8)

def bamini2unicode(text):
    return convert2unicode(text, bamini2utf8)

def boomi2unicode(text):
    return convert2unicode(text, boomi2utf8)

def dinakaran2unicode(text):
    return convert2unicode(text, dinakaran2utf8)

def dinamani2unicode(text):
    return convert2unicode(text, dinamani2utf8)

def dinathanthy2unicode(text):
    return convert2unicode(text, dinathanthy2utf8)

def kavipriya2unicode(text):
    return convert2unicode(text, kavipriya2utf8)

def murasoli2unicode(text):
    return convert2unicode(text, murasoli2utf8)

def mylai2unicode(text):
    return convert2unicode(text, mylai2utf8)

def nakkeeran2unicode(text):
    return convert2unicode(text, nakkeeran2utf8)

def roman2unicode(text):
    return convert2unicode(text, roman2utf8)

def tab2unicode(text):
    return convert2unicode(text, tab2utf8)

def tam2unicode(text):
    return convert2unicode(text, tam2utf8)

def tscii2unicode(text):
    return convert2unicode(text, tscii2utf8)
    
def auto2unicode(text):
    """
    This function tries to identify encode in available encodings.
    If it finds, then it will convert text into unicode string.
    
    Author : Arulalan.T
    
    04.08.2014
    
    """
    _all_encodes_ = [('anjal2utf8', anjal2utf8), ('bamini2utf8', bamini2utf8),
     ('boomi2utf8', boomi2utf8), ('dinakaran2utf8', dinakaran2utf8),
     ('dinamani2utf8', dinamani2utf8), ('dinathanthy2utf8', dinathanthy2utf8), 
     ('kavipriya2utf8', kavipriya2utf8), ('murasoli2utf8', murasoli2utf8),
     ('mylai2utf8', mylai2utf8), ('nakkeeran2utf8', nakkeeran2utf8), 
     ('roman2utf8', roman2utf8), ('tab2utf8', tab2utf8), 
     ('tam2utf8', tam2utf8), ('tscii2utf8', tscii2utf8)]      
            
    _all_unique_encodes_ = []
    _all_unicode_encodes_ = {}
    _all_common_encodes_ = set([])
    
    for name, encode in _all_encodes_:
        encode_utf8 = set([unicode(ch, 'utf-8') for ch in encode.keys()])
        _all_unicode_encodes_[name] = encode_utf8
    
    _all_unique_encodes_full_ =_all_unicode_encodes_.copy()
    
    for supname, super_encode in _all_unicode_encodes_.iteritems():
        for subname, sub_encode in _all_unicode_encodes_.iteritems():
            if supname == subname: continue
            # get unique of super_encode among other encodings
            super_encode = super_encode - sub_encode             
        # end of for sub_encode in _all_encodes_:        
        # get common for all over encodings
        common = _all_unique_encodes_full_[supname] - super_encode
        # merge common to all encodings common 
        _all_common_encodes_ = _all_common_encodes_.union(common)
        # store super_encode's unique keys with its name
        _all_unique_encodes_.append((supname, super_encode))    
    # end of for supname, super_encode in _all_encodes_:
    
    unique_chars = set([])
    if isinstance(text, str):
        text = text.split("\n")
    elif isinstance(text, (list, tuple)):
        pass
    
    def get_unique_ch(text): 
        
        special_chars = ['.', ',', ';', ':','', ' ', '\r', '\t', '\n', '']
        for line in text:
            for word in line.split(' '):
                word = set(unicode(word, 'utf-8'))
                # get unique chars from user passed word 
                unique_chars = word - _all_common_encodes_
                # if len of unique_chars is zero, then go for another word 
                if not unique_chars: continue
                 
                unique_chars_clean = unique_chars.copy()
                for ch in unique_chars:
                    if ch.isdigit() or ch in special_chars: 
                        # remove special common chars
                        unique_chars_clean.remove(ch)
                        continue
                    # end of if ch.isdigit() or ...:
                    # Whola, got unique chars from user passed text  
                    return unique_chars_clean
                # end of for ch in unique_chars:
            # end of for word in line.split(' '):
        # end of for line in text:   
    # end of def unique_ch(text): 

    unique_chars = get_unique_ch(text)
    clen = len(_all_common_encodes_)
    if not unique_chars:        
        print 'Need more words to find unique encode out of %d chars' % clen                          
        return ''
    # end of if not unique_chars: 
    
    for encode_name, encode_keys in _all_unique_encodes_:  
        if not len(encode_keys): continue
        if unique_chars.issubset(encode_keys):
            # found encode
            print "Whola! found encode : ", encode_name
            return convert2unicode(text, encode)                
        # end of if if unique_chars.issubset(encode_keys):
    else:
        print "Sorry, couldn't find encode"
        print 'Need more words to find unique encode out of %d chars' % clen
        return ''
    # end of for encode in _all_encodes_:
# end of def auto2unicode(text):
        
        
