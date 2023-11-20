# Trade Flow Analysis Global
<h2>This is a project as part of the Social Network Analysis course of the degree in computer science for management at the university of bologna</h2>
<br>In the context of global economic evolution, trade data analysis plays a crucial role in
understanding trade dynamics among nations. Globalization has expanded opportunities for
interchange, bringing with it increasing complexity in international trade patterns. Against
this backdrop, this study aims to explore and analyze the BACI dataset provided by the
French research center CEPII (Centre d'Etudes Prospectives d'Informations Internationales)
on global trade.
Link dataset: http://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=37

<br><h3>Objectives:</h3>
1. To understand how the density of trade between countries changes over
time and the consequences of these changes.
2. Identify the most influential countries in the trade network through
measures of centrality
3. Transform theoretical network analysis into practical and applicable results
for decision makers and stakeholders

<h3>Project Contributions:</h3>
- <b>Theoretical Significance:</b> The project will contribute to the development of
international trade network theory by integrating temporal analysis and node influence
assessment.
<br>- <b>Practical Relevance:</b> It will provide practical tools to analyze the trade network and
identify opportunities or risks related to global trade dynamics.
<br>- <b>Socio-Economic Impact:</b> Information from the project can be used to improve
understanding of global trade relations, guiding more informed and sustainable
economic decisions.

<h3>Exchange map for the year 2017:</h3>
Within figure, the global trade network for the year 2017 has been represented through an
oriented graph, in which we have:
- Nodes, representing the countries of the world identified by their ISO_3digit_alpha
- The oriented arcs, which represent an import or export of a given product from/to
other countries (nodes)
For each node, only the first two outgoing arcs (exports) are displayed, calculated based on
the value of trade (only the first two export flows were considered based on their value for
reasons of graph explicability).

![mappa2017](https://github.com/elia99l/SocialAnalysis/blob/main/figura2.jpg)

<h3>Change in trade flow density:</h3>
represents the change in trade density flow for the years 2017, 2018, 2019, 2020, and
2021. The density values by year were calculated by counting the number of connections that
came up in that year and dividing by the maximum number of connections that can be made
for a given year. 𝐷𝑒𝑛𝑠𝑖𝑡𝑦 = 𝑛links / 𝑛total
Where 𝑛links represents the number of connections made and 𝑛total represents the maximum
number of connections that can be made.

![density](https://github.com/elia99l/SocialAnalysis/blob/main/densit%C3%A0.png)
