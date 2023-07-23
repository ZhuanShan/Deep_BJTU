import numpy as np
import torch
from torch.autograd import Variable

x = Variable(torch.ones(2,2),requires_grad = False)
temp = Variable(torch.zeros(2,2),requires_grad = True)
print(x)
y = x + temp + 2
y = y.mean()           #求均值 
print(y)
y.backward()
#print(x.grad)
print(temp.grad)