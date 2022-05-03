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
SET dani.birthday = date("2002")
RETURN dani

MATCH (lou:person {name: "Lourdes"})
SET lou.birthday = date("2002")
RETURN lou

MATCH (sofi:person {name: "Sofia"})
SET sofi.birthday = date("2002")
RETURN sofi

MATCH (gaby:person {name: "Gabriela"})
SET gaby.birthday = date("2003")
RETURN gaby