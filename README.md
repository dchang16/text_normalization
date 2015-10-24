# text_normalization

Python module for text normalization into canonical form.

## Installation
    git clone https://github.com/dchang16/text_normalization/
    python setup.py install

## Example
```python
import normalization
    
## Whitespace Normalization
# Output: "This is not a normal sentence structure. The spaces are incoherant."
normalization.whitespace("This is not a normal sentence structure .  The spaces are incoherant  .")
    
## Capitalization Normalization
# Output: "This is not capitalized. It should be."
normalization.capitalize("this is not capitalized. it should be.")
    
## Abbreviations Normalization
# Output: "Doctor where were you on August fifth?"
normalization.abbreviations("Dr. where were you on aug 5th?")
    
## British Normalization
# Output: "ax apologize"
normalization.british("axe apologise")
    
## Contractions Normalization
# Output: I will listen to you all
normalization.contractions("I'll listen to y'all")
    
## Spellfix Normalization
# Output: "This sentence is acceptable."
normalization.spellfix("This sentance is acceptible.")
    
## Normalize
# Combines all normalization methods above
# Output: "This is a normal sentence."
normalization.normalize("This is a normal sentence.")
```

## License
The MIT License (MIT)

Copyright (c) 2015

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
