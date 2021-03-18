import psycopg2
import pandas as pd

from _functions.config import config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def contentFilter():
    # Pas deze regel aan om de database aan te passen
    commands = ["DROP TABLE contentFilter",
                "CREATE TABLE contentFilter AS SELECT idproducts, Concat(category, doelgroep, target) AS combined  FROM products ORDER BY combined"]
    db = config()
    con = psycopg2.connect(**db)
    cursor = con.cursor()
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    for command in commands:
        cursor.execute(command)
        con.commit()
    con.close()
    return