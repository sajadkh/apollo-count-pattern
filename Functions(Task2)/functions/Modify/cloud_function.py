import re



def cloud_function(json_input):
    must_be_modified_batch_str = json_input["mustBeModifiedBatchStr"]
    pattern = json_input["pattern"]
    
    # Processing
    must_be_modified_batch_str = must_be_modified_batch_str.replace(pattern, "")
    must_be_modified_batch_str = re.sub(' +', ' ', must_be_modified_batch_str).strip()
    # return the result
    res = {
        "modifiedStr": must_be_modified_batch_str
    }
    print(res)
    return res


def main(args):
    return cloud_function(args)