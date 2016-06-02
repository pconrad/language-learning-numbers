#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Why -*- coding: utf-8 -*- ? See: http://python.org/dev/peps/pep-0263/ 

numbers = {
    'Spanish':['cero', 'uno', 'dos',  'tres','cuatro',
               'cinco','seis','siete','ocho','nueve',
               'diez'], 
    'Mandarin-Pinyin':[u'líng',u'yī',u'èr',u'sān',u'sì',
                      u'wǔ',u'liù',u'qī',u'bā',u'jiǔ',
                      u'shí'],
    'Mandarin-Traditional':[u'零']
}

def languages_supported():
    return numbers.keys()


def limit(language):
    return len(numbers[language])


def val(language,number):
    return numbers[language][number]


