import psycopg2

from _functions.config import config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

"""
pseudocode for collab filtering

1. visitors en sessions pakken
2a type visitor
2b/ events pakken
2c/ similars
2d/ upselling duurdere variant verkopen
2e/ crossselling aan verwanten producten
2f/ deepselling meer verkopen aan soort gelijken producten
2g/ kijken naar sessions over de financieel situatie
3. linken in koppeltabel content
4. recommandaties geven
"""


def collaborativeFilter():
    commands = ["DROP TABLE IF EXISTS collaborativeFilter",
                "CREATE TABLE collaborativeFilter AS SELECT idvisitors, typevisitors FROM visitors ORDER BY typevisitors"]
    db = config()
    con = psycopg2.connect(**db)
    cursor = con.cursor()
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    for command in commands:
        cursor.execute(command)
        con.commit()
    con.close()
    return