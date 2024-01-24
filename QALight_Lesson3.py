# class Borsch: # креслення, рецепт, інструкція
#     value = 2 # атрибут класу, аргумент класу, параметр класу, поля класу(змінна класу)
#     beet = True # можуть юути будь-якого типу
#     meat = 'pork'
#
#     def boiled(self, temperature): # метод обʼекту класа (функція обʼекту класу)
#         if temperature > 100:
#             return 'You boiled borsch'
#         else:
#             return 'You need more'
#
# odesa_borsch = Borsch()
# print(odesa_borsch.value)
# print(odesa_borsch.meat)
# odesa_borsch.meat = 'veal'
# print(odesa_borsch.meat)
#
# lviv_borsch = Borsch()
# lviv_borsch.meat = 'chicken'
# print(lviv_borsch.meat)
#
# herson_borsch = Borsch()
# herson_borsch.beet = False
# herson_borsch.tomato = True
# print(herson_borsch.tomato)
#
# updated_borsch = Borsch()
# updated_borsch.sour_cream = True
# updated_borsch.parsley = True
# print(updated_borsch.parsley)
# print(updated_borsch.sour_cream)

class Human:
    age = 20
    name = 'Ted'
    profession = 'empty'
    def speak(self):
        return 'You are speaking'

class Pilot(Human):
    profession = 'pilot'
    def fly(self):
        return 'You are fling'

class Sailor(Human):
    profession = 'sailor'
    def go(self):
        return 'You are going'

ben = Pilot()
print(ben.name)
print(ben.profession)

ben = Sailor()
print(ben.name)
print(ben.profession)



