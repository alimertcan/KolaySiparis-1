from django.shortcuts import render

# Create your views here.
def listfood(request):
	app_label = 'app_model_belongs_to_food'
	return render_to_response('listfood.html',{'food':food.object.all()})
def listres(request):
	app_label = 'app_model_belongs_to_restaurant'
	return render_to_response('listres.html',{'food':food.object.all()})
