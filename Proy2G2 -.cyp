CREATE (sofi:person {name: "Sofi"})
CREATE (lou:person {name: "Lourdes"})
CREATE (dani:person {name: "Daniel"})
CREATE (gaby:person {name: "Gaby"})
CREATE (futbol:club {name: "Club de Football"})
CREATE (basket:club {name: "Club de Basketball"})
CREATE (ajedrez:club {name: "Club de Ajedrez"})
CREATE (voley:club {name: "Club de Voleiball"})
CREATE (marimba:club {name: "Club de Marimba"})
CREATE (karaoke:club {name: "Club de Karaoke"})
CREATE (dani)-[:FRIENDS]->(sofi)
CREATE (dani)-[:FRIENDS]->(lou)
CREATE (lou)-[:FRIENDS]->(gaby)
CREATE (sofi)-[:FRIENDS]->(lou)

CREATE (dani)-[:DEPORTE]->(basket)
CREATE (sofi)-[:ARTE]->(marimba)
CREATE (lou)-[:DEPORTE]->(voley)
MATCH (n) RETURN n

MATCH (dani:person {name: "Daniel"})










