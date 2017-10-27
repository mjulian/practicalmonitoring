from django.db import connection as sql_connection
from django.http import JsonResponse


def health():
    try:
        # Connect to a SQL database and select one row
        with sql_connection.cursor() as cursor:
            cursor.execute('SELECT 1 FROM table_name')
            cursor.fetchone()
        return JsonResponse({'status': 200}, status=200)
    except Exception, e:
        return JsonResponse({'status': 503, 'error': e}, status=503)
