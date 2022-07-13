#Código para resolver caso técnico para análisis - Data engineer 
#Derco, Carlos Peñaloza Casanova
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import json
import requests

#%%
#########____CONEXIÓN CON API____#########
print("REGIONES")
response = requests.get('https://apis.digital.gob.cl/dpa/regiones', headers={
    "User-Agent" : "Chrome/103.0.5060.11"})

for i in response.json():
  print("REGIÓN:", i['nombre'])


respons = requests.get('https://apis.digital.gob.cl/dpa/comunas', headers={
    "User-Agent" : "Chrome/103.0.5060.114"})

for i in respons.json():
  print("COMUNA:", i['nombre'])

#suprimimos advertencias
warnings.filterwarnings('ignore')

#_______DESARROLLO_________
'''Para estudiar el fenómeno de preferencia y recambio de automóviles en Chile, 
se entrega el siguiente set de datos anonimizados de tenencia de vehículos histórica:'''


#leemos el set de datos .csv y y declaramos nombre de columnas
df = pd.read_csv('bbdd prueba corp.csv', sep=';', encoding_errors='ignore',
                 names=['PLACA','MARCA','MODELO','AÑO','ID_CLIENTE',
                        'COMUNA','REGION','SEXO','ACTIVIDAD','VALOR_VEHICULO',
                        'FEC_TRANSFERENCIA','COLOR','EDAD','VIGENCIA'])

df.head()

#limpiamos, reemplazamos los ceros y espacios por nulos
df = df.replace('0', np.nan)
df = df.replace(' ', np.nan)


#analizamos datos de cada columna:

#_______MARCA_________
set(df['MARCA'])

#cambiamos las que son la misma marca por una unica
df['MARCA'] = df['MARCA'].replace({'GREAT WALL MOTOR': 'GREAT WALL', 
                                   'GREAT WALL MOTORS': 'GREAT WALL',
                                   'BAIC YINXIANG': 'BAIC',
                                   'DONG FENG': 'DONGFENG',
                                   'KIA MOTORS': 'KIA',
                                   'JAC MOTORS': 'JAC',
                                   'MARCA NULA': np.nan})

#verificamos los modelos que tengan marcas nulas para completarlas 
df[df['MARCA'].isna()]['MODELO'].unique()

suzuki = ['GRAND VITARA GLX 1.6', 'GRAND NOMADE GLX SPO', 'APV2 GL 1.6','GRAND VITARA GLX 4X4', 
          'GRAND VITARA GLX SPO', 'GRAND NOMADE GLX 2.0', 'JIMNY JX 1.3', 'GRAND NOMADE GLX 4X4',
          'JIMNY JLX 1.3', 'JIMNY JLX 4X4 1.3', 'APV VAN GL 1.6', 'GRAND VITARA 1.6']

mazda = ['CX 7 GT AWD 2.3 AT', 'CX 7 2.5 AT', 'CX7 2.5', 'CX 7 R 2.5 AT']

renault = ['KOLEOS EXPRESSION 2.', 'KOLEOS DYNAMIQUE 2.5']

haval = ['HAVAL H5 LX 4X4 2.4', 'HAVAL H3 LE 2.0']

great_wall = ['HOVER 2.4']

jac = ['REIN 4X4']


#completamos las marcas que están nulas despúes de conocer sus modelos
df['MARCA'].loc[(df['MODELO'].isin(suzuki)) & (df['MARCA'].isna())] = 'SUZUKI'
df['MARCA'].loc[(df['MODELO'].isin(mazda)) & (df['MARCA'].isna())] = 'MAZDA'
df['MARCA'].loc[(df['MODELO'].isin(renault)) & (df['MARCA'].isna())] = 'RENAULT'
df['MARCA'].loc[(df['MODELO'].isin(haval)) & (df['MARCA'].isna())] = 'HAVAL'
df['MARCA'].loc[(df['MODELO'].isin(great_wall)) & (df['MARCA'].isna())] = 'GREAT WALL'
df['MARCA'].loc[(df['MODELO'].isin(jac)) & (df['MARCA'].isna())] = 'JAC'




#_______MODELO_________
set(df['MODELO'])

#eliminamos los espacios al campo modelo
df['MODELO'] = df['MODELO'].apply(lambda x: x.strip() if isinstance(x, str) else x)

