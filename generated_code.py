from typing import Dict

def details_provider(function_name: str) -> Dict[str, str]:
    """
    This function provides details about the capabilities of a person based on their name.

    Args:
    function_name (str): The name of the person.

    Returns:
    Dict[str, str]: A dictionary containing details about the person's capabilities.
    """

    # Define a dictionary to store the details of different people's capabilities
    details: Dict[str, Dict[str, str]] = {
        "Bhai tu kya kya kar sakta hai?": {
            "function_name": "Bhai Tu Kya Kya Kar Sakta Hai?",
            "details": "He can do a variety of things, like cooking, dancing, singing, coding, designing, etc."
        },
        "Thoda details mai batayega kya": {
            "function_name": "Thoda Details Mai Batayega Kya?",
            "details": "He likes to provide a little detail about his capabilities, without revealing too much."
        },
        "Jitna details possible hai": {
            "function_name": "Jitna Details Possible Hai",
            "details": "He likes to provide as much detail as possible about his capabilities, so you can have a better understanding."
        }
    }

    # Check if the function_name exists in the details dictionary
    if function_name in details:
        # If it exists, return the corresponding details
        return details[function_name]
    else:
        # If it doesn't exist, return an error message
        return {"error": f"Sorry, we don't have any details for {function_name}."}


# Example usage
if __name__ == "__main__":
    print(details_provider("Bhai tu kya kya kar sakta hai?"))
    print(details_provider("Thoda details mai batayega kya"))
    print(details_provider("Jitna details possible hai"))
    print(details_provider("Unknown Function Name"))