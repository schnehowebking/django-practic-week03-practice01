from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    d= {
        'name': 'Amir',
        'age': 20,
        'fvS':['physics', 'chem', 'math', 'programing'],
        'clg': 'Rangur Eng. Clg',
        "date": datetime.datetime.now(),
        "dics": [
            {'name': 'Josh', 'age': 19},
            {'name': 'Dave', 'age': 22},
            {'name': 'Joe', 'age': 31},
        ],
        "escap":'<p>You are <em>pretty</em> smart!</p>', 
        "line": '''cat
            dog
            horse''',
        "slicees" : '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.''',
    }
    
    return render(request, 'app1/home.html', d)