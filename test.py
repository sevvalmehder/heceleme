__author__ = 'teknokrat-as'

def hypo(x):
    i = 0
    vw = "aeıioöuü"
    cn = "bcçdfgğhjklmnprsştvyz"
    while i < len(x):
        if x[i] in vw:
            if i + 1 < len(x) and x[i+1] in vw:
                return x[0:i+1] + "-" + hypo(x[i+1:len(x)])
            elif i + 2 < len(x) and x[i+2] in vw:
                return x[0:i+1] + "-" + hypo(x[i+1:len(x)])
            elif i + 3 == len(x) and x[i+1] in cn and x[i+2] in cn:
                return x[0:i+3] + "-" + hypo(x[i+3:len(x)])
            elif i + 3 < len(x) and x[i+3] in vw:
                return x[0:i+2] + "-" + hypo(x[i+2:len(x)])
            elif i+3 < len(x) and x[i+1] in cn and x[i+2] in cn and x[i+3] in cn:
                return x[0:i+3] + "-" + hypo(x[i+3:len(x)])
            elif i + 3 < len(x) and x[i:i+3] == 'str' or 'ktr' or 'ntr':
                return x[0:i+2] + "-" + hypo(x[i+2:len(x)])
            else:
                return x[0:i+3] + "-" + hypo(x[i+3:len(x)])

        i += 1

    return x

test_set = """
o
at
üst
su
tam
türk
aba
ayna
baba
bohça
ocak
aşkın
tabak
bostan
avurt
aldanç
kazanç
başkurt
"""
result_set = """
o-
at-
üst-
su-
tam-
türk-
a-ba-
ay-na-
ba-ba-
boh-ça-
o-cak-
aş-kın-
ta-bak-
bos-tan-
a-vurt-
al-danç-
ka-zanç-
baş-kurt-
"""

test_words = test_set.splitlines()
result_words = result_set.splitlines()

import unittest

class MyTest(unittest.TestCase):
    def test(self):
        for i, s in enumerate(test_words):
            self.assertEqual(hypo(s), result_words[i])

