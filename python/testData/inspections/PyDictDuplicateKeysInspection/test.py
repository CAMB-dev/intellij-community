dict = {<warning descr="Dictionary contains duplicate keys 'key_1'">key_1</warning> : 1, key_2: 2, <warning descr="Dictionary contains duplicate keys 'key_1'">key_1</warning> : 3}
dict = {'key_1' : 1, <warning descr="Dictionary contains duplicate keys 'key_2'">'key_2'</warning>: 2, <warning descr="Dictionary contains duplicate keys 'key_2'">'key_2'</warning> : 3}
a = {}
{'key_1' : 1, 'key_2': 2}

import random
def foo():
    return random.random()

{foo(): 1, foo():2}

# PY-2511
dict = dict([(<warning descr="Dictionary contains duplicate keys 'key'">'key'</warning>, 666), (<warning descr="Dictionary contains duplicate keys 'key'">'key'</warning>, 123)])
dict = dict(((<warning descr="Dictionary contains duplicate keys 'key'">'key'</warning>, 666), (<warning descr="Dictionary contains duplicate keys 'key'">'key'</warning>, 123)))
dict = dict(((<warning descr="Dictionary contains duplicate keys 'key'">'key'</warning>, 666), ('k', 123)), <warning descr="Dictionary contains duplicate keys 'key'">key</warning>=4)

dict([('key', 666), ('ky', 123)])

# PY-27375
d = {<warning descr="Dictionary contains duplicate keys 'a'">'a'</warning>: 1, <warning descr="Dictionary contains duplicate keys 'a'">"a"</warning>: 2}
d = dict([(<warning descr="Dictionary contains duplicate keys 'a'">'a'</warning>, 1), (<warning descr="Dictionary contains duplicate keys 'a'">"a"</warning>, 2)])

d = {<warning descr="Dictionary contains duplicate keys '1'">1</warning>: 1, <warning descr="Dictionary contains duplicate keys '1'">1</warning>: 2}
d = dict([(<warning descr="Dictionary contains duplicate keys '1'">1</warning>, 1), (<warning descr="Dictionary contains duplicate keys '1'">1</warning>, 2)])

d = {<warning descr="Dictionary contains duplicate keys 'True'">True</warning>: 1, <warning descr="Dictionary contains duplicate keys 'True'">True</warning>: 2}
d = dict([(<warning descr="Dictionary contains duplicate keys 'True'">True</warning>, 1), (<warning descr="Dictionary contains duplicate keys 'True'">True</warning>, 2)])

d = {<warning descr="Dictionary contains duplicate keys 'None'">None</warning>: 1, <warning descr="Dictionary contains duplicate keys 'None'">None</warning>: 2}
d = dict([(<warning descr="Dictionary contains duplicate keys 'None'">None</warning>, 1), (<warning descr="Dictionary contains duplicate keys 'None'">None</warning>, 2)])