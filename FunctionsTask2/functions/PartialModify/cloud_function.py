import re

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

def cloud_function(json_input):
    must_be_partial_modified_str = json_input["mustBePartialModifiedStr"]
    must_be_partial_modified_remained_pattern = json_input["mustBePartialModifiedRemainedPattern"]
    pattern = json_input["pattern"]
    
    # Processing
    must_be_partial_modified_str = rreplace(must_be_partial_modified_str, pattern, '',  must_be_partial_modified_remained_pattern)
    must_be_partial_modified_str = re.sub(' +', ' ', must_be_partial_modified_str).strip()
    # return the result
    res = {
        "partialyModifiedStr": must_be_partial_modified_str
    }
    
    return res


def main(args):
    return cloud_function(args)