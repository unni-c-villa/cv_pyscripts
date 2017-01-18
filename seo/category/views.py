from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from category.models import Category
from category.serializers import CategorySerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def categorys_list(request):
    """
    List all code category mapping.
    """
    try:
        if request.method == 'GET':
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            if serializer:
                return JSONResponse({"m":"success","s":1,"d":serializer.data})
            else:
                return JSONResponse({"m":"fail","s":0,"d":"No data available."}, status=200)
        else:
            return JSONResponse({"m":"fail","s":0,"d":"Requset Method must be GET"}, status=200)
    except Exception as e:
        return JSONResponse({"m":"fail","s":0,"d":e}, status=200)

@csrf_exempt
def categorys_create(request):
    """
    Create a new category mapping.
    """
    try:
        if request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = CategorySerializer(data=data)
            listing_page_type_flag = False
            international_url_flag = False
            if serializer.is_valid():
                for index in serializer.initial_data:
                    if index == 'domestic_url':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify domestic_url"}, status=200)
                    elif index == 'int_cat_map_id':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify int_cat_map_id"}, status=200)
                    elif index == 'is_active':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify is_active"}, status=200)
                    elif index == 'is_updated':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify is_updated"}, status=200)
                    elif index == 'listing_page_type':
                        listing_page_type_flag = True
                    elif index == 'international_url':
                        international_url_flag = True
                if listing_page_type_flag and international_url_flag:
                    if serializer.is_valid():
                        serializer.save()
                        return JSONResponse({"m":"success","s":1,"d":serializer.data}, status=200)
                    return JSONResponse({"m":"fail","s":0,"d":serializer.errors}, status=200)
                return JSONResponse({"m":"fail","s":0,"d":"Inconsistent Input: Please provide listing_page_type and international_url"}, status=200)
            return JSONResponse({"m":"fail","s":0,"d":serializer.errors}, status=200)
        else:
            return JSONResponse({"m":"fail","s":0,"d":"Requset Method must be POST"}, status=200)
    except Exception as e:        
        return JSONResponse({"m":"fail","s":0,"d":e}, status=200)

@csrf_exempt
def categorys_detail(request, pk):
    """
    List specific code category mapping.
    """
    try:
        categorys = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return JSONResponse({"m":"fail","s":0,"d":"Requseted entity does not exists."}, status=200)

    try:
        if request.method == 'GET':
            serializer = CategorySerializer(categorys)
            if serializer:
                return JSONResponse({"m":"success","s":1,"d":serializer.data})
            else:
                return JSONResponse({"m":"fail","s":0,"d":"No data available."}, status=200)
        else:
            return JSONResponse({"m":"fail","s":0,"d":"Requset Method must be GET"}, status=200)
    except Exception as e:
        return JSONResponse({"m":"fail","s":0,"d":e}, status=200)

@csrf_exempt
def categorys_update(request, pk):
    """
    Update category mapping international.
    """
    try:
        categorys = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return JSONResponse({"m":"fail","s":0,"d":"Requseted entity does not exists."}, status=200)

    try:
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = CategorySerializer(categorys, data=data)
            if serializer.is_valid():
                for index in serializer.initial_data:
                    if index == 'domestic_url':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify domestic_url"}, status=200)
                    elif index == 'int_cat_map_id':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify int_cat_map_id"}, status=200)
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
def categorys_update_dom(request, pk):
    """
    Update category mapping domestic.
    """
    try:
        categorys = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return JSONResponse({"m":"fail","s":0,"d":"Requseted entity does not exists."}, status=200)

    try:
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = CategorySerializer(categorys, data=data)
            if serializer.is_valid():
                for index in serializer.initial_data:
                    if index == 'international_url':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify international_url"}, status=200)
                    elif index == 'int_cat_map_id':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify int_cat_map_id"}, status=200)
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
def categorys_soft_delete(request, pk):
    """
    Soft delete category mapping.
    """
    try:
        categorys = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return JSONResponse({"m":"fail","s":0,"d":"Requseted entity does not exists."}, status=200)

    try:
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = CategorySerializer(categorys, data=data)
            if serializer.is_valid():
                for index in serializer.initial_data:
                    if index == 'international_url':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify international_url"}, status=200)
                    elif index == 'int_cat_map_id':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify int_cat_map_id"}, status=200)
                    elif index == 'domestic_url':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify domestic_url"}, status=200)
                    elif index == 'listing_page_type':
                        return JSONResponse({"m":"fail","s":0,"d":"Cannot have access to modify listing_page_type"}, status=200)
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