#Plot neuron

PLOT=True

PDF_folder = rootf +'/matias/Dropbox/Drop-IdV/git-Perturbation/analysis/OUTPUT_pert/RF_check/'

RF_fit = {}
checksize=75
for id in list(clusid.keys())[10:20]:
    neuron=id-1
    print(clusid[id])
    coor=matdata['EllipseCoor'][:,neuron]
    
    [X,Y] = meshgrid(np.arange(checksize), np.arange(checksize))
    X = X - (checksize-coor[0])
    Y = Y - (checksize-coor[1])
    GRF = 1*np.exp(-(X**2)/coor[2] - (Y**2)/coor[3] - coor[4]*X*Y )
    #GRF=GRF[::-1,::-1]
    if PLOT:
        #-----------------
        fig=figure(figsize=(10,5))
        #-----------------

        ax=fig.add_subplot(1,2,1)
        ax.imshow(matdata['Spatial'][::-1,::-1,neuron])

        ax.plot(checksize-coor[0],checksize-coor[1],'+',markersize=5,color='k')

        ax.set_xticks([])
        ax.set_yticks([])
        ax.plot(checksize-matdata['Xell'][:,neuron],checksize-matdata['Yell'][:,neuron],'w',lw=2)

        #coor2:3 = sigma2
        ax.title.set_text('Cluster nb '+str(clusid[id] )+ ' STA')

        #-----------------

        ax=fig.add_subplot(1,2,2)
        ax.imshow(GRF)

        ax.plot(checksize-matdata['Xell'][:,neuron],checksize-matdata['Yell'][:,neuron],'w',lw=2)
        ax.plot(checksize-coor[0],checksize-coor[1],'+',markersize=5,color='k')
        ax.set_xticks([])
        ax.set_yticks([])
    
#     ax.title.set_text('Cluster nb '+str(clusid[id] )+ ' fit')
    
    
    #------------------------    
    RF_fit[clusid[id]] = [[checksize-coor[0],checksize-coor[1]],[checksize-matdata['Xell'][:,neuron],checksize-matdata['Yell'][:,neuron]]]
    
    if PLOT:
        txtadd=''
        if UNSORTED: txtadd='_UNSORTED'
        fsave = PDF_folder +'exp'+str(exp)+'_clus' +str(clusid[id]) +'_RF_STA_check' +txtadd
    
#     fig.savefig(fsave+'.png',format='png',dpi=110)
#     close(fig)  
        
    i+=1




#----------------------------------------------------------------------------------------
#SAVING BINARY OBJECTS DATA
#need to automate data folder creation
#----------------------------------------------------------------------------------------
import pickle5 as pickle
import os as os

def save_obj(obj, name ):
    if name[-4:]=='.pkl':
        name = name[:-4]
    with open( name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    if name[-4:]=='.pkl':
        name = name[:-4]
    #~ try:
        #~ return pk5.dumps(name+'pkl', protocol=5)
    #~ except:
    with open( name + '.pkl', 'rb') as f:
        return pickle.load(f)

def load_py2_obj(name ):
    if name[-4:]=='.pkl':
        name = name[:-4]
    with open( name + '.pkl', 'rb') as f:
        return pickle.load(f,encoding = 'latin1')
        


def getfiles(startdir, phrase, function) :
    files = []
    for dirpath, dirnames, filenames in os.walk(startdir) :
        if function == 'find' :
            for filename in [f for f in filenames if f.find(phrase)!=-1]:
                files.append(os.path.join(dirpath, filename))
        elif function == 'endswith' :
            for filename in [f for f in filenames if f.endswith(phrase)]:
                files.append(os.path.join(dirpath, filename))
        else :
            assert function=='endswith' or function=='find'
    return files
