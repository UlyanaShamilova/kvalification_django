from cohere import Client
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

def index(request):
    return render(request, 'server_app/index.html')

cohere_client = Client(api_key='hptqGGiQSxLYf6eIvzJKxIlkqnn5gdRTFNSf1Izu')

@api_view(['POST'])
def chat_bot_view(request):
    user_message = request.data.get('message', '').strip()

    if not user_message:
        return Response({'reply': 'Будь ласка, введіть текст для запитання.'})

    system_message = """ You are a polite and helpful assistant who responds in the language the user writes in.
    You never say "no". Instead, if something is not possible, you gently explain alternatives like "Yes, it's possible, but you might want to consider this approach...".
    At the end of every answer, add an interesting fact related to the user's question to enrich the conversation.
    Always maintain respect, friendliness, and professionalism."""

    try:
        response = cohere_client.chat(
            model="command-nightly", #command-xlarge-nightly
            message=user_message,
            preamble=system_message
        )
        ai_reply = response.text
    except Exception as e:
        ai_reply = f"Помилка при запиті до Cohere API: {str(e)}"

    return Response({'reply': ai_reply})