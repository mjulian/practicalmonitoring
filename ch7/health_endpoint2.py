from django.db import connection as sql_connection
from django.http import JsonResponse
import redis


def check_sql():
    try:
        # Connect to a SQL database and select one row
        with sql_connection.cursor() as cursor:
            cursor.execute('SELECT 1 FROM table_name')
            cursor.fetchone()
        return {'okay': True}
    except Exception, e:
        return {'okay': False, 'error': e}


def check_redis():
    try:
        # Connect to a Redis database and retreive a key
        redis_connection = redis.StrictRedis()
        result = redis_connection.get('test-key')

        # Compare the key's value against a known value
        if result == 'some-value':
            return {'okay': True}
        else:
            return {'okay': False, 'error': 'Test value not found'}
    except Exception, e:
        return {'okay': False, 'error': e}


def health():
    if all(check_sql().get('okay'), check_redis().get('okay')):
        return JsonResponse({'status': 200}, status=200)
    else:
        return JsonResponse(
            {
                'mysql_okay': check_sql().get('okay'),
                'mysql_error': check_sql().get('error', None),
                'redis_okay': check_redis().get('okay'),
                'redis_error': check_redis().get('error', None)
            },
            status=503
        )
