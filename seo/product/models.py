from django.db import models

class Product(models.Model):
    IS_ACTIVE = ((0, 'false'),(1, 'true'))
    created = models.DateTimeField(auto_now_add=True)
    int_pdp_map_id = models.AutoField(primary_key=True)
    vendor_sku = models.CharField(max_length=100, blank=True, default='')
    domestic_pdp_url = models.TextField(blank=True, default='')
    domestic_pid = models.CharField(max_length=100, blank=True, default='')
    international_pdp_url = models.TextField(blank=True, default='')
    international_pid = models.CharField(max_length=100, blank=True, default='')
    is_active = models.CharField(max_length=1, default=1, choices=IS_ACTIVE)
    is_updated = models.CharField(max_length=1, default=0, choices=IS_ACTIVE)

    class Meta:
        ordering = ('created',)
        db_table = "international_pdp_mapping"