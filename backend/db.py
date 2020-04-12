from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'ba2f5c403aa741'
app.config['MYSQL_DATABASE_PASSWORD'] = '2b95f54d'
app.config['MYSQL_DATABASE_DB'] = 'heroku_1099c592e60f16d'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-iron-east-01.cleardb.net'
mysql.init_app(app)

#mySQL command
# mysql --host=us-cdbr-iron-east-01.cleardb.net --user=ba2f5c403aa741 --password=2b95f54d --reconnect heroku_1099c592e60f16d < /Users/Britta/Documents/GitHub/SquadGoals/backend/initDatabase.sql
