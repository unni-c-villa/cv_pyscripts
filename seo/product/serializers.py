from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('int_pdp_map_id', 'vendor_sku', 'domestic_pdp_url', 'domestic_pid', 'international_pdp_url','international_pid','is_active','is_updated')

    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.vendor_sku = validated_data.get('vendor_sku', instance.vendor_sku)
        instance.domestic_pdp_url = validated_data.get('domestic_pdp_url', instance.domestic_pdp_url)
        instance.domestic_pid = validated_data.get('domestic_pid', instance.domestic_pid)
        instance.international_pdp_url = validated_data.get('international_pdp_url', instance.international_pdp_url)
        instance.international_pid = validated_data.get('international_pid', instance.international_pid)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_updated = validated_data.get('is_updated', instance.is_updated)
        instance.save()
        return instance