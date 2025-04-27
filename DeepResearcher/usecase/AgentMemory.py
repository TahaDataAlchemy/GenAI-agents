from pymongo import MongoClient
from datetime import datetime
from app.config import settings
class AgentMemory:
    def __init__(self,db_uri = settings.MONGO_URI,db_name = settings.DB_NAME,collection_name = settings.UserMemory):
        self.client = MongoClient(db_uri)
        self.collection = self.client[db_name][collection_name]
    
    def add(self,query,related_questions,relevent_link,UserProvidedLink,summary):
        self.collection.insert_one(
            {
                "query":query,
                "UserProvidedLink":UserProvidedLink,
                "related_question":related_questions,
                "relevent_link":relevent_link,
                "timestamp":datetime.utcnow(),
                "summary":summary
            }
        )
    def get_all(self):
        return list(self.collection.find({},{"_id":0})) # empty dictionary means all values and _id:0 means i dont need id field

    def get_last(self):
        return self.collection.find_one(sort = ["timestamp",-1],projection = {"_id":0}) # projection doing the same as it is excluding the _id

    def search_context(self,keyword): # it avoid search and based on previous queries fetch the similar ones
        return list(
            self.collection.find(
                {"query":{"$regex":keyword,"$option":"i"}},
                {"_id":0}
            )
        )
    def clear_memory(self):
        self.collection.delete_many({})
    
    def suggest_next_queries(self,recent_count=3):
        recent = self.collection.find({},{"_id":0,"query":1}).sort("timestamp",-1).limit(recent_count)
        return [q["query"] for q in recent]