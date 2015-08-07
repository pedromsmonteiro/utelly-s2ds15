###PURPOSE : some general purposes function




def becomes_list(a):
    """Return the input as a list if it is not yet"""

    if isinstance(a,list):
        return a
    else:
        return [a]


def add_to_list(list1, new_element):
    """Concatenate new_element to a list

    Parameters:
    ----------
    list1: list
        Must be a list
    new_element : any
        new element to be added at the end of list1
    """

    return list1+becomes_list(new_element)
        
    
