# PROYECTO SBC - APLICACIÓN BÚSQUEDA DE PUBLICACIONES ODS CON GRAPHDB
# AUTORES: JOSÉ PULLAGUARI - JEFFERSON NÚÑEZ

from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON, N3


# Metodo para buscar publicaciones de un año especifico
def buscarPublicacionAnio():
    print("Ingrese el año:")
    anio = str(input())

    sparql = SPARQLWrapper("http://DESKTOP-L652HRK:7200/repositories/Datos_Polvo_y_Ceniza")
    sparql.setQuery("""
    PREFIX bibo: <http://purl.org/ontology/bibo/>
    PREFIX dct: <http://purl.org/dc/terms/>
    SELECT ?document ?name ?language
    WHERE{ 
        values ?date {'"""+anio+"""'} 
        ?document a bibo:Document . 
        ?document dct:date ?date . 
        ?document dct:title ?name .
        ?document dct:language ?language
        }
    """)


    sparql.setReturnFormat(JSON)
    cont = 0
    qres = sparql.query().convert()
    print('\nRESULTADOS ENCONTRADOS:\n')
    for res in qres['results']['bindings']:
        print('Uri: ' + res['document']['value'])
        print('Nombre: ' + res['name']['value'])
        print('Idioma: ' + res['language']['value'])
        print('\n')
        cont+=1
    
    print("Mostrando resultados: "+ str(cont))
    print("------------------------------")
    print("Desea volver a realizar alguna búsqueda Y/N")
    opcionVolver = input()
    if (opcionVolver == 'Y'):
        menuPrincipal()
    else:
        print("\nGracias por utilizar nuestra aplicación\n")

# Metodo para buscar publicaciones de un autor especifico
def buscarPublicacionAutor():
    print("Ingrese el autor:")
    Nombre = input()
    sparql = SPARQLWrapper("http://DESKTOP-L652HRK:7200/repositories/Datos_Polvo_y_Ceniza")
    sparql.setQuery("""
    PREFIX bibo: <http://purl.org/ontology/bibo/>
    PREFIX dct: <http://purl.org/dc/terms/>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    SELECT ?document ?name ?date 
    WHERE{ 
        values ?nombre_autor {'"""+Nombre+"""'} 
        ?document a bibo:Document .
        ?document dct:title ?name .
        ?document dct:date ?date .  
        ?document dct:creator ?autor . 
        ?autor foaf:name ?nombre_autor
        }
    """)

    sparql.setReturnFormat(JSON)
    cont = 0
    qres = sparql.query().convert()
    print('\nRESULTADOS ENCONTRADOS:\n')
    for res in qres['results']['bindings']:
        print('Uri: ' + res['document']['value'])
        print('Nombre: ' + res['name']['value'])
        print('Fecha: ' + res['date']['value'])
        print('\n')
        cont+=1
    
    print("Mostrando resultados: "+ str(cont))
    print("------------------------------")
    print("Desea volver a realizar alguna búsqueda Y/N")
    opcionVolver = input()
    if (opcionVolver == 'Y'):
        menuPrincipal()
    else:
        print("\nGracias por utilizar nuestra aplicación\n")

    # Metodo para buscar publicaciones por DOI
def buscarPublicacionDOI():
    print("Ingrese el valor del doi")
    doi = input()
    sparql = SPARQLWrapper("http://DESKTOP-L652HRK:7200/repositories/Datos_Polvo_y_Ceniza")
    sparql.setQuery("""
    PREFIX bibo: <http://purl.org/ontology/bibo/>
    PREFIX dct: <http://purl.org/dc/terms/>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    SELECT ?document ?name ?date ?language ?volume ?autor_name
    WHERE{ 
    	values ?doi{'"""+ doi +"""'}
        ?document a bibo:Document .
        ?document dct:title ?name .
        ?document dct:date ?date .  
    	?document bibo:doi ?doi .
		?document dct:language ?language .
    	?document bibo:volume ?volume .
    	?document dct:creator ?autor .
    	?autor foaf:name ?autor_name
        }
    """)

    sparql.setReturnFormat(JSON)
    cont = 0
    qres = sparql.query().convert()
    #print(qres)
    print('\nRESULTADOS ENCONTRADOS:\n')
    for res in qres['results']['bindings']:
        print('Uri: ' + res['document']['value'])
        print('Nombre: ' + res['name']['value'])
        print('Fecha: ' + res['date']['value'])
        print('Lenguaje: ' + res['language']['value'])
        print('Volumen: ' + res['volume']['value'])
        print('Autor: ' + res['autor_name']['value'])
        print('\n')
        cont+=1
    
    print("Mostrando resultados: "+ str(cont))
    print("------------------------------")
    print("Desea volver a realizar alguna búsqueda Y/N")
    opcionVolver = input()
    if (opcionVolver == 'Y'):
        menuPrincipal()
    else:
        print("\nGracias por utilizar nuestra aplicación\n")


# Metodo Principal
def menuPrincipal():
    print("\n------PUBLICACIONES ODS------\n")
    print("-------------MENU------------")
    print("1. Buscar publicaciones por año")
    print("2. Buscar publicaciones que pertenezcan a un autor")
    print("3. Buscar publicaciones por valor de DOI")
    print("-----------------------------")
    print("Seleccione un número\n")
    numElegido = input()

    if numElegido == "1":
        buscarPublicacionAnio()
    if numElegido == "2":
        buscarPublicacionAutor()
    if numElegido == "3":
        buscarPublicacionDOI()
        

if __name__ == '__main__':
    menuPrincipal()