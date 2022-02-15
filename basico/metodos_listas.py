#metodo append
my_list=[1,2,3]
my_list.append(4)
# [1,2,3,4]

#metodo insert
my_list=[1,2,3]
my_list.insert(0,-1) #lista.insert(#indice,#valor)
# [-1,1,2,3]

#metodo extend
my_list=[1,2,3]
my_list2=[4,5,6]
my_list.extend(my_list2)
# [1,2,3,4,5,6]

#metodo index
#Devuelve la posicion de un elemento en la lista
#sino esta en la lista, arroja error
my_list=[1,2,3]
my_list.index(1)
# 0 #indice del valor 1
my_list.index(4)
# error

#metodo remove
my_list=[1,2,3]
my_list.remove(3)
# [1,2]
my_list.remove(3)
# error #3 ya no esta en la lista

#metodo sort
my_list=[3,1,2]
my_list.sort() #forma ascendente
# [1,2,3]
my_list.sort(reverse=True) #forma descendente
# [3,2,1]

#metodo reverse
my_list=[5,2,1,3]
my_list.reverse()
# [3,1,2,5] #invierte la lista

#metodo pop
my_list=[1,2,3,4]
my_list.pop(0) #my_list.pop(#indice)
# 1
# [2,3,4]                  #my_list[3] no existe
my_list.pop(3)
# error #no existe ese indice
