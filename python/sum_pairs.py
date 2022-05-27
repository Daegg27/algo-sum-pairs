def sum_pairs_function(given_list, desired_sum):
    final_list = []
    i_condition = len(given_list)

    for number in range(0, len(given_list)):
        for nextValue in given_list:
            if given_list[number] == nextValue:
                continue
            if given_list[number] + nextValue == desired_sum:
                final_list.append([given_list[number], nextValue])
    

    for x in final_list:
        if x[0] > x[1]:
            # print(f"Deleted {x[0]} and {x[1]}")
            final_list.remove(x)
             
    # print(final_list)
    
    if final_list == []:
        return "unable to find pairs"
    else: 
        return final_list
        
