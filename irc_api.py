from fastapi import FastAPI, Query, Path, HTTPException
from datetime import datetime, date, time
from irc_elastic import elastic_message_query, elastic_chat_for_day

# Mapping of channel names and elastic indexes
channelIndex = {"Test1": "irc_test1", "Test2": "irc_test2",}

app = FastAPI()

def check_channel(channel):
    if (channel not in channelIndex):
        raise HTTPException(status_code=404, detail="Channel not found")

@app.get("/search")
def read_search(channel: str, query: str = Query(min_length=3), startdate: date = date(2000,1,1), enddate: date = date.today()):
    check_channel(channel)
    startdate = datetime.combine(startdate,time.min)
    enddate = datetime.combine(enddate,time.max)
    return elastic_message_query(channelIndex[channel],query,startdate,enddate)

@app.get("/getlog/{channel}/{date}")
def read_channel_day(channel: str, chatDate: date):
    check_channel(channel)
    startdate = datetime.combine(chatDate,time.min)
    enddate = datetime.combine(chatDate,time.max)
    return elastic_chat_for_day(channelIndex[channel],startdate,enddate)
