from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random

# Create your views here.

def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

guesses_dictionary = "guesses.txt"
answers_dictionary = "answers.txt"

guesses = load_dictionary(guesses_dictionary)
answers = load_dictionary(answers_dictionary)

@api_view(['GET'])
def word(request):
    if request.method == 'GET':
        secret_word = random.choice(answers).lower()
        return Response(secret_word)
    
db = {
    "letters": [
      {"key": "A"},
      {"key": "B"},
      {"key": "C"},
      {"key": "D"},
      {"key": "E"},
      {"key": "F"},
      {"key": "G"},
      {"key": "H"},
      {"key": "I"},
      {"key": "J"},
      {"key": "K"},
      {"key": "L"},
      {"key": "M"},
      {"key": "N"},
      {"key": "O"},
      {"key": "P"},
      {"key": "Q"},
      {"key": "R"},
      {"key": "S"},
      {"key": "T"},
      {"key": "U"},
      {"key": "V"},
      {"key": "W"},
      {"key": "X"},
      {"key": "Y"},
      {"key": "Z"}
    ],
    "solutions": [
      {"id": 1, "word": "ninja"},
      {"id": 2, "word": "spade"},
      {"id": 3, "word": "pools"},
      {"id": 4, "word": "drive"},
      {"id": 5, "word": "relax"},
      {"id": 6, "word": "times"},
      {"id": 7, "word": "train"},
      {"id": 8, "word": "cores"},
      {"id": 9, "word": "pours"},
      {"id": 10, "word": "blame"},
      {"id": 11, "word": "banks"},
      {"id": 12, "word": "phone"},
      {"id": 13, "word": "bling"},
      {"id": 14, "word": "coins"},
      {"id": 15, "word": "hello"}
    ]
  }

@api_view(['GET'])
def letters(request):
    if request.method == 'GET':
        return JsonResponse(db)