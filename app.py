import pymysql
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("app"),
    autoescape=select_autoescape()
)

serverIP            = "127.0.0.1"
serverUser          = "root"  
serverUserPwd       = "MYSQL$q1w2e3r4."       
characterSet        = "utf8mb4"
cursorType          = pymysql.cursors.DictCursor

dbname              = "taskninja"
dbtable             = "client"

mySQLConnection   = pymysql.connect(host=serverIP,
                                    user=serverUser,
                                    password=serverUserPwd,
                                    charset=characterSet,
                                    cursorclass=cursorType)

columns = None
try:
    cursorObject    = mySQLConnection.cursor()                                  
    cursorObject.execute(f"DESCRIBE {dbname}.{dbtable}")
    columns = cursorObject.fetchall()
    print(columns)
except Exception as e:
    print("Exception occured:{}".format(e))
    columns = None
finally:
    mySQLConnection.close()

if columns is not None:
    template = env.get_template("procedure_insert_simple.sql")
    print(template.render(table=dbtable, columns=columns))
