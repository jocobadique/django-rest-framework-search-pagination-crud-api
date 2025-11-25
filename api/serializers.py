from rest_framework import serializers
from .models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Drink
        fields = ["id", "name", "category", "category_name"]

    # Custom validation for duplicate name
    def validate_name(self, value):
        # Creating a new drink
        if self.instance is None:
            if Drink.objects.filter(name__iexact=value).exists():
                raise serializers.ValidationError("Drinks already exists")

        # Updating an existing drink
        else:
            if (
                Drink.objects.filter(name__iexact=value)
                .exclude(id=self.instance.id)
                .exists()
            ):
                raise serializers.ValidationError("Drinks already exists")

        return value
