config = dict()
import pywin

individuo = {
        'nombre':str(),
        'lugar':str(),
        'nota':float()
    }

def trier_to_name(algo:str|int):
    try:
        algo = int(algo)
        return 1
    except:
        return 0

def get_inf_and_return_ind(linea:list):

    ll = individuo.copy()
    linea.pop(0)

    name = str()
    while(trier_to_name(linea[0]) != 1):

        if(trier_to_name(linea[1]) != 1):
            name += linea[0] + ' '
        else:
            name += linea[0]

        linea.pop(0) 

    linea.pop(0)

    nota = linea[0]
    linea.pop(0)
    linea.pop(0)
    linea.pop(0)

    lugar = str()
    size = len(linea)
    for i in range(0, size):
        if(i != size-1):
            lugar += linea[i] + ' '
        else:
            lugar += linea[i]

    ll['nombre'] = name
    ll['lugar'] = lugar
    ll['nota'] = float(nota)

    return ll

def informacion_maker(lineas_page:list, a_config:dict):
        inf_rel = {
            'sede':str(),
            'escuela':str(),
            'individuos':list()
        } 
        lineas = lineas_page
        config = a_config

        sede = lineas[config['sede_index']].split(': ')
        inf_rel['sede'] = sede[1]

        escuela = lineas[config['escuela_index']].split(': ')
        inf_rel['escuela'] = escuela[len(escuela)-1]

        for i in range(config['ca_ant'],len(lineas) - config['ca_des']):
            linea_inf = lineas[i].split(' ')
            inf_rel['individuos'].append(get_inf_and_return_ind(linea_inf))

        return inf_rel

class Docer:

    def __init__(self, config:dict):
        self.pages = list()
        self.doc = str()
        self.config = config

    def loadFileAndStart(self, rul:str):
        file = open(rul, 'r', encoding='utf-8')
        self.doc = file.read()
        file.close()
        
        self.paginacion()
    
    def paginacion(self):

        pages_list = self.doc.split('\n\n')
        pages = self.pages

        for i in range(0, len(pages_list)):
            
            linea = pages_list[i].split('\n')
            pages.append(Page(linea, self.config));
                
class Page:

    def __init__(self, lista_de_lineas:list, a_config):
        self.lineas = lista_de_lineas
        self.informacion_relevante = informacion_maker(lista_de_lineas, a_config)

    