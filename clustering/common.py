import uuid
from utils import becomes_list, add_to_list

##duration should be expressed as datetime.timedelta object
unknown = None #define what should be put if unknown or not available


class Group():
    """Group found from clustering"""

    def __init__(self, keywords, members):
        self._id = uuid.uuid4()
        self.keywords = becomes_list(keywords)
        self.members = becomes_list(members)

    def add_member(self, new_member):
        self.members = add_to_list(self.members,new_member)


    def __repr__(self):
        return str(self.__class__.__name__)+"("+str(len(self.members))+")"




class Event():
    """Event"""

    def __init__(self, _id, **kwargs):
        self._id = _id

        ##recursively define class attributes
        for key, value in kwargs.items():
            setattr(self, key, value)





        
class Actor():
    """Actor(ress)"""

    def __init__(self):
        _id = uuid.uuid4()
        first_name = unknown
        second_name = unknown
        last_name = unknown
        date_of_birth = unknown
