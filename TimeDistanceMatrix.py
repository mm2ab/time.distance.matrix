#!/usr/bin/env python
# coding: utf-8

# # <ins>Cálculo das Matrizes de Tempo e Distância</ins>

# <div style="text-align: justify"><strong>Rotas:</strong> O presente código utilizou como referência o <a id="url" href="https://github.com/Project-OSRM/osrm-backend">Projeto OSRM</a> <br> <strong>Mapa:</strong> O arquivo utilizado foi extraído do <a id="url" href="https://download.geofabrik.de/south-america/brazil/sudeste.html">Projeto Open Street Map</a>
#  </div> 

# ### 1) Distâncias entre dois Ponto

# In[ ]:


#-------------------------------------------Distance
def DistanceOSRM(lat1, lon1, lat2, lon2):
    
    import osrm
    
    s = osrm.Client(host='http://localhost:5000') # consulta ao servidor local OSRM

    r = s.route(
        coordinates=[[lon1,lat1], [lon2,lat2]],
        overview=osrm.overview.full)

    d = ((r["routes"][0]["distance"])/1000)
    
    return d


# ### 2) Tempo entre dois Ponto

# In[ ]:


#-------------------------------------------Time
def TimeOSRM(lat1, lon1, lat2, lon2):
    
    import osrm
    
    s = osrm.Client(host='http://localhost:5000') # consulta ao servidor local OSRM

    r = s.route(
        coordinates=[[lon1,lat1], [lon2,lat2]],
        overview=osrm.overview.full)

    t = ((r["routes"][0]["duration"])/60)       
    
    return t


# ### 3) Resultados

# In[ ]:


#-------------------------------------------Export
import pandas as pd

f = pd.DataFrame(pd.read_csv('time.distance.matrix.input.csv',sep=";"))
vd = []
vt = []

for i in range(0,len(f['ORIGEM_LAT'])):
    vd.append(DistanceOSRM((f['ORIGEM_LAT'].values[i]),(f['ORIGEM_LON'].values[i]),(f['DESTINO_LAT'].values[i]),(f['DESTINO_LON'].values[i])))
    vt.append(TimeOSRM((f['ORIGEM_LAT'].values[i]),(f['ORIGEM_LON'].values[i]),(f['DESTINO_LAT'].values[i]),(f['DESTINO_LON'].values[i])))
    
f['DISTANCE'] = vd
f['TIME'] = vt

f.to_csv('time.distance.matrix.output.csv',sep=';')

