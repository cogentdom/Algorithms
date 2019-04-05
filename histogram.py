import pandas as pd
from numpy import *
from scipy.interpolate import *
from matplotlib.pyplot import *
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

df = pd.read_csv("cleanedBMG.csv")
print(df.columns)
np_prop = array(df['PROPERTY: Trg'])
np_form = array(df['formula'])
columnStr = 'PROPERTY : Tl(K)'
np_val = array(df[columnStr])

# for i in range(len(np_form)-1):
#    print(str(i) + "  " + np_form[i+1] + "   " + str(np_prop[i+1]))
num_pnts = 587
num_bins = 16
np_bin = []
#
# for i in range(18):
#     #print(str(i))
#     np_bin.append(0.35+((i)*0.02))
#     #print(np_bin[i])
# N, bins, patches = plt.hist(np_prop, np_bin, edgecolor='black')
# fracs = N / N.max()
# norm = colors.Normalize(fracs.min(), fracs.max())
#
# for thisfrac, thispatch in zip(fracs, patches):
#     color = plt.cm.viridis(norm(thisfrac))
#     thispatch.set_facecolor(color)
#
# plt.xlabel("PROPERTY: Trg")
# plt.ylabel("Frequency")
# plt.title("Histogram for Trg values")
# plt.show()
y = np_prop
x = np_val
p1 = polyfit(x,y,1)
print(p1)

plot(x,y,'o')
title("Trg regressed on " + columnStr)
ylabel('PROPERTY: Trg')
xlabel(columnStr)
plot(x,polyval(p1,x),'r-')

yfit = p1[0]*x+p1[1]
yresid= y - yfit
SSresid = sum(pow(yresid,2))
SStotal = len(y)* var(y)
rsq = 1 - SSresid/SStotal
print("The R^2 value is: " + str(rsq))
show()
