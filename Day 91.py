def check_key_exists(dictionary, key):
    """
    Check if a key exists in the dictionary.

    Args:
        dictionary (dict): The dictionary to check.
        key: The key to search for.

    Returns:
        bool: True if the key exists, False otherwise.
    """
    return key in dictionary


my_dict = {"name": "Max", "age": 25, "city": "Germany"}
key_to_check = input("Enter the key to check: ")

if check_key_exists(my_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")