from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON, N3
from flask import Flask, render_template, request

app = Flask(__name__)

sparql = SPARQLWrapper("http://DESKTOP-L652HRK:7200/repositories/Datos_Polvo_y_Ceniza")

def __init__(self, query):
    self.query = query

@app.route('/')
def init():
    return render_template('index.html')

@app.route('/Consulta', methods=['POST'])
def buscar():
    if request.method == 'POST':
        textoBuscar = request.form['textoBuscar']
        if "Buscar" in request.form :
            if request.form == "Autor":
                sparql.setQuery("""
                PREFIX bibo: <http://purl.org/ontology/bibo/>
                PREFIX dct: <http://purl.org/dc/terms/>
                PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                SELECT ?document ?name ?date ?language ?nombre_autor ?volume
                WHERE{  
                    values ?nombre_autor {'"""+textoBuscar+"""'}
                    ?document a bibo:Document .
                    ?document dct:title ?name .
                    ?document dct:date ?date .  
                    ?document bibo:doi ?doi .
                    ?document dct:language ?language .
                    ?document bibo:volume ?volume .
                    ?document dct:creator ?autor .
                    ?autor foaf:name ?nombre_autor
                    }
                """)
            else:
                if request.form == "Anio":
                    sparql.setQuery("""
                    PREFIX bibo: <http://purl.org/ontology/bibo/>
                    PREFIX dct: <http://purl.org/dc/terms/>
                    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                    SELECT ?document ?name ?date ?language ?nombre_autor ?volume
                    WHERE{  
                        values ?nombre_autor {'"""+textoBuscar+"""'}
                        ?document a bibo:Document .
                        ?document dct:title ?name .
                        ?document dct:date ?date .  
                        ?document bibo:doi ?doi .
                        ?document dct:language ?language .
                        ?document bibo:volume ?volume .
                        ?document dct:creator ?autor .
                        ?autor foaf:name ?nombre_autor
                        }
                    """)
                else:
                    sparql.setQuery("""
                    PREFIX bibo: <http://purl.org/ontology/bibo/>
                    PREFIX dct: <http://purl.org/dc/terms/>
                    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                    SELECT ?document ?name ?date ?language ?volume ?autor_name
                    WHERE{ 
                        values ?doi{'"""+ textoBuscar+"""'}
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
            
            qres = sparql.query().convert()
            #print('\nRESULTADOS ENCONTRADOS:\n')
            if qres:
                return render_template('Resultados.html', resultsQuery=qres)


app.run(host='localhost', port=5000, debug=True)
