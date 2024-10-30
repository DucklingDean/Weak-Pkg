import sqlite3

CREATE_WORDLISTS_TABLE = """
CREATE TABLE IF NOT EXISTS wordlists(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    title   TEXT NOT NULL,
    rank    TEXT NOT NULL,
    size    TEXT NOT NULL,
    comp    TEXT NOT NULL,
    keys    TEXT NOT NULL,
    url     TEXT NOT NULL,
    hashsum TEXT NOT NULL,
    rate    TEXT NOT NULL,


    "download name" TEXT NOT NULL,
    "torrent name"  TEXT NOT NULL,
    "download link" TEXT NOT NULL,
    "torrent link"  TEXT NOT NULL
);
"""

FIND_BY_URL = """
SELECT * FROM wordlists WHERE url = ?;
"""

FIND_BY_ID = FIND_BY_URL.replace("url", "id")


ADD_WORDLIST = """
INSERT INTO wordlists (
    id,
    title, 
    rank,
    size,
    comp,
    keys,
    url,
    hashsum,
    rate,
    "download name",
    "download link",
    "torrent name", 
    "torrent link"
)
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
"""



class DataBase:





    def __init__(self) -> None:
        self.connection = sqlite3.connect("file.db")
        self.cur        = self.connection.cursor()
        self.cur.execute(CREATE_WORDLISTS_TABLE)



    def _new_id(self) -> int:
        n = 1
        while True:
            if self.id_exsits(n):
                n += 1
            else: return n

        


    def add(self, wordlist:dict[str,str]) -> None:
        self.cur.execute(
            ADD_WORDLIST, 
            (
                self._new_id(),
                wordlist["title"],
                wordlist["rank"],
                wordlist["size"],
                wordlist["comp_size"],
                wordlist["keys"],
                wordlist["url"],
                wordlist["hashsum"],
                wordlist["rate"],
                wordlist["dw_name"],
                wordlist["dw_link"],
                wordlist["tr_name"],
                wordlist["tr_link"],

            )
        )



    def url_exsits(self, url) -> bool:
        self.cur.execute(FIND_BY_URL, (url,))
        return bool(self.cur.fetchone())



    def id_exsits(self, id) -> bool:
        self.cur.execute(FIND_BY_ID, (id,))
        return bool(self.cur.fetchone())
 


    def save(self) -> None:
        self.connection.commit()



    def close(self) -> None:
        self.cur.close()
        self.connection.close()





