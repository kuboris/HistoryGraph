# HistoryGraph

## Empower historians and public with novel approach to study of genealogy and ancestry
**Contributers and Contact Information: Jana M. Jakub K. - see Devpost for contact**

**Problem Statement addressed: see problem statement.md**

**Description**: 

We are utilizing TigerGraph to be able to work with genealogical data in a new ways that are enabled by usage of graph
database.
We want to empower historians as well as people with personal interest in genealogy to gain deeper, more accurate insights
from ancestral data in an easy and quick way.

Our goal is to create a solution that allows anyone to parse and upload ancestral data in GEDCOM format into 
the TigerGraph database and provide them with tools and queries allowing for a complex research of multi-generational 
ancestral relations while reaching a more accurate understanding than would ever be possible by means of a 
traditional database. We believe graph databases have a potential to be a game-changer for genealogy enabling researchers
to attain a more precise understanding of the past allowing us to find new insights into the history and/or our own ancestors. 

Our solution is enabling historians and users in a following 

- Impactful in solving a real world problem 
- Innovative use case of graph
- Ambitious and complex graph
- Applicable graph solution 

Other additions: 

 - **Data**: 
   - Used two main public dataset. 
   1) UK royal family dataset (~3 000 historical persons connected to UK royal family) Public source: https://webtreeprint.com/tp_famous_gedcoms.php
   2) Extensive royal families database (~58 000 historical persons) Available after registration: https://www.openicpsr.org/openicpsr/project/117045/version/V2/view
 - **Technology Stack**: 
   - Main programming language used: PYTHON
   - Libraries: pyTigerGraph - For communication 
   - Tiger GraphStudio - For visualizations
 - **Visuals**: 
   - Feel free to include other images or videos to better demonstrate your work.

All examples can be repeated using the provided code. 
 - Link websites or applications if needed to demonstrate your work. 

## Dependencies

Python3 and all dependencies can be installed using provided requirements.txt 
## Installation

This installation assumes python3 installed on the machine.
1. Clone repository
2. Install dependencies eg. `pip install -r requirements.txt`
3. It's recommended to use royal data provided in this repo (royal92.ged) or register and download extensive but much noisier data model from provided link.(See **Data** part)
4. Create your own TigerGraph instance and update password and url in scripts you are going to use.
5. Run main.py to fill graph database with data.
6. Run queries from genealogy_guestions.py (Tested running in GraphStudio in WriteQueries)
7. Run script genealogy_paths.py to find paths between persons. Edit id of persons you are interested in first.
8. To run TigerGraph graph algorithms (for example page-rank) pick algorithm from repo: https://github.com/tigergraph/gsql-graph-algorithms (Tested by installing and running it in GraphStudio in WriteQueries)

## Known Issues and Future Improvements

Using graph database for genealogical research is a game-changer for historical research. 
TigerGraph offers a lot of algorithms (see: https://docs-legacy.tigergraph.com/graph-algorithm-library) that were not 
yet used to find hidden relations between persons and allow us to distill new historical insights.
Current solution could be further improved by adding more historical "edges" that would further add more details into the graph.
We plan to add "mariage", "siblings", "step-siblings" edges into the graph in the future.

## Reflections

TigerGraph allowed us to work with this dataset in a way we could not imagine beforehand. Usage for GraphStudio enabled
us to visualize data in a tree form and quickly find paths that would be hidden from us beforehand.
We would however welcome possibility to have specific image as a thumbnail of an edge in GraphStudio for even better
experience. 

## References

To make this project following TigerGraph documentation and tutorials were used.
- https://towardsdatascience.com/using-api-data-with-tigergraph-ef98cc9293d3
- https://medium.com/@suobot.io/get-to-know-the-accumulators-in-gsql-in-tigergraph-through-sample-queries-1cddf5c5b2d6
- https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Centrality/pagerank/global/unweighted/tg_pagerank.gsql
