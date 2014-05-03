#import
import shapefile, pickle
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize
import matplotlib.patches as patches
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


def findOptimal(x, y, z):
    #subtract both pos and neg from neutral for easy computation
    neg, pos = max(x-y, 0), max(z-y, 0)
    #both neg and pos are equivalently strong 
    if (neg == 0 and pos == 0) or (neg == pos):
        #return neutral
        return 0.5
    #we normalize
    total = neg+pos
    neg_norm, pos_norm = neg/total, pos/total
    #result is the subtraction from one another
    result = abs(neg_norm - pos_norm)
    return result
    
def sentiment_score(continent):
    #load analyzed data
    classified = pickle.load(open("../../data/simulated/"+continent.lower()+"Analyzed.pkl", 'rb'))
    sentimentCol = classified.sentiment
    #initialize variables
    num_pos, num_neg, num_neu, result = 0.0, 0.0, 0.0, 0.0
    #count how many pos, neutral, neg tweets
    for s in sentimentCol:
        if s == 'positive': num_pos += 1
        elif s == 'neutral': num_neu += 1
        elif s == 'negative': num_neg += 1
    print "\nFor: "+continent+"\n"
    print "number of negative: ", str(num_neg), " number of neutral: ",str(num_neu), " number of positive: ",str(num_pos)
    #find optimal score
    result = findOptimal(num_neg, num_neu, num_pos)
    print "sentiment score of "+str(result)+" from scale: 0 ~ 1"
    return (num_pos, num_neg, num_neu, result)

def drawMap(continent):
    #   -- input --
    sf = shapefile.Reader("../../data/simulated/world_countries_boundary_file_world_2002")
    recs    = sf.records() #stores a list of lists. ex)[ ['Europe', 'Germany', 'GR'], ['Asia', 'Japan', ...  
    shapes  = sf.shapes() #stores a list of shape file containg coordinates for each country
    Nshp    = len(shapes) #number of total countries 
    cmap  = get_cmap('Reds') #use 'Red-White' coloring
    gmap = get_cmap('binary') #use 'Black-White' coloring

    continentList = ['Africa', 'Europe', 'United States', 'Latin America', 'Asia']
    scoreList = [sentiment_score('africa'), sentiment_score('eu'), sentiment_score('us'), sentiment_score('soamerica'), sentiment_score('asia')]
    asia = cmap(np.ones(Nshp)*scoreList[4][3])
    eu= cmap(np.ones(Nshp)*scoreList[1][3])
    us = cmap(np.ones(Nshp)*scoreList[2][3])
    africa = cmap(np.ones(Nshp)*scoreList[0][3])
    soamerica= cmap(np.ones(Nshp)*scoreList[3][3])
    colorList = [africa, eu, us, soamerica, asia]

    if continent == 'eu':
        continent = 'Europe'
    elif continent == 'us':
        continent = 'United States'
    elif continent == 'soamerica':
        continent = 'Latin America'

    #   -- plot --
    fig, ax = plt.subplots() # create 2 subplots
    ax.set_title(continent+" Tweet sentiment on 'College'",fontsize=40) #set main title
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=Normalize(vmin=-1, vmax=1)) #create color map
    sm._A = [] #store colors for color map
    cbar = fig.colorbar(sm, ticks=[-1, 0, 1], orientation='horizontal') #place color bar
    cbar.ax.set_xticklabels(['Positive', 'Neutral', 'Negative'],fontsize=20) #name scale
    if continent != 'World':
        i = continentList.index(continent)
    else:
        i = -1
    if i != -1:
        title = "number of negative: "+str(scoreList[i][1])+" number of neutral: "+str(scoreList[i][2])+" number of positive: "+str(scoreList[i][0])+"\n"+"sentiment score of "+str(scoreList[i][3])+" from scale: 0 ~ 1"
    else:
        num_neg = sum(scoreList[i][1] for i in range(4))
        num_neu = sum(scoreList[i][2] for i in range(4))
        num_pos = sum(scoreList[i][0] for i in range(4))
        result= findOptimal(num_neg, num_neu, num_pos)
        title = "number of negative: "+str(num_neg)+" number of neutral: "+str(num_neu)+" number of positive: "+str(num_pos)+"\n"+"overall sentiment score of "+str(result)+" from scale: 0 ~ 1"
    cbar.ax.set_title(title,fontsize=30) #set title for color map
    ax.set_xlim(-180,+180) #how wide?
    ax.set_ylim(-90,90) #how long?
    fig = plt.gcf() 
    fig.set_size_inches(25,15) #enlarge entire plot

    #loop through each country 
    for i in xrange(Nshp):
        concated, found = ''.join(map(str,recs[i])), -1
        if continent in concated:
            found = continentList.index(continent)
        if continent == 'World':
            for c in continentList:
                if c in concated:
                    found = continentList.index(c)
                    break
        if found != -1:
            ptchs = [] # a list for continent color
            pts = np.array(shapes[i].points) #store coordinates for countries in input continent
            prt = shapes[i].parts 
            par = list(prt) + [pts.shape[0]]
            #color each points
            for j in xrange(len(prt)):
                ptchs.append(Polygon(pts[par[j]:par[j+1]]))
            #apply the coloring on subplot
            ax.add_collection(PatchCollection(ptchs,facecolor=colorList[found][i,:],edgecolor='k', linewidths=.1))
        else: #color rest of countinents gray
            ptchs = []
            pts = np.array(shapes[i].points)
            prt = shapes[i].parts
            par = list(prt) + [pts.shape[0]]
            for j in xrange(len(prt)):
                ptchs.append(Polygon(pts[par[j]:par[j+1]]))
            ax.add_collection(PatchCollection(ptchs,facecolor=gmap(0.5*np.ones(Nshp))[i,:],edgecolor='k', linewidths=.1))

    fig.savefig('../../visualizations/'+continent+'.png') #save file
    #plt.show() #display

if __name__=='__main__':
    drawMap('Africa')
    drawMap('Asia')
    drawMap('eu')
    drawMap('us')
    drawMap('soamerica')
    drawMap('World')
