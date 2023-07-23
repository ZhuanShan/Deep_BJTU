# import numpy as np
# import torch
# from torch.autograd import Variable

# x = Variable(torch.ones(2,2),requires_grad = False)
# temp = Variable(torch.zeros(2,2),requires_grad = True)
# print(x)
# y = x + temp + 2
# y = y.mean()           #求均值 
# print(y)
# y.backward()
# #print(x.grad)
# print(temp.grad)


import torch as t
import torch.nn as nn
from torch.autograd import Variable as V

input = V(t.randn(2,3))
model = nn.Linear(3,4)      #linear更改张量尺寸
output1 = model(input)
print(output1)
output2=nn.functional.linear(input,model.weight, model.bias )
print(output1==output2)