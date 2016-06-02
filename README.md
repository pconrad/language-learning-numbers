# language-learning-numbers
Python module for learning numbers in various languages


The module provides a list of supported languages (e.g. `'English'`, `'Spanish'`), etc. identified by the language name spelled in
English with a capital letter as a string.

In some languages, there may be more than one way to represent a
number.  For example:

* In *Mandarin Chinese*, we have 
 - Pinyin (a phonetic transliteration) (for example, ten-thousand is  wàn)
 - Traditional characters (for example, ten-thousand is 萬)
 - Simplified characters (for example,ten-thousand is 万)

* In *Persian* (also known by the endonym *Farsi*), we have: 
 - The words for numbers as written in Persian script (for example, five is پنج	)
 - The words for numbers written phonetically (for example, five is panj)
 - The symbols uses for numbers in Persian text (for example, five is ۵)
 
For these, variants, we simply describe these as separate languages, e.g. `'Mandarin-Pinyin'`, `'Mandarin-Simplified-Characters'`, `'Persian-Numerals'`, `'Persian-Script'`, `'Persian-Phonetic'`).

For each supported language, the module provides access to representations of the number from zero up to some maximum value (available via `max_number(language)`.

The main functions provided are:
* For each supported language, if the language is represented using a romthere are predicate functions (functions that return True or False) to indicate wheth

Examples:
* val('Spanish',2) returns `'dos'`
* val('Mandarin-Pinyin',2) returns `'èr'`
* if `limit('Mandarin-Pinyin')` returns 5, then the numbers 0 through 4 are available in Mandarin-Pinyin.  Asking for `val('Manarin-Pinyin',6) will result in a `ValueError` being thrown as an exception.


Usage:

```
from language_learning_numbers import val
from language_learning_numbers import limit

for i in range(limit('Spanish')):
   print "The Spanish word for ",i," is ",val('Spanish',i)
   
```

* `languages_supported()` returns a list of strings with the supported languages
* `limit(language)` returns an integer, one more than the highest number available in the language.  The integers from zero up to that limit minus one are available.
