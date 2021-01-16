#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
（20 分）你正要去一間美術館看展覽，要買 x1 張全票與 x2 張學生票，而一張全票的售價是 p1 元，一
張學生票則是 p2 元。已知你要付的總金額不超過 t 元，若你拿出 t 元鈔票給櫃臺，請問櫃臺會找你多
少錢？

"""


# In[ ]:


x1 = int(input())
x2 = int(input())
p1 = int(input())
p2 = int(input())
money_paid = int(input())
total_cost = x1*p1+x2*p2
change = money_paid - total_cost
print(str(money_paid) + ", " + str(total_cost) + ", " + str(change))


# In[ ]:





# In[ ]:





# In[ ]:




