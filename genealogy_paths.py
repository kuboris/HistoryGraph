### USING TIGERGRAPH PATH ENDPOINTS FIND GENEALOGICAL CONNECTIONS BETWEEN IDS
import pyTigerGraph

### EDIT WITH YOUR PWD AND HOST
conn = pyTigerGraph.TigerGraphConnection(
    host="https://history.i.tgcloud.io", password="pwd", useCert=True)
print(conn.gsql('ls', options=[]))
###
conn.graphname = "genealogy"
conn.apiToken = conn.getToken(conn.createSecret())
### GET THE PATHS
source_person_id = 1
target_person_id = 350
paths = conn.allPaths([('person', source_person_id)], [('person', target_person_id)],
                        maxLength=7)
print(paths)

