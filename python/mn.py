import json
from mani import Docer

config = {
    'sede_index':0,
    'escuela_index':5,
    'cantidad_de_lineas_constantes':6,
    'ca_ant':6,
    'ca_des':1
}

#def cheker(en_la_lista, busca):
#
#    if(len(en_la_lista) == 0):
#        return 'no-existe'
#
#    index = 0
#
#    while(en_la_lista[index][0] != busca):
#        if(index+1 >= len(en_la_lista)):
#            return 'no-existe'
#        index+=1
#    
#    return index
    
a_doc = Docer(config)

file = 'zona_4.txt'

a_doc.loadFileAndStart(file)

the_dict = dict()

lugar_list = the_dict['lugar'] = dict()
escuela_list = the_dict['escuela'] = dict()
nota_list = the_dict['nota'] = dict()

notaList_menor_de_diez = nota_list['notas < 10'] = list()
notaList_mayor_de_diez = nota_list['notas > 10'] = list()

for i in a_doc.pages:
    page_info = i.informacion_relevante
    escuela = page_info['escuela']
    
    escuela_existente_actual = escuela_list.get(escuela, 0)
    if(escuela_existente_actual == 0):
        escuela_existente_actual = escuela_list[escuela] = list()

    for individuo in page_info['individuos']:

        escuela_existente_actual.append(individuo)
        
        #selecciona y almacena de acuerdo al lugar

        lugar = individuo['lugar']
        lugar_existente_actual = lugar_list.get(lugar, 0)
        if(lugar_existente_actual == 0):
            lugar_existente_actual = lugar_list[lugar] = list()           
        lugar_existente_actual.append(individuo)

        #selecciona y almacena de acuerdo a la nota

        nota_del_individuo = individuo['nota']
        if(nota_del_individuo < 10):
            notaList_menor_de_diez.append(individuo)
        else:
            notaList_mayor_de_diez.append(individuo)
            

for i in the_dict['lugar']:
    print(i+": "+str(len(the_dict['lugar'][i])))


with open(file.split('.')[0]+'.json', 'w', encoding='utf-8') as json_file:
    json.dump(the_dict,json_file, ensure_ascii=False)
    json_file.close()