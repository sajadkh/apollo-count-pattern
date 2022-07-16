def cloud_function(json_input):
    modified_str_arr = json_input["modifiedStrArr"]
    un_modified_str_arr = json_input["unModifiedStrArr"]
    
    # Processing
    result_un_modified = ' '.join(un_modified_str_arr)
    result_modified = ' '.join(modified_str_arr)

    result = result_un_modified + " " + result_modified


    # return the result
    res = {
        "modifiedStr": result
    }
    return res


def main(args):
    return cloud_function(args)