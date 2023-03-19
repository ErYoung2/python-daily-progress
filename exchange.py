import pandas as pd
import matplotlib.pyplot as plt

date = {'1q': ['01-01', '03-31'], '2q': ['04-01', '06-30'], '3q': ['07-01', '09-30'], '4q': ['10-01', '12-31']}

rate = []   # 定义一个空列表
for year in range(2020, 2022):   
    for i in range(1, 5):        
        s = f'{year}-' + date[f'{i}q'][0]  
        e = f'{year}-' + date[f'{i}q'][1]   
        
        url = f'http://www.safe.gov.cn/AppStructured/hlw/RMBQuery.do?startDate={s}&endDate={e}&queryYN=true'
        q = pd.read_html(url)[4]            
        rate.append(q)                      
df = pd.concat(rate)                        
df = df.sort_values(by='日期', ascending=[True]) 
df.to_excel('rate.xlsx', index=False)             

df = pd.read_excel(r'rate.xlsx')
plt.plot(df['日期'], df['美元'])
plt.title('Exchange graph')
plt.xlabel('time')
plt.ylabel('dollar exchage rate')
plt.show()

