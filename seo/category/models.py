from django.db import models

class Category(models.Model):
    PAGETYPE = ((0, 'category'),(1, 'sub category'),(2, 'feeds'))
    IS_ACTIVE = ((0, 'false'),(1, 'true'))
    created = models.DateTimeField(auto_now_add=True)
    int_cat_map_id = models.AutoField(primary_key=True)
    listing_page_type = models.CharField(max_length=1, default='', choices=PAGETYPE)
    domestic_url = models.TextField(blank=True, default='')
    international_url = models.TextField(blank=True, default='')
    is_active = models.CharField(max_length=1, default=1, choices=IS_ACTIVE)
    is_updated = models.CharField(max_length=1, default=0, choices=IS_ACTIVE)

    class Meta:
        ordering = ('created',)
        db_table = "international_list_mapping"