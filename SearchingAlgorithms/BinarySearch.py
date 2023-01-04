def binary_search(inp_list:list, item_to_search, sorted:bool = False) -> bool:
    """Binary Search Algorithm to search if the item exists in the list.

    Args:
        inp_list (list): List of the items to search from.
        item_to_search (_type_): Item to search for.
        sorted (bool, optional): State if the list is ordered. Defaults to False.

    Returns:
        bool: True if the item exists in the list.
    """
    #Order the list
    if not sorted:
        inp_list = inp_list.copy()
        inp_list.sort()
    if(inp_list == []):
        return False

    middle_index = len(inp_list) // 2
    searched_item = inp_list[middle_index]

    if(searched_item == item_to_search):
        return True
    elif(searched_item > item_to_search):
        return binary_search(inp_list[:middle_index], item_to_search)
    elif(middle_index+1 == len(inp_list)):
        return False
    else:
        return binary_search(inp_list[middle_index+1:], item_to_search)