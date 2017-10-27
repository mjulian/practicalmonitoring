from django.http import JsonResponse
import redis

redis_connection = redis.StrictRedis()


def write_data():
    try:
        # Connect to Redis and set a key/value pair
        redis_connection.set('test-key', 'some-value')
        return {'okay': True}
    except Exception, e:
        return {'okay': False, 'error': e}


def read_data():
    try:
        # Connect to Redis and retrieve the key/value we set
        result = redis_connection.get('test-key')
        if result == 'some-value':
            return {'okay': True}
        else:
            return {'okay': False, 'error': 'Redis data does not match'}
    except Exception, e:
        return {'okay': False, 'error': e}


def health():
    if not write_data().get('okay'):
        return JsonResponse({'status': 503, 'error': write_data().get('error')},
                            status=503)
    else:
        if read_data().get('okay'):
            # Clean up the old data before returning the HTTP responses
            redis_connection.delete('test-key')
            return JsonResponse({'status': 200}, status=200)
        else:
            # Clean up the old data before returning the HTTP responses
            redis_connection.delete('test-key')
            return JsonResponse(
                {
                    'status': 503,
                    'error': read_data.get('error')
                },
                status=503)
