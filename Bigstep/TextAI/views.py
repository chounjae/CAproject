from django.http import HttpResponse
from django.shortcuts import render
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings
from decouple import config


def home(request):
    return render(request, 'textAI.html')


# OpenAI API 키 설정
openai.api_key = config('~~~~~~~')

@csrf_exempt
def beautify_text(request):
    if request.method == 'POST':
        # 사용자가 보낸 텍스트 가져오기
        data = json.loads(request.body)
        user_text = data.get('text', '')
        
        #프롬프트 설정(== 변경 할 말투 설정)
        prompt = f"입력 받은 문장을 우아한 공주님 말투로 바꿔줘:\n{user_text}"

        try:
            # OpenAI API 호출
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt = prompt,
                max_tokens=100,
                temperature=0.7
            )

            # 변환된 텍스트 추출
            beautiful_text = response['choices'][0]['text'].strip()

            return JsonResponse({'success': True, 'text': beautiful_text})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)