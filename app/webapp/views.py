
import json
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.views.generic import TemplateView


@csrf_exempt
def add_view(request, *args, **kwargs):
    if request.method == 'POST' and request.body:
        try:
            num = json.loads(request.body)
            number_a = int(num['A'])
            number_b = int(num['B'])
            add = number_a + number_b
            response = JsonResponse({'answer': add, 'error': ''})
        except ValueError:
            response_data = {'error': 'Incorrect number format!'}
            response = JsonResponse(response_data)
        response.status_code = 200
        return response


@csrf_exempt
def subtract_view(request, *args, **kwargs):
    if request.method == 'POST' and request.body:
        try:
            num = json.loads(request.body)
            number_a = int(num['A'])
            number_b = int(num['B'])
            subtract = number_a - number_b
            response = JsonResponse({'answer': subtract, 'error': ''})
        except ValueError:
            response_data = {'error': 'Incorrect number format!'}
            response = JsonResponse(response_data)
        response.status_code = 200
        return response


@csrf_exempt
def multiply_view(request, *args, **kwargs):
    if request.method == 'POST' and request.body:
        try:
            num = json.loads(request.body)
            number_a = int(num['A'])
            number_b = int(num['B'])
            multiply = number_a * number_b
            response = JsonResponse({'answer': multiply, 'error': ''})
        except ValueError:
            response_data = {'error': 'Incorrect number format!'}
            response = JsonResponse(response_data)
        response.status_code = 200
        return response


@csrf_exempt
def divide_view(request, *args, **kwargs):
    if request.method == 'POST' and request.body:
        try:
            num = json.loads(request.body)
            number_a = int(num['A'])
            number_b = int(num['B'])
            divide = number_a / number_b
            response = JsonResponse({'answer': divide, 'error': ''})
        except ValueError:
            response_data = {'error': 'Incorrect number format!'}
            response = JsonResponse(response_data)
        except ZeroDivisionError:
            response_data = {'error': 'Division by zero!'}
            response = JsonResponse(response_data)
        response.status_code = 200
        return response


class IndexView(TemplateView):
    template_name = 'index.html'


@ensure_csrf_cookie
def get_token(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(f'Not allowed method {request.method}')

