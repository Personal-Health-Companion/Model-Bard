import json
import requests
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from Model import models



@method_decorator(csrf_exempt, name='dispatch')
class MyView(View):
    def get(self, request, id):

        text = request.GET.get('text', '')  # 'text' 파라미터가 없는 경우 빈 문자열을 기본값으로 사용

        user_details = json.loads(requests.get('http://3.39.13.133:8080/detail/1').text)
        age = user_details['age']
        gender = user_details['gender']
        disease1 = user_details['disease1']
        disease2 = user_details['disease2']
        disease3 = user_details['disease3']
        surgery = user_details['surgery']
        hobby1 = user_details['hobby1']
        hobby2 = user_details['hobby2']
        hobby3 = user_details['hobby3']
        medicine = user_details['medicine']

        input_String = f"내가 {age}이고 {gender}이며 {disease1},{disease2},{disease3}을 앓았던 이력이 있어, 그리고 {hobby1},{hobby2},{hobby3}를 취미로 하고 {medicine}을 복용 중이고 {surgery} 경력이 있어."

        returnString = input_String + " " + text + " " + "어떤 병원에 가야 할까?"
        response = models.bard(returnString)
        print(response)

        return HttpResponse(response)
