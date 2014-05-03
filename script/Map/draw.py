#   -- import --
import shapefile, pickle
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize
import matplotlib.patches as patches
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def sentiment_score(continent):
    classified = pickle.load(open("../../data/simulated"+continent.lower()+"Analyzed.pkl", 'rb'))
    sentimentCol = classified.sentiment
    num_pos,num_neg,num_neu = 0,0,0
    for s in sentimentCol:
        if s == 'positive': num_pos += 1
        elif s == 'neutral': num_neu += 1
        elif s == 'negative': num_neg += 1
    result = 1.0*num_neg - (0.5*num_neu) - (1.0*num_pos) 
    if result < 0.0:
        return 0.0
    elif result > 1.0:
        return 1.0
    return result

def drawMap(continent):
    #   -- input --
    sf = shapefile.Reader("../../data/simulated/world_countries_boundary_file_world_2002")
    recs    = sf.records()
    shapes  = sf.shapes()
    Nshp    = len(shapes)
    cns     = []
    for i in xrange(Nshp):
        if continent in recs[i]:
            cns.append( (recs[i][1], shapes[i]) )

    cns = np.array(cns)
    cmap  = get_cmap('bwr')
    cccol = cmap(np.ones(Nshp)*sentiment_score(continent))

    #   -- plot --
    fig, ax = plt.subplots()
    ax.set_title("Tweet sentiment on 'College'",fontsize=40)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=Normalize(vmin=-1, vmax=1))
    sm._A = []
    cbar = fig.colorbar(sm, ticks=[-1, 0, 1], orientation='horizontal')
    cbar.ax.set_xticklabels(['Positive', 'Neutral(not measured)', 'Negative'],fontsize=20)
    cbar.ax.set_title("sentiment scale",fontsize=30)

    for i in xrange(Nshp):
        concated = ''.join(map(str,recs[i]))
        if continent in concated:
            ptchs = []
            pts = np.array(shapes[i].points)
            prt = shapes[i].parts
            par = list(prt) + [pts.shape[0]]
            for j in xrange(len(prt)):
                ptchs.append(Polygon(pts[par[j]:par[j+1]]))
            ax.add_collection(PatchCollection(ptchs,facecolor=cccol[i,:],edgecolor='k', linewidths=.1))
        else:
            ptchs = []
            pts = np.array(shapes[i].points)
            prt = shapes[i].parts
            par = list(prt) + [pts.shape[0]]
            for j in xrange(len(prt)):
                ptchs.append(Polygon(pts[par[j]:par[j+1]]))
            ax.add_collection(PatchCollection(ptchs,facecolor=cmap(0.5*np.ones(Nshp))[i,:],edgecolor='k', linewidths=.1))

    ax.set_xlim(-180,+180)
    ax.set_ylim(-90,90)
    fig = plt.gcf()
    fig.set_size_inches(25,15)
    fig.savefig('../../visualizations/'+continent+'.png')
    plt.show()

if __name__=='__main__':
    drawMap('Africa')
