#type(i1) == type('str')
'''LEGO Pharaoh\'s Quest Rise of the Sphinx (7326)'''
def add(age, religion, birth, money, password, items=[]):
    return {'age':age, 'religion':religion, 'birth':birth, 'money':int(money), 'password':password, 'items':items}
class database:
    ie = eval(open('datas.py', 'r').read())
    items = {'aeroplane toy':5.00, 'car toy':8.00, 'hot wheels':9.00, 'yu-gi-oh':11.00, 'lego set bomba(5603)':12.00, 'lego scar':14.00}
    games = ['math', 'riddles', 'sell']
    riddles = {'''There was a bus with 17 people in the bus
including the driver. But there were 19 lives in the bus.
how? (lower case, with full stop)''':'because two of them were pregnant.', '''James had 3 bicycles and two sandbags.
then, when he wants to go home, the security guard
ask him, "can i check your things? i just want to make sure you aren't the smuggler."
Then the security checks James, he was free to go. But he was indeed smuggling. What's
that?''':'the bicycles.'}
def hhelp():
    print('help')
while True:
    i = input('identification or money or help?(i/m/h)')
    if i == 'i':
        i = input('add or del or read?(a/d/r)')
        if i == 'a':
            i1 = str(input('name'))
            i2 = int(input('age'))
            i3 = str(input('religion'))
            i4 = int(input('birth'))
            i5 = 0
            print('money = 0')
            i6 = input('password')
            if (i1 == '' or i2 == '') or (i3 == '' or i4 == '') or (i5 == '' or i6 == ''):
                print('add error., ErrorCode=1089')
            else:
                dic = eval(open('datas.py', 'r').read())
                dic[i1] = add(i2, i3, i4, i5, i6)
                open('datas.py', 'w').write(str(dic))
                database.ie[i1] = eval(open('datas.py', 'r').read())
                print('add sucsessful.')
        elif i == 'd':
            ij = input('name')
            uj = database.ie[ij]
            if input('password') == uj['password']:
                if input('are you sure?(y/n)') == 'y':
                    dic = eval(open('datas.py', 'r').read())
                    del dic[ij]
                    open('datas.py', 'w').write(str(dic))
                    database.ie = dic
                    print('del sucsessful.')
                else:
                    print('del canceled.')
            else:
                print('del error., ErrorCode=8967')
        elif i == 'r':
            gyu = input('name')
            uj = database.ie[gyu]
            if input('password') == uj['password']:
                print(gyu, uj)
                print('read successful.')
            else:
                print('read error., ErrorCode=8905')
        else:
            print('read error., ErrorCode=5555')
    elif i == 'm':
        ji = input('buy or earn money or read?(b/e/r)')
        if ji == 'b':
            n = input('name')
            uj = database.ie[n]
            if input('password') == uj['password']:
                print('''welcome to the shop! we have:
'''.title())
                toggle = True
                for i in database.items:
                    if not i == 'done':
                        if toggle:
                            print(i.title(), database.items[i], end=', ')
                            toggle = False
                        else:
                            print(i.title(), database.items[i])
                            toggle = True
                print()
                o = input('''
which one do you like?''').lower()
                out = database.items[o]
                print(out)
                if input('are you sure?(y/n)') == 'y':
                    if out <= uj['money']:
                        uj['money'] = uj['money'] - out
                        uj['items'].append(o)
                        dic = eval(open('datas.py', 'r').read())
                        dic[n] = add(uj['age'], uj['religion'], uj['birth'], uj['money'], uj['password'], uj['items'])
                        open('datas.py', 'w').write(str(dic))
                        database.ie[n] = eval(open('datas.py', 'r').read())
                        print('out sucsessful.')
                    else:
                        print('out error., ErrorCode=1099')
                else:
                    print('out canceled.')
            else:
                print('out error., ErrorCode=1567')
        elif ji == 'e':
            uj = database.ie[input('name')]
            if input('password') == uj['password']:
                print('''welcome to the shop! we have:
'''.title())
                toggle = True
                for i in database.games:
                    if not i == 'done':
                        if toggle:
                            print(i.title(), end=', ')
                            toggle = False
                        else:
                            print(i.title())
                            toggle = True
                o = input('''
which one do you like?''').lower()
                if input('are you sure?(y/n)') == 'y':
                    uj['money'] = uj['money'] + int(input('in code=').split('|')[0])
                    print('in sucsessful.')
            else:
                print('in error., ErrorCode=7865')
        elif ji == 'r':
            uj = database.ie[input('name')]
            if input('password') == uj['password']:
                print(uj['money'])
                print('in sucsessful.')
            else:
                print('read error., ErrorCode=4521')
        else:
            print('understanding error., ErrorCode=3481')
    elif i == 'h':
        i = input('how-to\'s or errors?(h/e)')
        if i == 'h':
            hhelp()
        elif i == 'e':
            i = int(input('enter ErrorCode='))
            if  i == 1089:
                print('''
add error:

this maybe because you fill one of the
questions empty.

please try again next time.

if there's still the same error,
call the coder, yusuf  ;)''')
            elif  i == 8967:
                print('''
del error:

this maybe because you  type in
the name or password wrong.

please try again next time.

if there's still the same error,
call the coder, yusuf  ;)''')
            elif  i == 8905:
                print('''
read error:

this maybe because you  type in
the name or password wrong.

please try again next time.

if there's still the same error,
call the developer, yusuf  ;)''')
            elif  i == 1099:
                print('''
out error:

this maybe because your money is less
than the out value.

please try again next time.

if there's still the same error,
call the developer, yusuf  ;)''')
            elif  i == 1567:
                print('''
out error:

this maybe because you  type in
the name or password wrong.

please try again next time.

if there's still the same error,
call the developer, yusuf  ;)''')
            elif  i == 4521:
                print('''
read error:

this maybe because you  type in
the name or password wrong.

please try again next time.

if there's still the same error,
call the developer, yusuf  ;)''')
            elif  i == 7845:
                print('''
understanding error:

this maybe because you  type in
something other than (i/m/h).

please try again next time.

if there's still the same error,
call the developer, yusuf  ;)''')
            elif  i == 3481:
                print('''
understanding error:

this maybe because you  type in
something other than (i/o/r).

please try again next time.

if there's still the same error,
call the developer, yusuf  ;)''')
            elif  i == 5555:
                print('''
understanding error:

this maybe because you  type in
something other than (i/m/h).

please try again next time.

if there's still the same error,
call the developer, yusuf  ;)''')
            elif i == 7865:
                print('''
in error:

this maybe because you  type in
the name or password wrong.

please try again next time.

if there's still the same error,
call the developer, yusuf  ;)''')
    elif i == 'show_ie':
        ie = database.ie
        print(ie, type(ie))
    elif i == 'del_ie':
        open('datas.py', 'w').write('{}')
        database.ie = eval(open('datas.py', 'r').read())
        ie = database.ie
        print(ie, type(ie))
    else:
        print('understanding error., ErrorCode=7845')
