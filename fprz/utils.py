from main.models import New
from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
def q_search(query):

    vector = SearchVector('title','content')
    query = SearchQuery(query)
    return New.objects.annotate(search=SearchRank(vector,query)).order_by("-rank")



'''
    keywords=[word for word in query.split() if len(word)>2]
    q_objects=Q()
    for token in keywords:
        q_objects |=Q(title__icontains=token)
        q_objects |=Q(content__icontains=token)
    return New.objects.filter(q_objects)
'''