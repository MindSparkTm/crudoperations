from . import models

from rest_framework import serializers









class useradserializer(serializers.ModelSerializer):

    class Meta:
        model = models.Register
        fields = ('id', 'created','name','email','mobilenumber','postalcode')





