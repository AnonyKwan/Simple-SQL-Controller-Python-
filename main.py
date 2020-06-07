import cx_Oracle
import os
from pprint import pprint
from colorama import init
from termcolor import colored
init()
# sql.execute(sqlquery) – – – -> to execute single query.
# sql.execute(sqlqueries) – – – -> to execute a group of multiple sqlquery seperated by “;”

class SQL_CONTROLLER (object):
    def __init__(self,ac = 'null',pwd = 'null'):
        self.ac = ac
        self.pwd = pwd
    def get_ac (self):
        return self.ac
    def get_pwd (self):
        return self.pwd
    def set_ac (self,newac):
        self.ac = newac
    def set_pwd (self,newpwd):
        self.pwd = newpwd
    def connection_test (self):
        try:
            con = cx_Oracle.connect('{}/{}@localhost:1521/XE'.format(self.ac,self.pwd))
            sql = con.cursor()
            print("THE DATEBASE IS CONNECTED!\n")
            sql.close()
            con.close()
        except cx_Oracle.DatabaseError as e:
            print ("There is a problem with Oracle", e,'n')
    def __str__(self):
        return "This is SQL Controller Created By A/K."

class SQL_EXEC (SQL_CONTROLLER):
    def __init__(self,ac,pwd):
        SQL_CONTROLLER.__init__(self,ac,pwd)
        self.exec = 'null'
    def sql_execution (self,exec):
        try:
            con = cx_Oracle.connect('{}/{}@localhost:1521/XE'.format(self.ac,self.pwd))
            sql = con.cursor()
            sql.execute(exec)
            result = sql.fetchall()
            for _ in result:
                pprint(_)
            print("The SQL is executed!\n")
            sql.close()
            con.close()
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e,'\n')
            print ("SQL:" ,exec)

class add_record (SQL_CONTROLLER):
    def __init__(self,ac,pwd):
        SQL_CONTROLLER.__init__(self,ac,pwd)
        self.income_value = int
        self.income_desc = ''
        self.market_value = float
    def add (self,income_value,income_desc,market_value):
        try:
            con = cx_Oracle.connect('{}/{}@localhost:1521/XE'.format(self.ac, self.pwd))
            sql = con.cursor()
            sql.callproc('add_record',[income_value,income_desc,market_value])
            print ("Data Has Been added!\n")
            sql.close()
            con.close()
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e,'\n')

class add_market_deposit (SQL_CONTROLLER):
    def __init__(self,ac,pwd):
        SQL_CONTROLLER.__init__(self,ac,pwd)
        self.market_deposit = int
    def get_market_deposit (self):
        return self.market_deposit
    def set_market_deposit (self,newmp):
        self.market_deposit = newmp
    def add (self,market_deposit):
        try:
            con = cx_Oracle.connect('{}/{}@localhost:1521/XE'.format(self.ac, self.pwd))
            sql = con.cursor()
            sql.callproc('add_market_deposit',[160])
            print ("Data Has Been added!\n")
            sql.close()
            con.close()
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e,'\n')
    def __str__(self):
        return "\n This Function is still under developing!\n Please Paste the Following Qurey to the SQL Console! \n execute add_market_deposit({})\n".format(self.market_deposit)

clear = lambda: os.system('cls')

print("You Are Going To Login The Database!")

login_account = ''
login_password = ''

while True:
    print("0. Login With AC_FINANCE\n")
    print("1. Database Connection Test\n")
    print("2. Execute SQL Qureies (SELECT STATEMENT)\n")
    print("3. Add Record for Income_Value,Market_Value\n")
    print("4. Add Market Deposit Value\n")
    print("9. Login With Other User\n")
    while True:
        try:
            user_select = int(input("Select a function with Number!\n"))
        except ValueError:
            print("WRONG INPUT,PLEASE TRY AGAIN!\n")
            continue
        else:
            break

    if user_select == 0:
        login_account = 'ac_finance'
        login_password = 'QQWWEE123'
        print("Login Successfully!\n")
    elif user_select == 1:
        DB = SQL_CONTROLLER(login_account, login_password)
        DB.connection_test()
    elif user_select == 2:
        user_exec = str(input("Type Your SQL Queries Here!"))
        execDB = SQL_EXEC(login_account, login_password)
        execDB.sql_execution(user_exec)
    elif user_select == 3:
        user_income_value = int(input("Type Your Income!\n"))
        user_income_desc = str(input("Type Your Income Description!\n"))
        user_market_value = float(input("Type Your Stocks Value!\n"))
        add_record_DB = add_record(login_account,login_password)
        add_record_DB.add(user_income_value,user_income_desc,user_market_value)
    elif user_select == 4:
        user_market_deposit_value = int(input("Type Your Deposit Value To The Market!\n"))
        add_market_deposit_DB = add_market_deposit(login_account,login_password)
#        add_market_deposit_DB.add(user_market_deposit_value)
        add_market_deposit_DB.set_market_deposit(user_market_deposit_value)
        print(colored(add_market_deposit_DB,"red"))
    elif user_select == 9:
        login_account = input("Type Your Account Here!\n")
        login_password = input("Type Your Password Here!\n")


#sql.close()
#con.close()