from main.models import New
from django.db.models import Q
def q_search(query):
    return New.objects.filter(title__icontains=query)