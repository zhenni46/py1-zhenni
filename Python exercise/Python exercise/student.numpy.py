import numpy as np
persontype = np.dtype({
    'names':['name','chinese', 'math', 'english'],
    'formats':['S32','i', 'i', 'i']})
peoples = np.array([("Zhangfei",68,65,30),("Guanyu",95,76,98),("Liubei",98,86,88),("Dianwei",90,88,77),("Xuchu",80,90,90)],dtype=persontype)
names=peoples['name']
chineses = peoples['chinese']
maths = peoples['math']
englishs = peoples['english']
print(peoples)
print('chinese average=',np.mean(chineses))
print('math average=',np.mean(maths))
print('english average=',np.mean(englishs))
print('chinese min=',np.min(chineses))
print('math min=',np.min(maths))
print('english min=',np.min(englishs))
print('chinese max=',np.max(chineses))
print('math max=',np.max(maths))
print('english max=',np.max(englishs))
print('chinese std=',np.std(chineses))
print('math std=',np.std(maths))
print('english std=',np.std(englishs))
print('chinese var=',np.var(chineses))
print('math var=',np.var(maths))
print('english var=',np.var(englishs))
ranking=sorted(peoples,key=lambda x:x[1]+x[2]+x[3])
print (ranking)