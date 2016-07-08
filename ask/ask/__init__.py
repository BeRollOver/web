import os
if(os.path.dirname(__file__)[0] is 'C'):
    import pymysql
    pymysql.install_as_MySQLdb()

