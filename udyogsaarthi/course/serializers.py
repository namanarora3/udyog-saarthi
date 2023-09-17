from rest_framework.serializers import ModelSerializer

class CourseSerializer(ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'description', 'educator']
