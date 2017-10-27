from django.http import JsonResponse
import requests


def health():
    r = requests.get('https://api.somesite.com/status')
    if r.status_code == requests.codes.ok:
        return JsonResponse({'status': 200}, status=200)
    else:
        return JsonResponse({'status': 503, 'error': r.text}, status=503)
