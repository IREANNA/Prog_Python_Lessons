# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random  
# lst = ['robot'] * 10   
# lst += ['human'] * 10   
# random.shuffle(lst)  
# data = pd.DataFrame({'whoAmI':lst})   
# data.head()


import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

category=list(set(lst)) # Определяем набор уникальных категорий (не привязывая конкретно к заданному генерирующему коду)
category

onehot_encoded = dict()  # Кодируем каждую категорию
for i in range(len(category)):
  item=[0 for category in range(len(category))]
  item[i]=1
  onehot_encoded[category[i]]=item
onehot_encoded

list_onehot=list() # Формируем столбец с кодировкой в соответствии с исходными данными
for i in range(len(lst)):
  list_onehot.append(onehot_encoded.get(lst[i]))

data_new=pd.DataFrame({'whoAmI_onehot':list_onehot})
data_new