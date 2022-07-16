def cloud_function(json_input):
    count_arr = json_input["countArr"]
    batch_arr = json_input["batchArr"]
    threshold = json_input["threshold"]
    # Processing

    sum_value = 0
    for i in range(len(count_arr)):
        sum_value = sum_value + count_arr[i]
        if sum_value > threshold:
            break
    total_count = sum(count_arr)
    must_be_modified_batch_arr = batch_arr[i:]
    un_modified_batch_arr = batch_arr[0:i]
    # return the result
    res = {
        "totalCount": total_count,
        "unModifiedBatchArr": un_modified_batch_arr,
        "mustBeModifiedBatchArr": must_be_modified_batch_arr
    }

    return res


def main(args):
    return cloud_function(args)