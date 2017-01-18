from rest_framework import serializers
from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('int_cat_map_id', 'listing_page_type', 'domestic_url', 'international_url','is_active','is_updated')

    def create(self, validated_data):
        """
        Create and return a new `Category` instance, given the validated data.
        """
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Category` instance, given the validated data.
        """
        instance.listing_page_type = validated_data.get('listing_page_type', instance.listing_page_type)
        instance.domestic_url = validated_data.get('domestic_url', instance.domestic_url)
        instance.international_url = validated_data.get('international_url', instance.international_url)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_updated = validated_data.get('is_updated', instance.is_updated)
        instance.save()
        return instance