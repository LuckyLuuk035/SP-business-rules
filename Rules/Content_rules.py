import psycopg2
import pandas as pd

from _functions.config import config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

"""
pseudocode for content filtering

1. Categorys gaan pakken
2. Orders/events pakken 
2a/ populaire producten pakken
2b/ genders pakken
2c/ prijzen pakken
2d/ brand pakken
2e/ product name pakken
2f/ variant pakken?
2g/ aanbieding pakken/folder actief
3. query analyseren
4. visitors en products aan linken in koppeltabel similars
5. recommendations geven

"""

def contentFilter():
    # Pas deze regel aan om de database aan te passen
    commands = ["CREATE TABLE contentFilter AS SELECT idproducts, category, doelgroep, target FROM products"]
    db = config()
    con = psycopg2.connect(**db)
    cursor = con.cursor()
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    for command in commands:
        cursor.execute(command)
        con.commit()
    print('Done')
    con.close()
    return