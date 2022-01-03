import pymysql
import pandas as pd


class DatabaseOperate:
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

    def __execution(self, *sql_sentence):
        """
        execution the sql sentences

        :param str sql_sentence: sql sentences to execution
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

    def add_exercise(self, topic, topic_picture, answer, answer_picture, category, chapter, section, difficulty):
        """
        add exercise to database

        :param str topic: describe of the exercise with ''
        :param str topic_picture: picture to supplement described
        :param str answer: answer of the exercise with ''
        :param str answer_picture: picture to supplement answer
        :param str category: category of the exercise with '' include '选择','填空','判断','名词解释','问答','算法','计算'
        :param int chapter: chapter of the exercise
        :param int section: section of the exercise
        :param str difficulty: difficulty of with the exercise with '' include '高','中','低'
        :return: None
        """
        sql_base = "insert into exercise_base_info (topic,topic_picture,answer,answer_picture) values (%s,%s,%s,%s);" % (
            topic, topic_picture, answer, answer_picture)
        sql_extra = "insert into exercise_extra_info (category,chapter,section,difficulty) values (%s,%d,%d,%s);" % (
            category, chapter, section, difficulty)
        self.__execution(sql_base, sql_extra)

    def delete_exercise(self, exercise_id):
        """
        delete the exercise from database by exercise id

        :param int exercise_id: the only representation of the exercise
        :return:
        """
        sql = "delete from exercise_base_info where ExerciseCode = %d;" % exercise_id
        self.__execution(sql)

    def query_exercise(self, condition) -> pd.DataFrame:
        """
        query exercise from database by condition.
        condition="all" means query all exercise

        :param str condition: query by condition
        :return:
        """

        sql = "select * from %s left join %s on %s.ExerciseCode = %s.ExerciseCode " % (
            "exercise_base_info", "exercise_extra_info", "exercise_base_info", "exercise_extra_info")
        if condition == "all":
            sql += ';'
        else:
            sql += condition + ';'

        value, description = self.__execution(sql)
        result = pd.DataFrame(value, columns=[x[0] for x in description])
        return result.groupby(level=0, axis=1).first()

    def update_exercise(self, exercise_id, columns, values):
        """
        update exercise by argus


        :param int exercise_id: the only representation of the exercise
        :param columns: the all index of the update values
        :param values: all update value
        :return:
        """
        pretreatment = dict(zip(columns, values))
        update_base = []
        update_extra = []
        for key, value in pretreatment.items():
            if key in {"topic", "topic_picture", "answer", "answer_picture"}:
                update_base += [key + '=' + value]
            if key in {"category", "chapter", "section", "difficulty"}:
                update_extra += [key + '=' + value]
        sql_base = "update exercise_base_info set %s where ExerciseCode=%d;" % (','.join(update_base), exercise_id)
        sql_extra = "update exercise_extra_info set %s where ExerciseCode=%d;" % (','.join(update_extra), exercise_id)
        self.__execution(sql_base, sql_extra)

    def __del__(self):
        self.__cursor.close()
        self.__conn.close()


def main():
    bop = DatabaseOperate("104.168.172.47", "forfind", "000000", "exercise")
    pd.set_option('display.max_columns', None,
                  'display.max_rows', None,
                  'display.max_colwidth', None,
                  'display.width', 100,
                  'expand_frame_repr', False)
    print(bop.update_exercise(2, ['answer', 'difficulty', 'topic'], ["'B'", "'中'", "'测试'"]))


if __name__ == '__main__':
    main()
