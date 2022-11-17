
import json
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie


def add_view(request, *args, **kwargs):
    if request.method == 'POST' and request.body:
        try:
            num = json.loads(request.body)
            number_a = int(num['A'])
            number_b = int(num['B'])
            add = number_a + number_b
            response = JsonResponse({'add': add})
            print(response)
            response.status_code = 200
        except ValueError:
            response_data = {'error': 'Incorrect number format!'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


def subtract_view(request, *args, **kwargs):
    if request.method == 'POST' and request.body:
        try:
            num = json.loads(request.body)
            number_a = int(num['A'])
            number_b = int(num['B'])
            subtract = number_a - number_b
            response = JsonResponse({'subtract': subtract})
            print(response)
            response.status_code = 200
        except ValueError:
            response_data = {'error': 'Incorrect number format!'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


def multiply_view(request, *args, **kwargs):
    if request.method == 'POST' and request.body:
        try:
            num = json.loads(request.body)
            number_a = int(num['A'])
            number_b = int(num['B'])
            multiply = number_a * number_b
            response = JsonResponse({'multiply': multiply})
            print(response)
            response.status_code = 200
        except ValueError:
            response_data = {'error': 'Incorrect number format!'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


def divide_view(request, *args, **kwargs):
    if request.method == 'POST' and request.body:
        try:
            num = json.loads(request.body)
            number_a = int(num['A'])
            number_b = int(num['B'])
            divide = number_a / number_b
            response = JsonResponse({'divide': divide})
            print(response)
            response.status_code = 200
        except ValueError:
            response_data = {'error': 'Incorrect number format!'}
            response = JsonResponse(response_data)
            response.status_code = 400
        except ZeroDivisionError:
            response_data = {'error': 'Division by zero!'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


@ensure_csrf_cookie
def get_token(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(f'Not allowed method {request.method}')

