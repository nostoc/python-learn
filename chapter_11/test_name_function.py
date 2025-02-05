from name_function import get_formatted_name


def test_first_name_last_name():
    """Do names like "Janis Joplin" work?"""

    formatted_name = get_formatted_name("Janis", "Joplin")
    assert formatted_name == "Janis Joplin"


def test_first_name_middle_name_last_name():
    """Do names like Janitha senani karunarathna work?"""
    formatted_name = get_formatted_name("Janitha", "Karunarathna", "Senani")
    assert formatted_name == "Janitha Senani Karunarathna"

