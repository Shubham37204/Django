from django.db import models
from django.urls import reverse

class Movies(models.Model):
    
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(max_length=100, default='action')
    image = models.ImageField(
        upload_to="images/", default="images/None/None.jpg")


#steps for serializers are

# 1. crtae a model.py ie class Movies(models.Model):
# 2. create a serializer.py  ie class MovieSerializer(serializers.ModelSerializer):
# 3. create a view.py  ie class MovieViewSet(viewsets.ModelViewSet):
#4. create a urls.py to map the viewset to urls ie path('', include(router.urls)),
