from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import Match, Range

client = Elasticsearch()

def elastic_message_query(index, qStr, qgte, qlte):
    s = Search(using=client, index=index).query("bool", must=[Match(msg=qStr),Range(date={"gte": qgte, "lte": qlte})])
    s = s[0:100]
    response = s.execute()
    results = []
    results.append({'total_hits': response.hits.total.value, 'time_taken': response.took})
    for hit in response:
        results.append({'datetime': hit.date, 'user': hit.user, 'msg': hit.msg})
    return results

def elastic_chat_for_day(index, qgte, qlte):
    s = Search(using=client, index=index).query(Range(date={"gte": qgte, "lte": qlte})).sort('date')
    s = s[0:5000]
    response = s.execute()
    results = []
    for hit in response:
        results.append({'datetime': hit.date, 'user': hit.user, 'msg': hit.msg})
    return results
