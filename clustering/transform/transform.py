import pdb


def call_field(collection,field_name,*args):
    """Extracts fields from a collection"""

    number_of_extra_arguments = len(args)
    event_id = []
    field_value = []
    
    for i in collection.find():
        event_id.append(i["_id"])

        if number_of_extra_arguments == 0:
            field_value.append(i[field_name])
        elif number_of_extra_arguments == 1:
            field_value.append(i[field_name][args[0]])
        elif number_of_extra_arguments == 2:
            field_value.append(i[field_name][args[0]][args[1]])
    return [event_id,field_value]