#reemplazomos los modelos nulos por valores nulos
df['MODELO'] = df['MODELO'].replace('MODELO NULA', np.nan)



#_______AÑO_________
#verificamos si columna AÑO tiene valores nulos
df[df['AÑO'].isna()]



#_______ ID_CLIENTE _________
# verificamos si columna ID_CLIENTE tiene valores nulos
df[df['ID_CLIENTE'].isna()]


#_______COMUNA_________
set(df['COMUNA'])

#cambiamos las comunas que son iguales por una unica
df['COMUNA'] = df['COMUNA'].replace({'CON CON': 'CONCON',
                                     'CALERA': 'LA CALERA',
                                     'PAIGUANO': 'PAIHUANO',
                                     'LLAYLLAY': 'LLAY-LLAY',
                                     'LLAY LLAY': 'LLAY-LLAY',
                                     'MARCHIGUE': 'MARCHIHUE',
                                     'SAN JOSE': 'SAN JOSE DE MAIPO',
                                     'EST CENTRAL': 'ESTACION CENTRAL',
                                     'ESTACION CENT': 'ESTACION CENTRAL',
                                     'SAN PEDRO': 'SAN PEDRO DE ATACAMA',
                                     'DIEGO DE ALMA': 'DIEGO DE ALMAGRO',
                                     'TEODORO SCHIMDT': 'TEODORO SCHMIDT',
                                     'QUINTA TILCOCO': 'QUINTA DE TILCOCO',
                                     'SAN PEDRO DE': 'SAN PEDRO DE ATACAMA',
                                     'SAN VICENTE': 'SAN VICENTE TAGUATAGUA',
                                     'P AGUIRRE CERDA': 'PEDRO AGUIRRE CERDA',
                                     'PEDRO AGUIRRE CERD': 'PEDRO AGUIRRE CERDA',
                                     'SAN PEDRO DE LA PA': 'SAN PEDRO DE LA PAZ',
                                     'SAN PEDRO DE ATACA': 'SAN PEDRO DE ATACAMA',
                                     'SAN JUAN DE LA COS': 'SAN JUAN DE LA COSTA',
                                     'SAN VICENTE TAGUA': 'SAN VICENTE TAGUATAGUA',
                                     'SAN VICENTE TAGUA TA': 'SAN VICENTE TAGUATAGUA'})



#_______REGION_________

#extramos las regiones de la API suministrada 
regiones = {'01': 'DE TARAPACA',                
            '02': 'DE ANTOFAGASTA',
            '03': 'DE ATACAMA',
            '04': 'DE COQUIMBO',
            '05' :'DE VALPARAISO',
            '06': 'DEL LIBERTADOR BERNARDO OHIGGINS',
            '07': 'DEL MAULE',
            '08': 'DEL BIO BIO',
            '09': 'DE LA ARAUCANIA',
            '10': 'DE LOS LAGOS',
            '11': 'AYSEN DEL GENERAL CARLOS IBANEZ',
            '12': 'DE MAGALLANES Y ANTARTICA CHILENA',
            '13': 'METROPOLITANA DE SANTIAGO',
            '14': 'DE LOS RIOS',
            '15': 'DE ARICA y PARINACOTA',
            '16': 'DE ÑUBLE'}

#agg un cero a los digitos para hacer join en las regiones
df['REGION'] = df['REGION'].replace({'5':'05', '2':'02', '8':'08', '3':'03', '9':'09', '6':'06', '1':'01', '7':'07', '4':'04'})

#por medio de las comunas se completan las regiones nulas
df['REGION'].loc[(df['COMUNA']=='SAN JUAN DE LA COSTA') & (df['REGION'].isna())] = 'DE LOS LAGOS'
df['REGION'].loc[(df['COMUNA']=='SAN JOSE DE MAIPO') & (df['REGION'].isna())] = 'METROPOLITANA DE SANTIAGO'

#unificamos las regiones
df['REGION'] = df['REGION'].replace(regiones)
df['REGION'].unique()


#_______SEXO_________
df['SEXO'].unique()


#_______ACTIVIDAD_________
df['ACTIVIDAD'].unique()
#la columna no posee información suficiente por lo tanto se elimina
df.drop(columns=['ACTIVIDAD'], inplace=True)


