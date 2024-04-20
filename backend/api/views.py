from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from products.models import Product
import json


# Create your views here.
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title", "price"])
        data = dict(data)
        json_data_str = json.dumps(data, default=str)
    return HttpResponse(json_data_str,
                        headers={"content-type": "application/json"})
