from rest_framework import serializers
from advanceProfile.models import Adv_prof



class Adv_profClass(serializers.ModelSerializer):
    class Meta:
        model = Adv_prof
        fields = '__all__'