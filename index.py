heros = [
    ("Pablo",900),
    ("Marley",1001),
    ("Prisley",2001),
    ("Bob",5001),
    ("Claudio",7001),
    ("Odete",8001),
    ("Paola",9001),
    ("Lopes",10001),
]

for (hero, exp) in heros:
    level = ""
    if exp <= 1000:
        level = "Ferro"
    elif exp >= 1001 and exp <= 2000:
        level = "Bronze"
    elif exp >= 2001 and exp <= 5000:
        level = "Prata"
    elif exp >= 5001 and exp <= 7000:
        level = "Ouro"
    elif exp >= 7001 and exp <= 8000:
        level = "Platina"
    elif exp >= 8001 and exp <= 9000:
        level = "Ascendente"
    elif exp >= 9001 and exp <= 10000:
        level = "Imortal"
    elif exp >= 10001:
        level = "Radiante"


    print(f"O Herói de nome **{hero}** está no nível de **{level}**")



