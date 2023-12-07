import os
import json
import requests
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from Model import models

# Github Secret에 환경 변수로 저장
# BASE_URL = os.getenv('BASE_URL')
BASE_URL = "http://3.39.13.133:8080";


@method_decorator(csrf_exempt, name='dispatch')
class MyView(View):
    def get(self, request, id):
        # 프론트로부터 사용자가 입력한 text 전달 받음
        userText = request.GET.get('text', '')
        # 백으로부터 사용자의 userID가 id인 사용자의 세부 정보를 불러옴
        userDetails = json.loads(requests.get(f'{BASE_URL}/detail/{id}').text)

        # 각각의 대응되는 정보를 별도의 변수를 만들어 저장
        age = userDetails['age']
        gender = userDetails['gender']
        disease1 = userDetails['disease1']
        disease2 = userDetails['disease2']
        disease3 = userDetails['disease3']
        surgery = userDetails['surgery']
        hobby1 = userDetails['hobby1']
        hobby2 = userDetails['hobby2']
        hobby3 = userDetails['hobby3']
        medicine = userDetails['medicine']
        job = userDetails['job']

        if disease1 == '' and disease2 == '' and disease3 == '':
            diseaseString = ""
        elif disease2 == '' and disease3 == '':
            diseaseString = f"{disease1}을 앓았던 이력이 있어, "
        elif disease3 == '':
            diseaseString = f"{disease1}, {disease2}을 앓았던 이력이 있어, "
        else:
            diseaseString = f"{disease1}, {disease2}, {disease3}을 앓았던 이력이 있어, "

        if hobby1 == '' and hobby2 == '' and hobby3 == '':
            hobbyString = ""
        elif hobby2 == '' and hobby3 == '':
            hobbyString = f"{hobby1}를 취미로 하고, "
        elif hobby3 == '':
            hobbyString = f"{hobby1}, {hobby2}를 취미로 하고, "
        else:
            hobbyString = f"{hobby1}, {hobby2}, {hobby3}를 취미로 하고, "

        if medicine == '':
            medicineString = ""
        else:
            medicineString = f"{medicine}을 복용 중이고, "

        if surgery == '':
            surgeryString = ""
        else:
            surgeryString = f"{surgery} 경력이 있으며, "

        if job == '':
            jobString = ""
        else:
            jobString = 