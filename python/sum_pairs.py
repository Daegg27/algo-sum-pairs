def sum_pairs_function(given_list, desired_sum):
    final_list = []
    real_final_list = []
    i_condition = len(given_list)

    for number in range(0, len(given_list)):
        for nextValue in given_list:
            if given_list[number] == nextValue:
                continue
            if given_list[number] + nextValue == desired_sum:
                final_list.append([given_list[number], nextValue])
    

    for x in final_list:
        if x[1] > x[0]:
            # print(f"Deleted {x[0]} and {x[1]}")
            real_final_list.append([x[0], x[1]])
             
    # print(real_final_list)
    
    if real_final_list == []:
        return "unable to find pairs"
    else: 
        return real_final_list
        
