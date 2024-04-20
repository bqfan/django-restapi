import json
from django.http import JsonResponse


# Create your views here.
def api_home(request, *args, **kwargs):
    print(request.GET)
    print(request.POST)
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass

    data["params"] = dict(request.GET)
    data["headers"] = dict(request.headers)
    # json.dumps(dict(request.headers))
    data["content_type"] = request.content_type

    return JsonResponse(data)
