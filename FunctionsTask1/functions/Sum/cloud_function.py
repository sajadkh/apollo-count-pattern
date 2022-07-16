def cloud_function(json_input):
    count_arr = json_input["countArr"]
    
    # Processing
    total_count = sum(count_arr)
    # return the result
    res = {
        "totalCount": total_count
    }
    return res


def main(args):
    return cloud_function(args)