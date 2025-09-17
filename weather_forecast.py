import requests, pprint, time
import matplotlib.pyplot as plt 

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-059?Authorization=rdec-key-123-45678-011121314&elementName=T&sort=time'

data = requests.get(url).json()
#pprint.pprint(data)

temp = data['records']['locations'][0]['location'][0]['weatherElement'][0]['time']
t_list = []

for t in temp:
    t_list.append(int(t['elementValue'][0]['value']))
#print(t_list)
print("現在時間:", time.ctime())
print()
day = 1
for i in range(0,len(t_list)-1,2):
    print('未來第'+str(day)+'天溫差：'+str(abs(t_list[i+1]-t_list[i])))
    if abs(t_list[i+1]-t_list[i]) >= 4:
        print("早晚溫差大")    
    day += 1
    print()

l_time = time.localtime(time.time())
day = [i for i in range(l_time.tm_mday, l_time.tm_mday+len(t_list)) ]

plt.rcParams["figure.figsize"] = (20,10)
plt.rcParams['font.size'] = 16
plt.rcParams['font.family'] = 'Microsoft JhengHei'

plt.plot(day, t_list)
day_morning = []
for i in range(l_time.tm_mday, l_time.tm_mday+7):
    for j in range(2):
        if j%2 == 0:
            day_morning.append(i)
        else:
            day_morning.append("")
if len(t_list) == 15 and l_time.tm_hour > 0:
    day_night = []
    for i in range(l_time.tm_mday+1, l_time.tm_mday+8):
        for j in range(2):
            if j%2 == 0:
                day_night.append(i)
            else:
                day_night.append("")
    plt.xticks(day, [""]+day_night)
elif len(t_list) == 15:
    plt.xticks(day, day_morning+[""])    
else:
    plt.xticks(day, day_morning)
    
plt.title('未來7天早晚溫度')
plt.xlabel('日期(每日6:00及18:00)')
plt.ylabel('氣溫(°C)')
plt.grid(1)

plt.show()


