# HistoryGraph
![Screenshot 2022-04-20 175416](https://user-images.githubusercontent.com/5594182/164273048-602a639c-0a06-4d8c-b513-8859eb74325f.png)

## Empower historians and public with novel approach to study of genealogy and ancestry
**Contributers and Contact Information:

Jana M. and Jakub K. - see Devpost submission for contact details**
https://devpost.com/software/historygraph-graph-for-better-understanding-of-history

**Problem Statement addressed: see problem statement.md**:

https://github.com/kuboris/HistoryGraph/blob/main/problem_statement.md

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

Our solution is enabling historians and users in a following ways:

### Impact:
There are two main areas impacted by and benefiting from our solution.

1) We provide professional historians with tools and queries allowing for a more complex 
exploration of multi-generational ancestral relations than would ever be possible by means of traditional databases 
currently at hand. We believe graph databases have a potential to be a game-changer for genealogy making research 
easier, faster and able to achieve a more precise understanding of the past allowing us to find new insights into our 
history and heritage.

2) According to Precedence Research, the global genetic testing market size was valued at USD 8 billion in 2021. (https://www.globenewswire.com/news-release/2022/01/06/2362697/0/en/Genetic-Testing-Market-Size-to-Hit-USD-15-8-Billion-by-2030.html)
As we mention in our presentation, genealogy research is becoming more and more popular with people from all backgrounds
exploring their own family roots and heritage. Our solution is a perfect tool for them to organize the data sets they collect
and visualize their findings.

### Innovation:
There are several points showing the innovativeness of our solution:

1) We utilize TigerGraph to work with genealogical data in new ways which are not possible when using 
traditional table format databases. TigerGraph allows us to process tens of thousands of records and achieve 
deep analysis and insights across dozens of generations and hundreds of years. This is something that would take 
a lot of time and effort to work out from traditional sources and would be even harder to visualize in a comprehensive way. 
The fact that TigerGraph is able to achieve it quickly and easily shows that is a major innovation for genealogy researchers.

2) We believe this is one of the first ever usages of advanced algorithms such as page-rank algorithm on the 
genealogical historical data.

3) We have created a well working GSQL schema that allows for an easy upload of genealogy data format.

4) Our solution is open sourced and public, meaning it can be used and developed further by anyone.

### Ambition:
We tested our solution with the help of two different sets of historical data.
our understanding is that these are the two biggest publicly available historical datasets. 
1) UK royal family dataset (~3100 historical persons (vertex) connected to UK royal family (7488edges))
Public source: https://webtreeprint.com/tp_famous_gedcoms.php (Best resource we found so far)
2) Extensive royal families database (~58 000 historical persons)

- We have created the schema for loading GED datasets with 4 types of edges and 1 type of vertexes with personal properties.
- We have created queries with genealogical questions that users can immediately use to answer their questions.
- We have provided code to run TigerGraph pathfinding algorithms on the genealogical datasets.
- We have provided an example for running page-rank on genealogical databases.
- We have tested the finding of connections between persons across hundreds of years: TigerGraph is able to handle 
it without any issues.

### Application

Our solution is there for professional historians as well as amateur researchers, for universities, various research 
organizations and associations focusing on different historical, genealogical or even genetic questions.
The fact that TigerGraph is able to quickly and easily process tens of thousands of records and achieve 
deep analysis and insights across dozens of generations and hundreds of years makes it a perfect research tool 
for all of them. The comprehensive visualization in GraphStudio is another major help applicable throughout their research
process. The solution is open sourced and public making it readily available to anyone as well as flexible enough for further 
development and adaptation for various research needs.

## Other additions: 

 - **Data**: 
   - Used two main public dataset. 
   1) UK royal family dataset (~3 000 historical persons connected to UK royal family) Public source: https://webtreeprint.com/tp_famous_gedcoms.php
   2) Extensive royal families database (~58 000 historical persons) Available after registration: https://www.openicpsr.org/openicpsr/project/117045/version/V2/view
 - **Technology Stack**: 
   - Main programming language used: Python
   - Libraries: pyTigerGraph - For communication with TigerGraph
   - Tiger GraphStudio - For visualizations
 - **Visuals**: 
   - Queen Victoria PageRank graph![victoria_graph](https://user-images.githubusercontent.com/5594182/164274143-7c141da7-454a-4b61-8d62-529f02a5c0a2.png)

   - Detection of cyclic relations in genealogy![cyclic examples](https://user-images.githubusercontent.com/5594182/164274230-e203ac7b-3452-4df3-902a-e10e76ef4774.png)
   - Victoria connection paths to Henry II ![connection examples](https://user-images.githubusercontent.com/5594182/164274355-52fd035e-1c75-4758-8348-a4bf839af0c8.png)


All examples can be repeated using the provided code. 

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
