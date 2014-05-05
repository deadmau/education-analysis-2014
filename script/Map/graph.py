import pickle
import numpy as np
import matplotlib.pyplot as plt

africa = pickle.load(open('../../data/simulated/africaWordAnalyzed.pkl', 'rb'))
asia = pickle.load(open('../../data/simulated/asiaWordAnalyzed.pkl', 'rb'))
us= pickle.load(open('../../data/simulated/usWordAnalyzed.pkl', 'rb'))
eu = pickle.load(open('../../data/simulated/euroWordAnalyzed.pkl', 'rb'))
latin = pickle.load(open('../../data/simulated/soamericaWordAnalyzed.pkl', 'rb'))
total = pickle.load(open('../../data/simulated/totalWordAnalyzed.pkl', 'rb'))

dataList = [africa, asia, us, eu, latin, total]
benefit = {'negative':0, 'positive':0, 'neutral':0}
cost = {'negative':0, 'positive':0, 'neutral':0}
quality = {'negative':0, 'positive': 0,'neutral':0}
time = {'negative':0, 'positive': 0,'neutral':0}
xAxis = [benefit, cost, quality, time]

for data in dataList:
    key, sen, select = data.keyword, data.sentiment, -1
    for i in range(len(data)-1):
        if key[i] == 'benefit':
            select = 0
        elif key[i] == 'cost':
            select = 1
        elif key[i] == 'quality':
            select = 2
        elif key[i] == 'time':
            select = 3
        if select != -1:
            xAxis[select][sen[i]] += 1

N = 4
negTotal = tuple(a['negative'] for a in xAxis)
posTotal = tuple(a['positive'] for a in xAxis)
neuTotal = tuple(a['neutral'] for a in xAxis)

ind = np.arange(N)  # the x locations for the groups
width = 0.2      # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, negTotal, width, color='r')
rects2 = ax.bar(ind+width, posTotal, width, color='b')
rects3 = ax.bar(ind+width+width, neuTotal, width, color='0.75')

# add some
ax.set_ylabel('Number of tweets', fontsize=20)
ax.set_title('Scores by Keywords', fontsize=40)
ax.set_xticks(ind+width)
ax.set_xticklabels( ('"Benefit"', '"Cost"', '"Quality"', '"Time"'),fontsize=20 )

ax.legend( (rects1[0], rects2[0], rects3[0]), ('Negative', 'Neutral', 'Positive'),fontsize=20 )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
fig.set_size_inches(25,15) #enlarge entire plot
plt.show()
