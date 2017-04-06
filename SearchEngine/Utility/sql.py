import mysql.connector


class MySQL(object):
    def __init__(self):
        self.host = '104.199.252.211'
        self.database = 'INFORETRIEVAL'
        self.user = 'root'
        self.password = 'cz4034'
        self.db_connection = mysql.connector.connect(host=self.host,
                                                     database=self.database,
                                                     user=self.user,
                                                     password=self.password)
        self.db_cursor = self.db_connection.cursor()

    def execute_query(self, sql_query):
        try:
            self.db_cursor.execute(sql_query)

            if sql_query[:6].lower() == "select" or sql_query[1:7].lower() == "select":
                # print "inside if"
                return self.db_cursor.fetchall()
            self.db_connection.commit()
        except Exception as error:
            print error
            self.db_connection.rollback()

    def close(self):
        self.db_connection.close()


def __main__():
    mysql_obj = MySQL()
    result = mysql_obj.execute_query("SELECT id from crawlData WHERE id='sport/2017/apr/05/wisden-comes-out-fighting-free-to-air-cricket-coverage-england-alastair-cook'")
    for id in result:
        print "{}: 1. {} 2. ".format(id, id, id)

if __name__ == __main__():
    __main__()