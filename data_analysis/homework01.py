import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# df = pd.read_csv('C:\GitHub\python\data_analysis\data01\pp_gas_emission\gt_2013.csv', 
                # names=["AT", "AP", "AH", "AFDP", "GTEP", "TIT", "TAT", "TEY", "CDP", "CO", "NOX"])
df = pd.read_csv('C:\GitHub\python\data_analysis\data01\pp_gas_emission\gt_2014.csv')
# print(df.head(5))
# print(df.info())
#print(df.describe())
# df['AP'] = df['AP'] / 10
print(df.head(5))

plt.figure(figsize=(10,9))
plt.title('Gas Turbine CO & Nox Emission', size=15)

# dataset = df.corr(method='pearson', min_periods=1)  # pearson, kendall, spearman
# pearson : 두 변수들간의 값 (+ : 양의관계, - : 음의관계)
# kendall : 두 변수들간의 순위로 비교
dataset = df.corr(method='pearson')  # pearson, kendall, spearman
colormap = plt.cm.PuBu  #plt.cm.gist_heat
sns.heatmap(dataset, linewidths=0.1, vmax=1.0, cmap=colormap, square=True, linecolor='white', annot=True)
# df.corr() : 상관계수
# vmax : 오른쪽 color bar 최대값
# annot : 셀안에 숫자

plt.show()

########################
df.sort_values('CDX')