#_______VALOR VEHICULO_________
set(df['VALOR_VEHICULO'])
#se eliminan espacios, comas y valores posteriores
df['VALOR_VEHICULO'] = df['VALOR_VEHICULO'].apply(lambda x: x.strip() if isinstance(x, str) else x)
df['VALOR_VEHICULO'] = df['VALOR_VEHICULO'].apply(lambda x: x.split(',')[0] if isinstance(x, str) else x)
#cambiamos la columna a tipo int
df['VALOR_VEHICULO'] = df['VALOR_VEHICULO'].fillna(0).astype(int)


#_______TRANSFERENCIA_________
df['FEC_TRANSFERENCIA'].unique()

#_______COLOR_________
set(df['COLOR'])

#los colores que poseen un espacio luego de su nombre se cambian por el nombre - otros
#tengo dos categorias de colores.
df['COLOR'].loc[df['COLOR'].str.startswith('AZUL ', na=False)] = 'AZUL - OTROS'
df['COLOR'].loc[df['COLOR'].str.startswith('AMARILLO ', na=False)] = 'AMARILLO - OTROS'
df['COLOR'].loc[df['COLOR'].str.startswith('BEIGE ', na=False)] = 'BEIGE - OTROS'
df['COLOR'].loc[df['COLOR'].str.startswith('BLANCO ', na=False)] = 'BLANCO - OTROS'
df['COLOR'].loc[df['COLOR'].str.startswith('CAFE ', na=False)] = 'CAFE - OTROS'
df['COLOR'].loc[df['COLOR'].str.startswith('CELESTE ', na=False)] = 'CELESTE - OTROS'
df['COLOR'].loc[df['COLOR'].str.startswith('DORADO ', na=False)] = 'DORADO - OTROS'
df['COLOR'].loc[df['COLOR'].str.startswith('GRIS ', na=False)] = 'GRIS - OTROS'
df['COLOR'].loc[df['COLOR'].str.startswith('NARANJO ', na=False)] = 'NARANJO - OTROS'
df['COLOR'].loc[df['COLOR'].str.startswith('NEGRO ', na=False)] = 'NEGRO - OTROS'
df['COLOR'].loc[df['COLOR'].str.startswith('PLATEADO ', na=False)] = 'PLATEADO - OTROS'
df['COLOR'].loc[df['COLOR'].str.startswith('ROJO ', na=False)] = 'ROJO - OTROS'
df['COLOR'].loc[df['COLOR'].str.startswith('VERDE ', na=False)] = 'VERDE - OTROS'
df['COLOR'].loc[df['COLOR'].str.startswith('VIOLETA ', na=False)] = 'VIOLETA - OTROS'




#_______EDAD_________
df['EDAD'].unique()

#pongo nulo a los clientes con EDAD == 3 y edad == 134
df['EDAD'].loc[(df['EDAD'] == 134) | (df['EDAD'] == 3)] = np.nan

#se convierte la columna a tipo int
df['EDAD'] = df['EDAD'].fillna(0).astype(int)



#_______VIGENCIA_________
df['VIGENCIA'].unique()



'''SE PIDE APLICAR TÉCNICAS DE ETL, EXPLORACIÓN, DESCUBRIMIENTO 
Y ANALÍTICA PARA EXPLICAR Y CARACTERIZAR LOS FENÓMENOS QUE EN LOS DATOS SE PUEDEN OBSERVAR'''


#_______VISUALIZACIÓN DE DATOS Y ETL_________
df.info()

#marcas que hacen parte de DERCO
derco = ['SUZUKI', 'MAZDA', 'RENAULT', 'HAVAL', 'GREAT WALL', 'CHANGAN', 'JAC']


#se crean dos df
df_derco = df[df['MARCA'].isin(derco)] #marcas de derco
df_otros = df[~df['MARCA'].isin(derco)] #otras marcas

#paleta de colores
colors_plt = sns.color_palette("Set2")
colors_sns = sns.color_palette("Paired",10)



#%%
#########____PLOTEAMOS LOS DATOS DEL SEXO DE LOS CLIENTES DERCO Y CLIENTES DE OTRAS MARCAS____#########

