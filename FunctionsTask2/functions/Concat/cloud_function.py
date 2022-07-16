def cloud_function(json_input):
    modified_str_arr = json_input["modifiedStrArr"]
    un_modified_str_arr = json_input["unModifiedStrArr"]
    partialy_modified_str = json_input["partialyModifiedStr"]
    
    # Processing
    result_un_modified = ' '.join(un_modified_str_arr)
    result_modified = ' '.join(modified_str_arr)

    if partialy_modified_str != "":
        partialy_modified_str = " " + partialy_modified_str + " "
    else:
        partialy_modified_str = " "
    result = result_un_modified + partialy_modified_str + result_modified


    # return the result
    res = {
        "modifiedStr": result
    }
    return res


def main(args):
    return cloud_function(args)