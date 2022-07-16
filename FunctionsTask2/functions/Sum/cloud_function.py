def rreplace(s, old, new, occurrence):
  li = s.rsplit(old, occurrence)
  return new.join(li)


def cloud_function(json_input):
    count_arr = json_input["countArr"]
    batch_arr = json_input["batchArr"]
    threshold = json_input["threshold"]
    # Processing

    sum_value = 0
    must_be_partial_modified = {}
    must_be_partial_modified_str = ""
    must_be_partial_modified_remained_pattern =0
    for i in range(len(count_arr)):
        new_sum_value = sum_value + count_arr[i]
        if new_sum_value > threshold and sum_value == threshold:
            break
        elif new_sum_value > threshold:
            must_be_partial_modified_str = batch_arr[i]
            must_be_partial_modified_remained_pattern = threshold - sum_value
            i = i + 1
            break
        sum_value = new_sum_value
    total_count = sum(count_arr)
    must_be_modified_batch_arr = batch_arr[i:]
    un_modified_batch_arr = batch_arr[0:i]
    # return the result
    res = {
        "totalCount": total_count,
        "unModifiedBatchArr": un_modified_batch_arr,
        "mustBeModifiedBatchArr": must_be_modified_batch_arr,
        "mustBePartialModifiedStr": must_be_partial_modified_str,
        "mustBePartialModifiedRemainedPattern": must_be_partial_modified_remained_pattern
    }

    return res


def main(args):
    return cloud_function(args)