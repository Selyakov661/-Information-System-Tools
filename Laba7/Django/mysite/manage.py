#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django
import pymysql

connect = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='pass',
    database='my_db'
)

cursor = connect.cursor()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    if connect:
        print("MySQL's connected", end='\n\n')

    main()
