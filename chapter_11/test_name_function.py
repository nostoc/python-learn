from name_function import get_formatted_name


def test_first_name_last_name():
    """Do names like "Janis Joplin" work?"""
    
    formatted_name = get_formatted_name("Janis","Joplin")
    assert formatted_name == "Janis Joplin"
