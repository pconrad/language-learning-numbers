# language-learning-numbers
Python module for learning numbers in various languages


The module provides a list of supported languages (e.g. `'English'`, `'Spanish'`), etc. identified by the language name spelled in
English with a capital letter as a string.

In some languages, there may be more than one way to represent a
number.  For example:

* in Mandarin Chinese, we have simplified characters (, the trandiFor languages where there may be both a native
script as well as a phonetic representation, e.g. Mandarin, the
separate representations are provided separately, for example:
`'Mandarin-Pinyin'`, `'Mandarin-Simplified-Characters'`,
`'Persian-Numerals'`, `'Persian-Words'`, `'Persian-Phonetic'`).

For each supported language, the module provides access to the words for the numbers in that language from zero up to some maximum value (available via `max_number(language)`.

The main functions provided are:
* For each supported language, if the language is represented using a romthere are predicate functions (functions that return True or False) to indicate wheth

Examples:
* if `max_number('Mandarin') returns 5, then the numbers 0 through 5 are available in Mandarin.  Asking for 6 or higher will result in a ValueError being thrown.



Usage:

```
from language_learning_numbers import *
```

* `languages_supported()` returns a list of strings that is the languages that are supported

* `highest(language)` returns an integer, the highest number supported in that language

