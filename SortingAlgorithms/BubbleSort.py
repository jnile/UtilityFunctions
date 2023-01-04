def bubble_sort(inp_list:list, ascending_order:bool = True) -> None:
    """Bubble Sort Algorithm to sort the list.

    Note: 
        Variable is changed!

    Args:
        inp_list (list): List of items to sort.
        ascending_order (bool, optional): Set to False for decending order. Defaults to True.
    """

    changed = True
    counter = 0
    while changed:
        changed = False
        for x in range(len(inp_list)-1-counter):
            if inp_list[x] > inp_list[x+1]:
                if ascending_order:
                    inp_list[x], inp_list[x+1] = inp_list[x+1], inp_list[x]
                    changed = True
            elif(inp_list[x] == inp_list[x+1]):
                pass
            else:
                if not ascending_order:
                    inp_list[x], inp_list[x+1] = inp_list[x+1], inp_list[x]
                    changed = True
        counter += 1