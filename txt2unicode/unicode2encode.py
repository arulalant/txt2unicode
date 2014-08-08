#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
#                                                                            #
# Author : Arulalan.T <arulalant@gmail.com>                                  #
# Date : 08.08.2014                                                          #
#                                                                            #
# This file is part of txt2unicode                                           #
#                                                                            #
# txt2unicode is free software: you can redistribute it and/or               #
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


def unicode2encode(text, charmap):
    '''
    charmap : dictionary which has both encode as key, unicode as value
    '''
    if isinstance(text, (list, tuple)):
        unitxt = ''
        for line in text:
            for val,key in charmap.iteritems():  
                if key in text:
                    line = line.replace(key, val)
                # end of if val in text:
            unitxt += line
        # end of for line in text:
        return unitxt
    elif isinstance(text, str):
        for val,key in charmap.iteritems():
            if key in text: 
                text = text.replace(key, val)
        # end of for val,key in charmap.iteritems():
        return text
    # end of if isinstance(text, (list, tuple)):
# end of def unicode2encode(text, charmap):

def unicode2anjal(text):
    return unicode2encode(text, anjal2utf8)

def unicode2bamini(text):
    return unicode2encode(text, bamini2utf8)

def unicode2boomi(text):
    return unicode2encode(text, boomi2utf8)

def unicode2dinakaran(text):
    return unicode2encode(text, dinakaran2utf8)

def unicode2dinamani(text):
    return unicode2encode(text, dinamani2utf8)

def unicode2dinathanthy(text):
    return unicode2encode(text, dinathanthy2utf8)

def unicode2kavipriya(text):
    return unicode2encode(text, kavipriya2utf8)

def unicode2murasoli(text):
    return unicode2encode(text, murasoli2utf8)

def unicode2mylai(text):
    return unicode2encode(text, mylai2utf8)

def unicode2nakkeeran(text):
    return unicode2encode(text, nakkeeran2utf8)

def unicode2roman(text):
    return unicode2encode(text, roman2utf8)

def unicode2tab(text):
    return unicode2encode(text, tab2utf8)

def unicode2tam(text):
    return unicode2encode(text, tam2utf8)

def unicode2tscii(text):
    return unicode2encode(text, tscii2utf8)

