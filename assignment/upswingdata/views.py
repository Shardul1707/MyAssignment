from pymongo import MongoClient
from datetime import datetime
from django.http import JsonResponse

# Connect to MongoDB
client = MongoClient("localhost",27017)
db = client['mqtt_data']
collection = db['messages']


def retrieve(request, startTime, endTime):
    try:
        start_time = datetime.fromisoformat(startTime)
        end_time = datetime.fromisoformat(endTime)
        count = collection.count_documents({
                    "time": {
                        "$gte": start_time,
                        "$lte": end_time
                    }
                    })
        
        return JsonResponse({'count': count})

    except Exception as e:
        raise e