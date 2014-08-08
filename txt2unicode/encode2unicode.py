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

_all_encodes_dic_ = {'anjal2utf8' : anjal2utf8, 'bamini2utf8' : bamini2utf8,
     'boomi2utf8': boomi2utf8, 'dinakaran2utf8' : dinakaran2utf8,
     'dinamani2utf8': dinamani2utf8, 'dinathanthy2utf8': dinathanthy2utf8,
     'kavipriya2utf8': kavipriya2utf8, 'murasoli2utf8': murasoli2utf8,
     'mylai2utf8': mylai2utf8, 'nakkeeran2utf8': nakkeeran2utf8,
     'roman2utf8': roman2utf8, 'tab2utf8': tab2utf8,
     'tam2utf8': tam2utf8, 'tscii2utf8': tscii2utf8}

# By enable this flage, it will write individual encodes unique & common
# characters in text file.
__WRITE_CHARS_TXT = False


def convert2unicode(text, charmap):
    '''
    charmap : dictionary which has both encode as key, unicode as value
    '''
    if isinstance(text, (list, tuple)):
        unitxt = ''
        for line in text:
            for key,val in charmap.iteritems():
                if key in text:
                    line = line.replace(key, val)
                # end of if key in text:
            unitxt += line
        # end of for line in text:
        return unitxt
    elif isinstance(text, str):
        for key,val in charmap.iteritems():
            if key in text:
                text = text.replace(key, val)
            # end of if key in text:
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
    _all_common_encodes_single_char_ = set([])

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

    for ch in _all_common_encodes_:
        # collect single common chars
        if len(ch) == 1: _all_common_encodes_single_char_.add(ch)
    # end of for ch in _all_common_encodes_:

    # remove single common char from compound common chars
    _all_common_encodes_ -= _all_common_encodes_single_char_

    unique_chars = ''
    if isinstance(text, str):
        text = text.split("\n")
    elif isinstance(text, (list, tuple)):
        pass

    def get_unique_ch(text):

        special_chars = ['.', ',', ';', ':','', ' ', '\r', '\t', '=', '\n']
        for line in text:
            for word in line.split(' '):
                word = unicode(word, 'utf-8')
                for ch in _all_common_encodes_:
                    if ch in word: word = word.replace(ch, '')
                # end of for ch in _all_common_encodes_:

                # if len of word is zero, then go for another word
                if not word: continue

                for ch in word:
                    if ch.isdigit() or ch in special_chars:
                        # remove special common chars
                        word = word.repl(ch, '')
                        continue
                    # end of if ch.isdigit() or ...:
                    # Whola, got unique chars from user passed text
                    return word
                # end of for ch in word:
            # end of for word in line.split(' '):
        # end of for line in text:
        return ''
    # end of def  get_unique_ch(text):

    # get unique word which falls under any one of available encodes from
    # user passed text lines
    unique_chars = get_unique_ch(text)

    if __WRITE_CHARS_TXT:
        # write common compound characters of all encodes
        f = open('all.encodes.common.chars.txt', 'w')
        for ch in _all_common_encodes_:
            ch = ch.encode('utf-8')
            for encode_keys in _all_encodes_dic_.values():
                if ch in encode_keys:
                    uni = encode_keys[ch]
                    break
                # end of if ch in encode_keys:
            # end of for encode_keys in _all_encodes_dic_.values():
            f.write(ch + '  =>  ' + uni + '\n')
        # end of for ch in _all_common_encodes_:
        f.close()
        # write unique compound characters of all encodes
        for encode_name, encode_keys in _all_unique_encodes_:
            f = open(encode_name + '.unique.chars.txt', 'w')
            for ch in encode_keys:
                ch = ch.encode('utf-8')
                uni = _all_encodes_dic_[encode_name][ch]
                f.write(ch + '  =>  ' + uni + '\n')
            # end of for ch in encode_keys:
            f.close()
        # end of for encode_name, encode_keys in _all_unique_encodes_:
    # end of if __WRITE_CHARS_TXT:

    # count common encode chars
    clen = len(_all_common_encodes_)
    msg = "Sorry, couldn't find encode :-(\n"
    msg += 'Need more words to find unique encode out of %d ' % clen
    msg += 'common compound characters'
    if not unique_chars:
        print msg
        return ''
    # end of if not unique_chars:

    for encode_name, encode_keys in _all_unique_encodes_:
        if not len(encode_keys): continue
        for ch in encode_keys:
            # check either encode char is presnent in word
            if ch in unique_chars:
                # found encode
                print "Whola! found encode : ", encode_name
                return convert2unicode(text, encode)
        # end of if if unique_chars.issubset(encode_keys):
    else:
        print msg
        return ''
    # end of for encode in _all_encodes_:
# end of def auto2unicode(text):

