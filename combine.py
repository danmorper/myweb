def combine_dicts(dict1, dict2):
    combined_dict = dict1.copy()  # Create a copy of the first dictionary to preserve the original
    combined_dict.update(dict2)   # Update it with the second dictionary
    return combined_dict
