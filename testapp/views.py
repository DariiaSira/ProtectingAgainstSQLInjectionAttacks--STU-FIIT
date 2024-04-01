from django.shortcuts import render
from django.db import connection
from .models import User

def search_users_info_vulnerable(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        print("Search query:", search_query)  # Отладочное сообщение
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM my_database.users WHERE username LIKE '%" + search_query + "%'")
        users = cursor.fetchall()
        print("Found users:", users)  # Отладочное сообщение
        return render(request, 'search_results.html', {'users': users})
    else:
        return render(request, 'search_users.html')

def search_users_info_protected (request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        print("Search query:", search_query)  # Отладочное сообщение
        users = User.objects.filter(username__icontains=search_query)
        print("Found users:", users)  # Отладочное сообщение
        return render(request, 'search_results.html', {'users': users})
    else:
        return render(request, 'search_users.html')


def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})