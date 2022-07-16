def cloud_function(json_input):
    original_str = json_input["originalStr"]
    word_per_batch = json_input["wordPerBatch"]
    
    # Processing

    words = original_str.split()
    result = list(" ".join(words[i:i+word_per_batch]) for i in range(0, len(words), word_per_batch))

    # return the result
    res = {
        "batchArr": result
    }
    return res


def main(args):
    return cloud_function(args)