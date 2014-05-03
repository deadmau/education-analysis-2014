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
    #count how many pos, neutral, neg tweets
    num_pos, num_neg, num_neu = 0.0, 0.0, 0.0
    for s in sentimentCol:
        if s == 'positive': num_pos += 1
        elif s == 'neutral': num_neu += 1
        elif s == 'negative': num_neg += 1
    print "number of negative: ", str(num_neg), " number of neutral: ",str(num_neu), " number of positive: ",str(num_pos)
    #find optimal score
    result = findOptimal(num_neg, num_neu, num_pos)
    print "sentiment score of "+str(result)+" from scale: 0 ~ 1"
    return result

def drawMap(continent):
    #   -- input --
    sf = shapefile.Reader("../../data/simulated/world_countries_boundary_file_world_2002")
    recs    = sf.records() #stores a list of lists. ex)[ ['Europe', 'Germany', 'GR'], ['Asia', 'Japan', ...  
    shapes  = sf.shapes() #stores a list of shape file containg coordinates for each country
    Nshp    = len(shapes) #number of total countries 
    cmap  = get_cmap('bwr') #use 'Blue-Red' coloring 
    cccol = cmap(np.ones(Nshp)*sentiment_score(continent)) #create range of 'Blue-Red' colors according to sentiment score

    #   -- plot --
    fig, ax = plt.subplots() # create 2 subplots
    ax.set_title("Tweet sentiment on 'College'",fontsize=40) #set main title
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=Normalize(vmin=-1, vmax=1)) #create color map
    sm._A = [] #store colors for color map
    cbar = fig.colorbar(sm, ticks=[-1, 0, 1], orientation='horizontal') #place color bar
    cbar.ax.set_xticklabels(['Positive', 'Neutral(not measured)', 'Negative'],fontsize=20) #name scale
    cbar.ax.set_title("sentiment scale",fontsize=30) #set title for color map
    ax.set_xlim(-180,+180) #how wide?
    ax.set_ylim(-90,90) #how long?
    fig = plt.gcf() 
    fig.set_size_inches(25,15) #enlarge entire plot

    #loop through each country 
    for i in xrange(Nshp):
        concated = ''.join(map(str,recs[i]))
        if continent in concated: #found a continent that matches the input
            ptchs = [] # a list for continent color
            pts = np.array(shapes[i].points) #store coordinates for countries in input continent
            prt = shapes[i].parts 
            par = list(prt) + [pts.shape[0]]
            #color each points
            for j in xrange(len(prt)):
                ptchs.append(Polygon(pts[par[j]:par[j+1]]))
            #apply the coloring on subplot
            ax.add_collection(PatchCollection(ptchs,facecolor=cccol[i,:],edgecolor='k', linewidths=.1))
        else: #color rest of countinents white
            ptchs = []
            pts = np.array(shapes[i].points)
            prt = shapes[i].parts
            par = list(prt) + [pts.shape[0]]
            for j in xrange(len(prt)):
                ptchs.append(Polygon(pts[par[j]:par[j+1]]))
            ax.add_collection(PatchCollection(ptchs,facecolor=cmap(0.5*np.ones(Nshp))[i,:],edgecolor='k', linewidths=.1))

    fig.savefig('../../visualizations/'+continent+'.png') #save file
    plt.show() #display

if __name__=='__main__':
    drawMap('Africa')
