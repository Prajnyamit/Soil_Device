from rest_framework import serializers
from app.models.soil_sample import SoilSample


class SoilSampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoilSample

        fields = [
            "id",
            "crop_name"
            "crop_age"
            "field_image"
            "user_problem"
            "sample_name",
            "location",
            "latitude",
            "longitude",
            "ph",
            "nitrogen",
            "phosphorus",
            "potassium",
            "moisture",
            "temperature",
            "ec",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]