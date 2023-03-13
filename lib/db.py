from psycopg2 import connect, Error


class Database(object):
    def __init__(self, host: str = None, socket_path:str = None, ):
        socket_path = socket_path
        self.cursor = None
        self.conn = None

    def connect(self):
        ...

    def query(self, sql: str = None, commit: bool = False) -> None:
        try:
            if sql:
                self.cursor.execute(sql)

            if commit:
                self.cursor.commit()
        except Error as e:
            print(e.pgerror)
