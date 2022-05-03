CREATE (sofi:person {name: "Sofi"})
CREATE (lou:person {name: "Lourdes"})
CREATE (dani:person {name: "Daniel"})
CREATE (gaby:person {name: "Gaby"})
CREATE (maria:person {name: "Maria"})
CREATE (ligia:person {name: "Ligia"})
CREATE (vicky:person {name: "Victoria"})
CREATE (ruth:person {name: "Ruth"})
CREATE (mynor:person {name: "Mynor"})
CREATE (otto:person {name: "Otto"})
CREATE (pablo:person {name: "Pablo"})
CREATE (monica:person {name: "Monica"})

CREATE (futbol:club {name: "Club de Football"})
CREATE (basket:club {name: "Club de Basketball"})
CREATE (ajedrez:club {name: "Club de Ajedrez"})
CREATE (voley:club {name: "Club de Voleiball"})
CREATE (marimba:club {name: "Club de Marimba"})
CREATE (karaoke:club {name: "Club de Karaoke"})
CREATE (pintura:club {name: "Club de Pintura"})
CREATE (videojuegos:club {name: "Club de Videojuegos"})
CREATE (atletismo:club {name: "Club de Atletismo"})

CREATE (dani)-[:FRIENDS]->(sofi)
CREATE (dani)-[:FRIENDS]->(lou)
CREATE (lou)-[:FRIENDS]->(gaby)
CREATE (sofi)-[:FRIENDS]->(lou)
CREATE (sofi)-[:FRIENDS]->(otto)
CREATE (otto)-[:FRIENDS]->(mynor)
CREATE (otto)-[:FRIENDS]->(maria)
CREATE (ligia)-[:FRIENDS]->(vicky)
CREATE (monica)-[:FRIENDS]->(pablo)
CREATE (ruth)-[:FRIENDS]->(pablo)
CREATE (pablo)-[:FRIENDS]->(ligia)

CREATE (dani)-[:DEPORTE]->(basket)
CREATE (sofi)-[:ARTE]->(marimba)
CREATE (lou)-[:DEPORTE]->(voley)
CREATE (ligia)-[:ARTE]->(pintura)
CREATE (pablo)-[:DEPORTE]->(basket)
CREATE (otto)-[:DEPORTE]->(basket)
CREATE (lou)-[:ARTE]->(pintura)
CREATE (mynor)-[:DEPORTE]->(futbol)
CREATE (ruth)-[:DEPORTE]->(futbol)
CREATE (vicky)-[:DEPORTE]->(voley)
CREATE (ruth)-[:DEPORTE]->(ajedrez)
CREATE (ruth)-[:DEPORTE]->(futbol)
CREATE (monica)-[:ARTE]->(karaoke)
CREATE (maria)-[:DEPORTE]->(basket)


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
