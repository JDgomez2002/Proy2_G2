CREATE (sofi:person {name: "Sofi"})
CREATE (lou:person {name: "Lourdes"})
CREATE (dani:person {name: "Daniel"})
CREATE (gaby:person {name: "Gaby"})
CREATE (futbol:club {name: "Club de Football"})
CREATE (basket:club {name: "Club de Basketball"})
CREATE (futbol:club {name: "Club de Football"})







CREATE (dani)-[:DEPORTE]->(basket)
CREATE (sofi)-[:ARTE]->(marimba)
CREATE (lou)-[:DEPORTE]->(voley)
MATCH (n) RETURN n

MATCH (dani:person {name: "Daniel"})










