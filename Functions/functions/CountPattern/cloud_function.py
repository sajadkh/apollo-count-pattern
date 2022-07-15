def cloud_function(json_input):
    batch_str = json_input["batchStr"]
    pattern = json_input["pattern"]
    
    # Processing
    count = batch_str.count(pattern)
    # return the result
    res = {
        "count": count
    }
    return res
