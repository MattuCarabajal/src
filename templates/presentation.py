from datetime import datetime
from libs.csv import csv_to_list_dict


def get_me_data():
    me = csv_to_list_dict( 'data_vault/me.csv' )[ 0 ]
    return me

def get_date():
    date = datetime.today().strftime( '%B %Y' )
    return date

def get_ide_data():
    ide_data = {
        'language_img'     : 'static/images/icon-python.png',
        'file_name'        : 'hello_world.py',
        'branch'           : 'master',
        'encoding'         : 'UTF-8',
        'language'         : 'Python',
        'language_version' : '3.9.1'
    }
    return ide_data
