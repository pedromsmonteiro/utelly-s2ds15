import re
def _convert_nn(val):
    to_19 = ( 'zero',  'one',   'two',  'three', 'four',   'five',   'six',
              'seven', 'eight', 'nine', 'ten',   'eleven', 'twelve', 'thirteen',
              'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' )
    tens  = ( 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
    if val < 20:
        return to_19[val]
    for (dcap, dval) in ((k, 20 + (10 * v)) for (v, k) in enumerate(tens)):
        if dval + 10 > val:
            if val % 10:
                return dcap + '-' + to_19[val % 10]
            return dcap

def _convert_nnn(val):
    to_19 = ( 'zero',  'one',   'two',  'three', 'four',   'five',   'six',
              'seven', 'eight', 'nine', 'ten',   'eleven', 'twelve', 'thirteen',
              'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' )
    word = ''
    (mod, rem) = (val % 100, val // 100)
    if rem > 0:
        word = to_19[rem] + ' hundred'
        if mod > 0:
            word += ' '
    if mod > 0:
        word = word + _convert_nn(mod)
    return word

def english_number(val):
    denom = ( '',
              'thousand',     'million',         'billion',       'trillion',       'quadrillion',
              'quintillion',  'sextillion',      'septillion',    'octillion',      'nonillion',
              'decillion',    'undecillion',     'duodecillion',  'tredecillion',   'quattuordecillion',
              'sexdecillion', 'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion' )
    if val < 100:
        return _convert_nn(val)
    if val < 1000:
        return _convert_nnn(val)
    for (didx, dval) in ((v - 1, 1000 ** v) for v in range(len(denom))):
        if dval > val:
            mod = 1000 ** didx
            l = val // mod
            r = val - (l * mod)
            ret = _convert_nnn(l) + ' ' + denom[didx]
            if r > 0:
                ret = ret + ', ' + english_number(r)
            return ret

def roman_to_int(n):
    numeral_map = zip(
        (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
        ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    )
    n = unicode(n).upper()

    i = result = 0
    for integer, numeral in numeral_map:
        while n[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result

def roman_to_int_repl(match):
    numeral_map = zip(
        (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
        ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    )
    return str(roman_to_int(match.group(0)))

def roman_replace(text):
    regex = re.compile(r'\b(?!(I)\b)(?=[MDCLXVI]+\b)M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\b')
    return regex.sub(roman_to_int_repl, text)

def strip_accents(s):
    import unicodedata
    if type(s) == str:
            s = s.decode('utf-8','ignore')
            s = unicode(s)
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')) if s else ""



def gen_seo_name(text, separator='-'):
    text = strip_accents (text)
    map = {
        ' ': '-',
        '.': '',
        '&': 'and',
        '$': '',
        ':': '',
        ',': '',
        '/': '',
        '[': '',
        ']': '',
        '\'': '',
        '?': '',
        '(': '',
        ')': '',
        '"': '',
        '+': 'plus',
        '*': 'star'

    }
    #replace roman numbers to numbers
    text = roman_replace(text)
    #convert number to string
    tstr = text
    for number in re.findall(r'\d+', tstr):
        text = text.replace(number,english_number(int(number)), 1)

    text = text.lower()
    #remove all subsequent spaces
    text = re.sub(' +',' ', text)
    # if ch does not exists in the map return ch
    str = ''.join([map.get(ch,ch) for ch in text])
    str = re.sub(r'[^a-zA-Z0-9\- ]', '', str)
    # now we need to clear all types of __ ___ ____ to _
    str = re.sub('_+', '_', str)
    #remove all subsequent -
    str = re.sub('-+', '-', str)
    # remove the last underscore if exist
    str = str[0:-1] if str[-1:] == '-' else str
    #replace - to any char you want
    str = str.replace('-', separator)
    return str

print gen_seo_name('hi! this is a test IV 800')