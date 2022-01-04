import pymysql
import pandas as pd


def get_dataframe(value, description) -> pd.DataFrame:
    """
    transform sql query result to DataFrame

    :param tuple value:
    :param description:
    :return:
    """
    result = pd.DataFrame(value, columns=[x[0] for x in description])
    return result.groupby(level=0, axis=1).first()


class DatabaseTool:
    __exercise_base = {"topic", "topic_picture", "answer", "answer_picture"}
    __exercise_extra = {"category", "chapter", "section", "difficulty"}

    def __init__(self, host, user, password, database):
        """
        connect the database by argus

        :param str host: database host
        :param str user: user name
        :param str password: user password
        :param str database: database name
        """
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
        try:
            self.__conn = pymysql.connect(host=self.__host, user=self.__user, password=self.__password,
                                          database=self.__database)
            self.__cursor = self.__conn.cursor()
        except pymysql.err.OperationalError as e:
            print("DataBase connect error")

    def __execution(self, sql_sentence):
        """
        execution the sql sentences

        :param list sql_sentence: sql sentences to execution
        :return: result of the execution
        """
        try:
            for sql in sql_sentence:
                self.__cursor.execute(sql)
        except pymysql.err.Error as e:
            self.__conn.rollback()
            print("Sql execution error")
        else:
            self.__conn.commit()
        result = self.__cursor.fetchall()
        return result, self.__cursor.description

    def add(self, tables, columns, values):
        """
        add to tables

        :param list tables: tables to add
        :param list columns: columns in add
        :param list values: values to add
        :return:
        """
        sql = []
        for t, c, v in zip(tables, columns, values):
            sql.append("insert into %s (%s) values (%s);" % (t, c, v))
        self.__execution(sql)

    def delete(self, tables, conditions):
        """
        Delete eligible items from tables

        :param list tables: list of table
        :param list conditions: list of condition to delete
        :return:
        """
        sql = []
        for t, c in zip(tables, conditions):
            sql.append("delete from %s where %s;" % (t, c))
        self.__execution(sql)

    def update(self, tables, contents, conditions):
        """
        Update tables

        :param list tables: table to update
        :param list contents: the contents to update
        :param list conditions: update item with this conditions
        :return:
        """
        sql = []
        for table, content, condition in zip(tables, contents, conditions):
            sql.append("update %s set %s where %s;" % (table, content, condition))
        self.__execution(sql)

    def query(self, tables, columns, conditions) -> pd.DataFrame:
        """
        Query items from tables

        :param list tables: query from these tables
        :param list columns: echo these columns
        :param list conditions: query condition
        :return:
        """
        sql = []
        for t, col, con in zip(tables, columns, conditions):
            sql.append("select %s from %s %s;" % (col, t, con))

        value, description = self.__execution(sql)
        return get_dataframe(value, description)

    def get_last_id(self):
        sql = ["select @@IDENTITY;"]
        value, description = self.__execution(sql)
        return value[0][0]

    def __del__(self):
        self.__cursor.close()
        self.__conn.close()
