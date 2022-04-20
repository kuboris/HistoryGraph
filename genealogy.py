from ged4py import GedcomReader
import pyTigerGraph

########## EDIT FOLLOWING PART WITH YOUR DATA
tgcloud_host = "https://history.i.tgcloud.io"
tgcloud_password = "pwd"
# CHANGE FOR YOUR OWN GED FILE
path = 'royal92.GED'
#############################################

## LOGIN
conn = pyTigerGraph.TigerGraphConnection(
    host=tgcloud_host, password=tgcloud_password, useCert=True)
print(conn.gsql('ls', options=[]))

## CREATE SCHEMA
## NAME IS NOT UNIQUE USE IDS FOR PEOPLE
print(conn.gsql('''
CREATE VERTEX person (PRIMARY_ID id UINT, name STRING, sex STRING, birth STRING, death STRING, first_name STRING, surname STRING) WITH primary_id_as_attribute="true"
CREATE DIRECTED EDGE mother_to (FROM person, TO person) WITH REVERSE_EDGE="mothers_descendant"
CREATE DIRECTED EDGE father_to (FROM person, TO person) WITH REVERSE_EDGE="fathers_descendant"
''', options=[]))
# Create the Graph
print(conn.gsql('''CREATE GRAPH genealogy(person, mother_to, father_to)''', options=[]))
conn.graphname = "genealogy"
conn.apiToken = conn.getToken(conn.createSecret())

## USE THIS CODE TO LOAD GEDCOM FILES
with GedcomReader(path, encoding="utf-8", errors='replace') as parser:
    # ITERATE TO ADD PEOPLE
    vertex_list = []
    for record in parser.records0("INDI"):
        person_name = record.name.given
        first_name = record.name.first
        surname = record.name.surname
        sex = record.sex
        birth, death = 'Unknown', 'Unknown'
        if record.sub_tag('BIRT'):
            if record.sub_tag('BIRT').sub_tag('DATE'):
                birth = str(record.sub_tag('BIRT').sub_tag('DATE').value)
        if record.sub_tag('DEAT'):
            if record.sub_tag('DEAT').sub_tag('DATE'):
                death = str(record.sub_tag('DEAT').sub_tag('DATE').value)
        id = int(record.xref_id.replace('@I', '').replace('@', ''))
        vertex_list.append((id, {"name": person_name, "first_name": first_name, "surname": surname, "sex": sex,
                                 "birth": birth, "death": death}))
    conn.upsertVertices("person", vertex_list)
    # ITERATE TO ADD CONNECTIONS
    father_list = []
    mother_list = []
    for record in parser.records0("INDI"):
        id = int(record.xref_id.replace('@I', '').replace('@', ''))
        # IF MOTHER KNOWN ADD MOTHER
        if record.mother:
            mother_id = int(record.mother.xref_id.replace('@I', '').replace('@', ''))
            mother_list.append((mother_id, id))

        # IF FATHER KNOWN ADD FATHER
        if record.father:
            father_id = int(record.father.xref_id.replace('@I', '').replace('@', ''))
            father_list.append((father_id, id))
    conn.upsertEdges("person", "mother_to", "person", mother_list)
    conn.upsertEdges("person", "father_to", "person", father_list)