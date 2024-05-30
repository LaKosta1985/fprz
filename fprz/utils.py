from main.models import *
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

