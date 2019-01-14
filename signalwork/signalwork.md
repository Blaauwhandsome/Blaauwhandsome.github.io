利用R语言脚本输出特征文件
```markdown
import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import r, pandas2ri
import os
os.chdir('C:/Users/lenovov/Desktop/abc')

data_list = []

#获取特征文件
def get_feature(fname):
    pandas2ri.activate()
    robjects.r.source('feature_extract.R')      #利用rpy2读取R脚本
    data_read = robjects.r.processFolder(fname) #得到数据文件
    data_read = pandas2ri.ri2py(data_read)      #转化为python可以使用的数据
    return data_read

if __name__ == '__main__':
    file_name_list = os.listdir('male')         #存放.wav格式声音的文件夹
    for file_name in file_name_list:
     data = get_feature(file_name)
    data_list.append(data)
    result = pd.concat(data_list)           
    result['label'] = 'male'
    result.to_csv("male.csv", index=False)
    #result['label'] = 'female'
    #result.to_csv("female.csv", index=False)
```
注：该文件主要是用来构造训练过程中的特征文件，需要人为的标定male或者female。对生成的male.csv和female.csv文件再合并成为train.csv文件，用于训练。


获得训练model
```markdown
import xgboost as xgb
import pandas as pd
import numpy as np
import sklearn
import pickle
import pprint

def xgb_score(preds, dtrain):
    labels = dtrain.get_label()
    return 'log_loss', sklearn.metrics.log_loss(labels, preds)


input_data = pd.read_csv('C:\\Users\\lenovov\\Desktop\\voice.csv')
input_data = input_data.sample(frac=1) 
gender = {'male' : 0, 'female' : 1}
input_data['label'] = input_data['label'].map(gender)
cols = [c for c in input_data.columns if c not in ['label']]
print (cols)
train = input_data.iloc[0 :3300]
test = input_data.iloc[3300 : ]
test_label = test['label']
test_label = np.array(test_label).reshape([-1 , 1])
del(test['label'])

fold = 1
for i in range(fold):
    params = {
        'eta': 0.01, #use 0.002
        'max_depth': 5,
        'objective': 'binary:logistic',
        'eval_metric': 'logloss',
        'lambda':0.1,
        'gamma':0.1,
        'seed': i,
        'silent': True
    }
    x1 = train[cols][0:3000]
    x2 = train[cols][3000:]
    y1 = train['label'][0:3000]
    y2 = train['label'][3000 : ]
    watchlist = [(xgb.DMatrix(x1, y1), 'train'), (xgb.DMatrix(x2, y2), 'valid')]
    model = xgb.train(params, xgb.DMatrix(x1, y1), 1500,  watchlist, feval=xgb_score, maximize=False, verbose_eval=50, early_stopping_rounds=50) #use 1500
    if i != 0:
        pred += model.predict(xgb.DMatrix(test[cols]), ntree_limit=model.best_ntree_limit)
    else:
        pred = model.predict(xgb.DMatrix(test[cols]), ntree_limit=model.best_ntree_limit)

pred /= fold
pre_label = np.zeros([pred.shape[0], 1])
for i in range(pred.shape[0]):
    if pred[i] >= 0.5:
        pre_label[i] = 1
    else:
        pre_label[i] = 0

acc = np.mean(np.equal(pre_label, test_label).astype(np.float))
print("the test acc is:", acc)

model_save = open('model.pkl', 'wb')    #保存模型
pickle.dump(model, model_save)
model_save.close()
```


测试声音
```markdown
import xgboost as xgb
import pandas as pd
import numpy as np
import sklearn
import pickle
import pprint
import rpy2.robjects as robjects
from rpy2.robjects import r, pandas2ri
import os
os.chdir('C:/Users/lenovov/Desktop/abc')

#get feature file
def get_feature(fname):
    pandas2ri.activate()
    robjects.r.source('feature_extract.R')
    data_read = robjects.r.processFolder(fname)
    data_read = pandas2ri.ri2py(data_read)
    return data_read

if __name__ == '__main__':
    data_list = []
    model_save = open('model.pkl', 'rb')
    model = pickle.load(model_save)
    model_save.close()

    file_name_list = os.listdir('data')             #读取声音文件
    for file_name in file_name_list:
        data = get_feature(file_name)
        data_list.append(data)
    test = pd.concat(data_list)

    pred = model.predict(xgb.DMatrix(test), ntree_limit=model.best_ntree_limit)
    print (pred)
    pre_label = np.zeros([pred.shape[0], 1])
    for i in range(pred.shape[0]):
        if pred[i] >= 0.5:
            pre_label[i] = 1
        else:
            pre_label[i] = 0
    num = 0
    tlen = len(pre_label)
    for i in pre_label:
        num += i
    print ('female is;'+str(num))
    print ('male is:'+str(tlen-num))
    print ((tlen-num)/tlen)
    print (num/tlen) 
```