from django.http import HttpResponse
from category.models import Category
from category.serializers import CategorySerializer
from product.models import Product
from product.serializers import ProductSerializer
from django.db import connection

def category_mapping(request):
	try:
		category = Category.objects.filter(is_updated=0)
		if category:
			for cat in category:
			    cat.domestic_url = cat.international_url.replace("/us/","/")
			    cat.is_updated = 1
			    cat.save()
			return HttpResponse("Done!!!")
		else:
		    return HttpResponse("No data")
	except Exception as e:
		return HttpResponse(e)

def product_mapping(request):
    try:
	    product = Product.objects.filter(is_updated=0)
	    if product:
	    	vendor_sku = [e.vendor_sku for e in product]
	    	format_strings = ','.join(['%s'] * len(vendor_sku))
	    	cursor = connection.cursor()
	    	cursor.execute("SELECT cpev.entity_id AS product_id, cpev.value AS url_key, cpev2.value AS vendor_sku FROM catalog_product_entity_varchar AS cpev LEFT JOIN catalog_product_entity_varchar AS cpev2 ON cpev.entity_id = cpev2.entity_id WHERE cpev.attribute_id = (SELECT attribute_id FROM eav_attribute WHERE attribute_code = 'url_key' AND entity_type_id = (SELECT entity_type_id FROM eav_entity_type WHERE entity_type_code = 'catalog_product')) AND cpev.entity_type_id = (SELECT entity_type_id FROM eav_entity_type WHERE entity_type_code = 'catalog_product') AND cpev.entity_id IN (SELECT entity_id FROM catalog_product_entity_varchar WHERE attribute_id = (SELECT attribute_id FROM eav_attribute WHERE attribute_code = 'vendorsku') AND entity_type_id = (SELECT entity_type_id FROM eav_entity_type WHERE entity_type_code = 'catalog_product') AND value IN (%s)) AND cpev2.attribute_id = (SELECT attribute_id FROM eav_attribute WHERE attribute_code = 'vendorsku') AND cpev2.entity_type_id = (SELECT entity_type_id FROM eav_entity_type WHERE entity_type_code = 'catalog_product') GROUP BY vendor_sku" % format_strings,tuple(vendor_sku))
	    	result = cursor.fetchall()
	    	connection.close()
	    	for row in result:
	    		productrow = Product.objects.get(vendor_sku=row[2])
	    		productrow.domestic_pdp_url = "/shop/"+row[1]+"/"+str(row[0])
	    		productrow.domestic_pid = row[0]
	    		productrow.is_updated = 1
	    		productrow.save()
	    	return HttpResponse("Done!!!!")
	    else:
	    	return HttpResponse("No data")
    except Exception as e:
		return HttpResponse(e)