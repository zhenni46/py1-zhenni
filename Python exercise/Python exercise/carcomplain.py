import pandas as pd  
data=pd.read_csv('car_complain.csv',encoding='utf-8')
data['problem']=data['problem'].apply(lambda x:x.strip(','))#字符串去空格
data['problem']=data['problem'].apply(lambda x:x.split(','))#字符串分割成表
data1=data.explode('problem')
print(data)
print(data1)
pinpai=data1['brand'].value_counts()
chexing=data1['car_model'].value_counts()
print(pinpai)
print(chexing)
print(pinpai.idxmax(),max(pinpai))
print(chexing.idxmax(),max(chexing))
#每一brand car_model
grouped=data1.groupby(['brand'])
car_model_number=grouped['car_model'].value_counts()
print(car_model_number)