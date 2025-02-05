from name_function import get_formatted_name


def text_first_name_last_name():
    """Do names like "Janis Joplin" work?"""
    
    formatted_name = get_formatted_name("Janis","Joplin")
    assert formatted_name == "janis Joplin"