#_______SEXO DE LOS CLIENTES DERCO_________
fig = plt.figure(figsize=(9,6))
ax = plt.bar(df_derco['SEXO'].value_counts().index, df_derco['SEXO'].value_counts(), color=colors_plt)
plt.title('Sexo de los clientes Derco', color="white")

for rect in ax.patches:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2., 1*height,'%d' % int(height),ha='center', va='bottom')

plt.box(False)
plt.yticks([])

#_______SEXO DE LOS CLIENTES DE OTRAS MARCAS_________
fig = plt.figure(figsize=(9,6))
ax = plt.bar(df_otros['SEXO'].value_counts().index, df_otros['SEXO'].value_counts(), color=colors_plt)
plt.title('\n Sexo de los clientes de otras marcas', color="white")

for rect in ax.patches:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2., 1*height,'%d' % int(height),ha='center', va='bottom')

plt.box(False)
plt.yticks([])
plt.show()

#%%
#_______PORCENTAJE DE CLIENTES DERCO SEGÚN SU SEXO_________

fig = plt.figure(figsize=(10,5))

plt.pie(df_derco['SEXO'].value_counts(), labels=df_derco['SEXO'].value_counts().index, colors=colors_plt,
        autopct='%.0f%%', shadow=True, rotatelabels=False)

plt.title('Porcentaje de clientes Derco según sexo', color="white")
fig = plt.figure(figsize=(10,5))

plt.pie(df_otros['SEXO'].value_counts(), labels=df_otros['SEXO'].value_counts().index, colors=colors_plt,
        autopct='%.0f%%', shadow=True, rotatelabels=False)

plt.title('\n\nPorcentaje de clientes de otras marcas según sexo', color="white")
plt.show()



#%%
#########____PLOTEAMOS LOS DATOS DE LA EDAD DE LAS PERSONAS____#########

df_derco.EDAD_cuts = pd.cut(df_derco["EDAD"], [0,10,20,30,40,50,60,70,80,90,100,110,120], include_lowest=False)   
group1 = df_derco.groupby(df_derco.EDAD_cuts)

#edad clientes DERCO
fig = plt.figure(figsize=(9,6))
ax = sns.barplot(x=list(group1.groups), y= group1.EDAD.count())
plt.title('Edad de los clientes Derco\n', color="white")
plt.xticks(rotation=90)

for rect in ax.patches:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., 1*height,'%d' % int(height),ha='center', va='bottom')

plt.box(False)
plt.yticks([])
plt.ylabel('')



df_otros.EDAD_cuts = pd.cut(df_otros["EDAD"], [0,10,20,30,40,50,60,70,80,90,100,110,120], include_lowest=False)   
group1 = df_otros.groupby(df_otros.EDAD_cuts)

#edad clientes OTRAS MARCAS
fig = plt.figure(figsize=(9,6))
ax = sns.barplot(x=list(group1.groups), y= group1.EDAD.count())
plt.title('\n\nEdad de los clientes de otras marcas\n', color="white")
plt.xticks(rotation=90)

for rect in ax.patches:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., 1*height,'%d' % int(height),ha='center', va='bottom')
plt.box(False)
plt.yticks([])
plt.ylabel('')
plt.show()


#distribución de la edad de los clientes DERCO
fig = plt.figure(figsize=(9,6))
ax = sns.distplot(df_derco[df_derco['EDAD']>0]['EDAD'], kde=False)
plt.title('Distribución de la edad de los clientes de Derco', color="white")
plt.box(False)
plt.yticks([])
plt.ylabel('Densidad')


#distribución de la edad de los clientes OTRAS MARCAS
fig = plt.figure(figsize=(9,6))
ax = sns.distplot(df_otros[df_otros['EDAD']>0]['EDAD'], kde=False)
plt.title('\n\nDistribución de la edad de los clientes de otras marcas', color="white")
plt.box(False)
plt.yticks([])
plt.ylabel('Densidad')
plt.show()



#%%
#########____PLOTEAMOS LOS DATOS POR CANTIDAD DE VEHICULOS____#########

#cantidad de vehiculos derco vs otras 
fig = plt.figure(figsize=(9,6))
ax = plt.bar(df.groupby(df['MARCA'].isin(derco))['PLACA'].count().index, df.groupby(df['MARCA'].isin(derco))['PLACA'].count(), color=colors_plt)
plt.title('Cantidad de vehiculos', color="white")

