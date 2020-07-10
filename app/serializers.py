from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .models import Company,Product,Purchase,Purchase
import datetime
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class CompanySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Company
		fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'


class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Purchase
		fields = ['product','quantity']
	def create(self,validated_data):
		year = datetime.date.today().year
		n = 0
		if Purchase.objects.all().last():
				pon = Purchase.objects.all().last().purchage_order_number
				pon_list = pon.split('/')
				number = pon_list[-1]
				yr = pon_list[-2]
				n = int(number) + 1
				if int(yr) != int(year):
					n = 0
					new_pon = f'PO/{year}/{n}'
				else:
					new_pon = f'PO/{year}/{n}'
		else:
			new_pon = f'PO/{year}/{n}'

		p_cost = validated_data['product'].COST
		quantity = validated_data['quantity']
		purchase = Purchase(
			purchage_order_number = new_pon,
			product = validated_data['product'],	
			quantity = validated_data['quantity'],
			total_amount = p_cost * quantity

		)
		purchase.save()
		return purchase