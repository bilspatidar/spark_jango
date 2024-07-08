from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

@method_decorator(csrf_exempt, name='dispatch')
class TestView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            title = data.get('title')
            amount = data.get('amount')
            description = data.get('description')
        except json.JSONDecodeError:
            title = request.POST.get('title')
            amount = request.POST.get('amount')
            description = request.POST.get('description')
        
        response_data = {
            'message': 'POST request received successfully',
            'title': title,
            'amount': amount,
            'description': description,
        }
        
        return JsonResponse(response_data)
    
    def get(self, request, *args, **kwargs):
        response_data = {
            'message': 'GET request received successfully'
        }
        
        return JsonResponse(response_data)

# New view for root URL
@method_decorator(csrf_exempt, name='dispatch')
class RootView(View):
    def get(self, request, *args, **kwargs):
        response_data = {
            'message': 'Welcome to the root URL!'
        }
        return JsonResponse(response_data)

    def post(self, request, *args, **kwargs):
        response_data = {
            'message': 'POST request received at root URL'
        }
        return JsonResponse(response_data)
