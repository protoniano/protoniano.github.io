
def hacedor(a_doc:list):
    escuela_dict = dict()
    lugar_dict = dict()
    nota_dict = dict()

    notaList_menor_de_diez = nota_dict['notas < 10'] = list()
    notaList_mayor_de_diez = nota_dict['notas > 10'] = list()

    for i in a_doc:
        page_info = i.informacion_relevante
        escuela = page_info['escuela']
    
        escuela_existente_actual = escuela_dict.get(escuela, 0)
        if(escuela_existente_actual == 0):
            escuela_existente_actual = escuela_dict[escuela] = list()

        for individuo in page_info['individuos']:

            escuela_existente_actual.append(individuo)
            
            #selecciona y almacena de acuerdo al lugar

            lugar = individuo['lugar']
            lugar_existente_actual = lugar_dict.get(lugar, 0)
            if(lugar_existente_actual == 0):
                lugar_existente_actual = lugar_dict[lugar] = list()           
            lugar_existente_actual.append(individuo)

            #selecciona y almacena de acuerdo a la nota

            nota_del_individuo = individuo['nota']
            if(nota_del_individuo < 10):
                notaList_menor_de_diez.append(individuo)
            else:
                notaList_mayor_de_diez.append(individuo)

    return {'lugar':lugar_dict,'escuela':escuela_dict,'nota':nota_dict}

def hacedor_simple(pages:list):

    #canr = {'N_alumnos':int(),'notas':list()}
    # al usar copy en canr no funciona
    escuela_dict = dict()
    lugar_dict = dict()
    nota_dict = dict()
    cantidad_de_individuos = int()

    cantidad_con_mn10 = int()
    cantidad_con_my10 = int()
    
    for page in pages:
        page_info = page.informacion_relevante
        escuela = page_info['escuela']

        escuela_exist = escuela_dict.get(escuela,0)
        
        if(escuela_exist == 0):
            escuela_exist = escuela_dict[escuela] = {'N_alumnos':int(),'notas':list()}
        
        for individuo in page_info['individuos']:
            nota_del_individuo = individuo['nota']
            lugar_del_individuo = individuo['lugar']
            
            lugar_exist = lugar_dict.get(lugar_del_individuo, 0)

            if(lugar_exist == 0):
                lugar_exist = lugar_dict[lugar_del_individuo] = {'N_alumnos':int(),'notas':list()}

            lugar_exist['N_alumnos'] += 1
            lugar_exist['notas'].append(nota_del_individuo)

            if(nota_del_individuo < 10):
                cantidad_con_mn10 = cantidad_con_mn10 + 1
            else:
                cantidad_con_my10 = cantidad_con_my10 + 1

            escuela_exist['N_alumnos']+=1
            escuela_exist['notas'].append(nota_del_individuo)            

            cantidad_de_individuos+=1

    nota_dict['notas > 10'] = cantidad_con_my10
    nota_dict['notas < 10'] = cantidad_con_mn10

    return {'x_individuos':cantidad_de_individuos,'lugar':lugar_dict,'escuela':escuela_dict,'nota':nota_dict}

