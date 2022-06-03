import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinequiz.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible d'importer Django. Êtes-vous sûr qu'il est installé et "
            "disponible sur votre variable d'environnement PYTHONPATH? As tu "
            "oublier d'activer un environnement virtuel ?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
