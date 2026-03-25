import matplotlib.pyplot as plt
categories=['A','B','C','D']
values=[3,7,8,5]
plt.bar(categories,values,color='g',label='bar data')
plt.title('bar plot')
plt.xlabel('categories')
plt.ylabel('values')
plt.legend()
plt.show()