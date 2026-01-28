#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite1.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    #execute_from_command_line(sys.argv)

    #If statement that checks the argument you pass after python on pwershell and changes the port to 8001 if argument is runserver
    if len(sys.argv)==2 and sys.argv[1]== "runserver":
        port = os.getenv("PORT", "8000")
        execute_from_command_line([sys.argv[0], "runserver", f"0.0.0.0:{port}"])
    else:
        execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
