from main.models import New
from django.db.models import Q
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
    SearchHeadline,
)


def q_search(query):

    vector = SearchVector("title", "content")
    query = SearchQuery(query)
    result = (
        New.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )
    result=result.annotate(
	    headline=SearchHeadline(
	        'title',
		    query,
		    start_sel='<span style="background-color:yellow;">',
		    stop_sel="</span>",
	        )
    )

    result=result.annotate (
	    bodyline=SearchHeadline(
	        'content',
		    query,
		    start_sel='<span style="background-color:yellow;">',
		    stop_sel="</span>",
	        )
    )
    return result

"""
    keywords=[word for word in query.split() if len(word)>2]
    q_objects=Q()
    for token in keywords:
        q_objects |=Q(title__icontains=token)
        q_objects |=Q(content__icontains=token)
    return New.objects.filter(q_objects)
"""
