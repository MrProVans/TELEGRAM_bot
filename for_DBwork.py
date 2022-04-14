import datetime
import sqlite3


class DB:
    def __init__(self):
        self.con = sqlite3.connect('db_For_TGbot.sqlite')

    def add_user(self, surname, name, patronymic, post, id_tg):  # добавление пользователя
        self.con.cursor().execute(f'''INSERT INTO Users(surname, name, patronymic, post, id_tg)
         VALUES ('{surname}', '{name}', '{patronymic}', {post}, '{id_tg}')''')
        self.con.commit()

    def add_company(self, title, phone, password):  # добавление компании
        self.con.cursor().execute(f'''INSERT INTO Companies(title, number_phone, password_cl)
         VALUES ('{title}', '{phone}', '{password}')''')
        self.con.commit()

    def delete_company(self, title):  # удаление компании
        self.con.cursor().execute(f'''DELETE from Companies 
        WHERE title = \'{title}\'''')
        self.con.commit()

    def check_mailing(self, text, date, company):  # проверка наличия уведомления
        if self.con.cursor().execute(f'''SELECT count(*) FROM Mailings
         WHERE text = '{text}' AND
          date = '{date}' AND
           company = \'{company}\'''').fetchall()[0][0] != 0:
            return True
        else:
            return False

    def add_mailing(self, text, date, company):  # добавление уведомления
        self.con.cursor().execute(f'''INSERT INTO Mailings(text, date, company)
         VALUES ('{text}', '{date}', '{company}')''')
        self.con.commit()

    def delete_mailing(self, text, date, company):  # удаление уведомления
        self.con.cursor().execute(f'''DELETE from Mailings 
        WHERE text = '{text}' AND
          date = '{date}' AND
           company = \'{company}\'''')
        self.con.commit()

    def check_question_all(self, text_q, text_a, company):  # проверка вопроса на полную уникальность
        if self.con.cursor().execute(f'''SELECT count(*) FROM Questions
         WHERE text_q = '{text_q}' AND
          text_a = '{text_a}' AND
           company = \'{company}\'''').fetchall()[0][0] != 0:
            return True
        else:
            return False

    def add_question(self, text_q, text_a, company):  # добавление вопроса
        self.con.cursor().execute(f'''INSERT INTO Questions(text_q, text_a, company)
                 VALUES ('{text_q}', '{text_a}', '{company}')''')
        self.con.commit()

    def check_question(self, text_q, company):  # проверка вопроса на существование
        if self.con.cursor().execute(f'''SELECT count(*) FROM Questions
         WHERE text_q = '{text_q}' AND
           company = \'{company}\'''').fetchall()[0][0] != 0:
            return True
        else:
            return False

    def redact_question(self, text_q, text_a, company):  # редактирование вопроса
        self.con.cursor().execute(f'''UPDATE Questions
        SET text_a = '{text_a}'
         WHERE text_q = '{text_q}' AND
           company = \'{company}\'''')
        self.con.commit()

    def delete_question(self, text_q, text_a, company):  # удаление вопроса
        self.con.cursor().execute(f'''DELETE from Questions
                 WHERE text_q = '{text_q}' AND
                  text_a = '{text_a}' AND
                   company = \'{company}\'''')
        self.con.commit()

    def get_questions(self, company):  # получение всех вопросов для данной компании
        return '\n'.join([str(x[0] + 1) + '. ' + x[1][0]
                          for x in enumerate(self.con.cursor().execute(f'''SELECT text_q FROM Questions
         WHERE company = \'{company}\'''').fetchall())])

    def get_company_password(self, company):  # получение пароля для клиентов компании
        return self.con.cursor().execute(f'''SELECT password_cl FROM Companies
         WHERE title = \'{company}\'''').fetchall()[0][0]

    def check_company(self, company):  # проверка компании на существование
        if self.con.cursor().execute(f'''SELECT count(*) FROM Companies
         WHERE title = \'{company}\'''').fetchall()[0][0] != 0:
            return True
        else:
            return False



bd = DB()
# bd.add_company('a', 'b', 'c')
# bd.add_user('a', 'b', 'c', 1, '12432wer')
# bd.delete_company('a')
# bd.add_mailing('a', '01.01.01', 'A')
# print(bd.check_mailing('a', '01.01.01', 'A'))
# bd.delete_mailing('a', '01.01.01', 'A')
# bd.add_question('a3', 'b4', 'Comp')
# print(bd.check_question_all('a', 'b', 'c'))
# bd.redact_question('a', 'b', 'c')
# bd.delete_question('a', 'b', 'c')
# print(bd.check_question('a', 'c'))
# print(bd.get_questions('Comp'))
# print(bd.get_company_password('a'))
# print(bd.check_company('a'))
