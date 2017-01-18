from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from product.models import Product
from product.serializers import ProductSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def products_list(request):
    """
    List all code product mapping.
    """
    try:
        if request.method == 'GET':
            product = Product.objects.all()
            serializer = ProductSerializer(product, many=True)
            if serializer:
                return JSONResponse({"m":"success","s":1,"d":serializer.data})
            else:
                return JSONResponse({"m":"fail","s":0,"d":"No data available."}, status=200)
        else:
            return JSONResponse({"m":"fail","s":0,"d":"Requset Method must be GET"}, status=200)
    except Exception as e:
        return JSONResponse({"m":"fail","s":0,"d":e}, status=200)
    

@csrf_exempt
def products_create(request):
    """
    Create a new products mapping.
    """
    try:
        if request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ProductSerializer(data=data)
            vendor_sku_flag = False
            international_pdp_url_flag = False
            international_pid_flag = False
            if serializer.is_valid():
                for index in serializer.initial_data:
                    if index == 'domestic_pdp_url':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify domestic_pdp_url"}, status=200)
                    elif index == 'domestic_pid':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify domestic_pid"}, status=200)
                    elif index == 'int_pdp_map_id':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify int_pdp_map_id"}, status=200)
                    elif index == 'is_updated':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify is_updated"}, status=200)
                    elif index == 'vendor_sku':
                        vendor_sku_flag = True
                    elif index == 'international_pdp_url':
                        international_pdp_url_flag = True
                    elif index == 'international_pid':
                        international_pid_flag = True
                if vendor_sku_flag and international_pdp_url_flag and international_pid_flag:
                    if serializer.is_valid():
                        serializer.save()
                        return JSONResponse({"m":"success","s":1,"d":serializer.data}, status=200)
                    return JSONResponse({"m":"fail","s":0,"d":serializer.errors}, status=200)
                return JSONResponse({"m":"fail","s":0,"d":"Inconsistent Input: Please provide vendor_sku,international_pdp_url and international_pid"}, status=200)
            return JSONResponse({"m":"fail","s":0,"d":serializer.errors}, status=200)
        else:
            return JSONResponse({"m":"fail","s":0,"d":"Requset Method must be POST"}, status=200)
    except Exception as e:
        return JSONResponse({"m":"fail","s":0,"d":e}, status=200)
    

@csrf_exempt
def products_detail(request, pk):
    """
    List specific code product mapping.
    """
    try:
        products = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JSONResponse({"m":"fail","s":0,"d":"Requseted entity does not exists."}, status=200)

    try:
        if request.method == 'GET':
            serializer = ProductSerializer(products)
            if serializer:
                return JSONResponse({"m":"success","s":1,"d":serializer.data})
            else:
                return JSONResponse({"m":"fail","s":0,"d":"No data available."}, status=200)
        else:
            return JSONResponse({"m":"fail","s":0,"d":"Requset Method must be GET"}, status=200)
    except Exception as e:
        return JSONResponse({"m":"fail","s":0,"d":e}, status=200)

@csrf_exempt
def products_update(request, pk):
    """
    Update product mapping international.
    """
    try:
        products = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JSONResponse({"m":"fail","s":0,"d":"Requseted entity does not exists."}, status=200)
    
    try:
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ProductSerializer(products, data=data)
            if serializer.is_valid():
                for index in serializer.initial_data:
                    if index == 'domestic_pdp_url':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify domestic_pdp_url"}, status=200)
                    elif index == 'domestic_pid':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify domestic_pid"}, status=200)
                    elif index == 'int_pdp_map_id':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify int_pdp_map_id"}, status=200)
                    elif index == 'is_active':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify is_active"}, status=200)
                    elif index == 'is_updated':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify is_updated"}, status=200)
                if serializer.is_valid():
                    serializer.save()
                    return JSONResponse({"m":"success","s":1,"d":serializer.data}, status=200)
                return JSONResponse({"m":"fail","s":0,"d":serializer.errors}, status=200)
            return JSONResponse({"m":"fail","s":0,"d":serializer.errors}, status=200)
        else:
            return JSONResponse({"m":"fail","s":0,"d":"Requset Method must be PUT"}, status=200)
    except Exception as e:
        return JSONResponse({"m":"fail","s":0,"d":e}, status=200)

@csrf_exempt
def products_update_dom(request, pk):
    """
    Update product mapping domestic.
    """
    try:
        products = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JSONResponse({"m":"fail","s":0,"d":"Requseted entity does not exists."}, status=200)

    try:
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ProductSerializer(products, data=data)
            if serializer.is_valid():
                for index in serializer.initial_data:
                    if index == 'vendor_sku':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify vendor_sku"}, status=200)
                    elif index == 'international_pdp_url':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify international_pdp_url"}, status=200)
                    elif index == 'international_pid':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify international_pid"}, status=200)
                    elif index == 'int_pdp_map_id':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify int_pdp_map_id"}, status=200)
                    elif index == 'is_active':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify is_active"}, status=200)
                if serializer.is_valid():
                    serializer.save()
                    return JSONResponse({"m":"success","s":1,"d":serializer.data}, status=200)
                return JSONResponse({"m":"fail","s":0,"d":serializer.errors}, status=200)
            return JSONResponse({"m":"fail","s":0,"d":serializer.errors}, status=200)
        else:
            return JSONResponse({"m":"fail","s":0,"d":"Requset Method must be PUT"}, status=200)
    except Exception as e:
        return JSONResponse({"m":"fail","s":0,"d":e}, status=200)

@csrf_exempt
def products_soft_delete(request, pk):
    """
    Soft delete product mapping.
    """
    try:
        products = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JSONResponse({"m":"fail","s":0,"d":"Requseted entity does not exists."}, status=200)

    try:
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ProductSerializer(products, data=data)
            if serializer.is_valid():
                for index in serializer.initial_data:
                    if index == 'vendor_sku':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify vendor_sku"}, status=200)
                    elif index == 'international_pdp_url':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify international_pdp_url"}, status=200)
                    elif index == 'international_pid':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify international_pid"}, status=200)
                    elif index == 'int_pdp_map_id':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify int_pdp_map_id"}, status=200)
                    elif index == 'domestic_pdp_url':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify domestic_pdp_url"}, status=200)
                    elif index == 'domestic_pid':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify domestic_pid"}, status=200)
                    elif index == 'is_updated':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify is_updated"}, status=200)
                if serializer.is_valid():
                    serializer.save()
                    return JSONResponse({"m":"success","s":1,"d":serializer.data}, status=200)
                return JSONResponse({"m":"fail","s":0,"d":serializer.errors}, status=200)
            return JSONResponse({"m":"fail","s":0,"d":serializer.errors}, status=200)
        else:
            return JSONResponse({"m":"fail","s":0,"d":"Requset Method must be PUT"}, status=200)
    except Exception as e:
        return JSONResponse({"m":"fail","s":0,"d":e}, status=200)
    