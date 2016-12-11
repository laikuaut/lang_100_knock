#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pylab import *
from pandas import *
#import matplotlib.pyplot as plt
#import numpy as np
#ts = Series(randn(1000), index=date_range('1/1/2000', periods=1000))
#
## 日本語を使うため必要
fontprop = matplotlib.font_manager.FontProperties(fname="/usr/share/fonts/vlgothic/VL-Gothic-Regular.ttf")
#
data = [
9194,
7486,
6868,
6772,
6420,
6243,
6071,
5508,
5337,
3988]
form_list = [
        'の',
        '。',
        'て',
        '、',
        'は',
        'に',
        'を',
        'と',
        'が',
        'た']
index = ['{}位\n{}'.format(i, form) for i, form in enumerate(form_list, start=1)]
#ts = Series(data, index=list(map(lambda x:str(x), range(1,11))))
##index = ['あ']
##ts = Series(randn(1), index=index)
##ts = ts.cumsum()
#ts.plot(kind='bar')
#plt.title('タイトル', size='24', fontproperties=fontprop)
#plt.savefig("image.png")
#
##from pylab import *
##from pandas import *
##import matplotlib.pyplot as plt
##import numpy as np
##ts = Series(randn(1000), index=date_range('1/1/2000', periods=1000))
##ts = ts.cumsum()
##ts.plot()
##plt.show()
##plt.savefig("image.png")
#
##df2 = DataFrame(rand(10, 4), columns=['a', 'b', 'c', 'd'])
##df2.plot(kind='bar')
##plt.savefig("image6.png")
#
##df = DataFrame(randn(1000, 4), index=ts.index, columns=list('ABCD'))
##df = df.cumsum()
##plt.figure();
##df.ix[5].plot(kind='bar'); plt.axhline(0, color='k')
##plt.show()
##plt.savefig("image5.png")

#t = np.arange(0.0, 2.0, 0.01)
#s = np.sin(2*np.pi*t)
#plt.plot(data, range(1,11), 'b')
plt.bar(range(1,11), data, align='center', width=0.3)
#plt.bar(index, data)

plt.xticks(range(1,11), index, fontproperties=fontprop)
plt.xlabel('単語表層系', fontproperties=fontprop)
plt.ylabel('出現頻度', fontproperties=fontprop)
plt.title('単語の出現頻度の棒グラフ(上位10単語)', fontproperties=fontprop)
plt.grid(True)
plt.savefig("test.png")
#plt.show()
