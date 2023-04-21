from rest_framework import serializers
from testreact.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')

#  This code specifies the model to work with and the fields to be converted to JSON.
