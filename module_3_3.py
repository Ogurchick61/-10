                 #1 Функция с параметрами по умолчанию:

def print_params(a = 1, b = 'string', c= True):
    print(a, b, c)

print_params(a=1, b='string', c=True)

print_params(a=12, b='Bool', c=False)

print_params()

print_params(b = 25) #Работает но ругается потому как в "b" тип данных "str".

print_params(c=[1,2,3]) #Работает но так же ругается в "c" тип данных "bol"

                 #2 Распаковка параметров:
#values_list = [4, 'Bobr', 4.6]
#values_dict = {'a': 1, 'b': 'string', 'c': True }
#print(values_list, values_dict)
#print_params(*values_list, **values_dict)#Захешил что бы не мешала работать 3-му пункту

                #3 Распаковка + отдельные параметры:
values_list_2 = [54.32,'string']
print(values_list_2)
print_params(*values_list_2, 42)




