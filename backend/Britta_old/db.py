#Tutorial: https://flask.palletsprojects.com/en/1.1.x/tutorial/database/
#Note: this assumes using App Faactory Function

import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    '''
    Establishes a connection to the file pointed at by the DATABASE configuration key
    '''
    if 'db' not in g: #g is a special object used to store data
        g.db = sqlite3.connect(
            current_app.config['DATABASE'], #current_app is a special object that points to the Flask application handling the request
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        #Return rows that behave like dicts
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


###INITIALISE DATABASE

def init_db():
    '''
    get_db returns a database connection, which is used to execute the commands read from the schema sql file.
    '''
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

#Define a command line command called init-db that calls the init_db function and shows a success message to the user.
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


###REGISTER FUNCTIONS WITH THE APP

    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
