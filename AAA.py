'''contacts_dict = {} 
while True: 
    value = input('Введите данные. Фамилия Имя Отчество: Телефон => ') 
    if len(value):
        try:
            value = value.split(':')
            contacts_dict[value[0].strip()] = value[1].strip() 
        except:
            print('введены не корректные данные')
    else: 
        break 
result = sorted(contacts_dict .items(), key=lambda items: (items[0], items[1]))
for i in result: 
    print(' => '.join(i))'''


#def translit(name):
#    letters = {
#        'а': 'a',
#        'б': 'b',
#        'в': 'v',
#        'г': 'g',
#        'д': 'd',
#        'е': 'e',
#        'ё': 'jo',
#        'ж': 'zh',
#        'з': 'z',
#        'и': 'i',
#        'й': 'j',
#        'к': 'k',
#        'л': 'l',
#        'м': 'm',
#        'н': 'n',
#        'о': 'o',
#        'п': 'p',
#        'р': 'r',
#        'с': 's',
#        'т': 't',
#        'у': 'u',
#        'ф': 'f',
#        'х': 'h',
#        'ц': 'c',
#        'ч': 'ch',
#        'ш': 'sh',
#        'щ': 'shh',
#        'ъ': '',
#        'ы': 'y',
#        'ь': '',
#        'э': 'e',
#        'ю': 'yu',
#        'я': 'ya',
#    }
#    letters_list = letters.keys()
#    result = ''
#    for letter in name.lower():
#        if letter in letters_list:
#            result += letters[letter]
#        elif letter == ' ':
#            result += '_'
#        elif letter in ('-', '_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
#            result += letter
#        else:
#            result += letter
#    return result

#r = translit('Hf5раРАОвэdfdf.jpg')

#a = [
#    [9, 4, 6, 2, 2], 
#    [5, 2, 7, 7, 8], 
#    [7, 9, 8, 7, 8], 
#    [5, 9, 5, 3, 2], 
#    [6, 4, 6, 7, 4]
#]

#y = len(a) 
#x = y - 1
#p = 1
#for i in range(y):
#    for j in list(range(x,i,-1)):
#        p*= a[i][j] 
#print(p)


d = {'name_1':
{'RESULT':1,'other':5},
'name_2':
{'RESULT':0,'other':4},
'name_3':
{'RESULT':2,'other':5},
}
a = sorted(d.items(), key=lambda i: i[1]['RESULT'])
