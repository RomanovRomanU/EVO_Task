import time
import math
import random

class node():   #Создаём класс для ячейки в трёхмерной матрице
    def __init__(self,x,y,z,cargo):
        self.x=x
        self.y=y
        self.z=z
        self.cargo=cargo    #Значение ячейки
    def __str__(self):      #Для удобства(что бы можно было использовать print)
        return 'coordinats:'+str(self.x)+','+str(self.y)+','+str(self.z)+'|'+'cargo:'+str(self.cargo)

def in_one_column(first_node,second_node):  #Этот метод проверяет,находяться ли две ячейки на одной оси(столбце)
    if (first_node.x==second_node.x and first_node.y==second_node.y):
        return True
    if (first_node.x==second_node.x and first_node.z==second_node.z):
        return True
    if (first_node.y==second_node.y and first_node.z==second_node.z):
        return True
    else:
        return False

#Создаём матрицу как список ячеек
a=[]
for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            #Ячейка с координатами x,y,z,и случайным значением
            a.append(node(i,j,k,random.randrange(0,10)))



def better_solution(a):
    sum=0
    max_sum=0
    for first_node in a:
        node_index=a.index(first_node)
        #Наш индекс вида a*100+b*10+c,находим a,b,c
        node_index_hundred=node_index//100      #В какой сотне индекс
        node_index_tens=(node_index%100)//10    #В каком десятке индекс
        node_index_ones=(node_index%10)         #Сколько единиц в индексе

        #Проходимся только по ячейкам с такими же x и y
        index_for_x_y=node_index_hundred*100 + node_index_tens*10
        while index_for_x_y <(node_index_hundred)*100 + (node_index_tens+1)*10:
            sum+=a[index_for_x_y].cargo
            index_for_x_y+=1

        #Проходимся только по ячейкам с такими же x и z
        index_for_x_z=node_index_hundred*100+node_index_ones
        while index_for_x_z <(node_index_hundred+1)*100:
            sum+=a[index_for_x_z].cargo
            index_for_x_z+=10

        #Проходимся только по ячейкам с такими же y и z
        index_for_y_z=node_index_tens*10+node_index_ones
        while index_for_y_z<1000:
            sum+=a[index_for_y_z].cargo
            index_for_y_z+=100

        sum=sum-first_node.cargo*2 #Саму ячейку first_node мы посчитали трижды
        if sum>max_sum:
            max_sum=sum
            sum=0
        else:
            sum=0
    return max_sum
    
def simple_solution(a):
    max_sum=0
    sum=0
    for first_node in a:
        for second_node in a:
            #Просто перебираем все остальные ячейки
            if in_one_column(first_node,second_node)==True:
                #Если вторая ячейка лежит на одной оси(в том же столбце),то она нам походит
                sum+=second_node.cargo
        if sum>max_sum:
            max_sum=sum
            sum=0
        else:
            sum=0
    return max_sum

print('Simple solution:')
start_time_for_simple_method=time.time() #Замеряем время
print('Max sum for this matrix:'+str(simple_solution(a)))
print('This method took:'+str(time.time()-start_time_for_simple_method)+' seconds\n')


print('Better solution:')
start_time_for_better_method=time.time() #Замеряем время
print('Max sum for this matrix:'+str(better_solution(a)))
print('This method took:'+str(time.time()-start_time_for_better_method)+' seconds')
