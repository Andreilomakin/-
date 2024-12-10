immutable_var=1,2,3,'apple'
tuple_=immutable_var
tuple_[2]=5
print(tuple_)# сам кортеж неизменяем,изменяются только объекты в нём.
mutable_list=[1,2,3,'banana']
mutable_list[1]='appel'
print(mutable_list)