for rect in ax.patches:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2., 1*height,'%d' % int(height),ha='center', va='bottom')

plt.box(False)
plt.yticks([])
plt.xticks([0,1],['OTRAS','DERCO'])

#porcentaje de vehiculos derco vs otras
fig = plt.figure(figsize=(10,5))
plt.pie(df.groupby(df['MARCA'].isin(derco))['PLACA'].count(), labels=['OTRAS', 'DERCO'], colors=colors_plt,
        autopct='%.0f%%', shadow=True, rotatelabels=False)

plt.title('\n\nPorcentaje de vehiculos', color="white")
plt.show()


#%%
#########____PLOTEAMOS LOS DATOS POR MARCAS____#########
fig = plt.figure(figsize=(15,10))
plt.pie(df[df['MARCA'].isin(derco)]['MARCA'].value_counts(), labels=df[df['MARCA'].isin(derco)]['MARCA'].value_counts().index, colors=colors_plt,
        autopct='%.0f%%', shadow=True, rotatelabels=False)

plt.title('Porcentaje de vehiculos Derco según su marca', color="white")
plt.show()


df['DERCO'] = df['MARCA'].isin(derco)
id = df.groupby(['MARCA', 'DERCO'])['PLACA'].count().sort_values().index.get_level_values(0)
ax = df.groupby(['MARCA', 'DERCO'])['PLACA'].count().unstack(1).reindex(id).plot.barh(figsize=(20,10), color=colors_plt)

plt.title('Cantidad de vehiculos por marca y si pertenecen o no a Derco')

plt.box(False)
plt.xticks([])
plt.show()


#%%
#########____PLOTEAMOS LOS DATOS POR REGIONES____#########
id = df.groupby(['REGION', 'DERCO'])['PLACA'].count().sort_values().index.get_level_values(0).unique()
ax = df.groupby(['REGION', 'DERCO'])['PLACA'].count().unstack(1).reindex(id).plot.bar(figsize=(20,10), color=colors_plt)

plt.title('Cantidad de vehiculos por región, pertenecientes o no a DERCO')
plt.box(False)
plt.show()

#%%
#########____PLOTEAMOS LOS DATOS POR VALOR____#########

#Distribución del valor de los vehiculos de los clientes de Derco
fig = plt.figure(figsize=(9,6))
ax = sns.distplot(df_derco[df_derco['VALOR_VEHICULO']>0]['VALOR_VEHICULO'])
plt.title('Distribución del valor de los vehiculos de los clientes de Derco')
plt.box(False)
plt.yticks([])
plt.ylabel('Densidad')
plt.xticks([0,5000000,10000000,15000000,20000000,25000000,30000000,35000000,40000000])

#Distribución del valor de los vehiculos de los clientes de otras marcas
fig = plt.figure(figsize=(9,6))
ax = sns.distplot(df_otros[df_otros['VALOR_VEHICULO']>0]['VALOR_VEHICULO'])
plt.title('\n\nDistribución del valor de los vehiculos de los clientes de otras marcas')
plt.box(False)
plt.yticks([])
plt.ylabel('Densidad')
plt.xticks([0,5000000,10000000,15000000,20000000,25000000,30000000,35000000,40000000])
plt.show()

#Distribución del valor de los vehiculos de los clientes de Derco según la región
ax = sns.displot(data=df_derco[df_derco['VALOR_VEHICULO']>0], x='VALOR_VEHICULO', hue='REGION', kind='kde', fill=True, height=10, aspect=1.5)
plt.title('Distribución del valor de los vehiculos de los clientes de Derco según la región')
plt.box(False)
plt.yticks([])
plt.ylabel('Densidad')


#Distribución del valor de los vehiculos de los clientes de otras marcas según la región
ax = sns.displot(data=df_otros[df_otros['VALOR_VEHICULO']>0], x='VALOR_VEHICULO', hue='REGION', kind='kde', fill=True, height=10, aspect=1.5)
plt.title('\n\nDistribución del valor de los vehiculos de los clientes de otras marcas según la región')
plt.box(False)
plt.yticks([])
plt.ylabel('Densidad')
plt.show()
