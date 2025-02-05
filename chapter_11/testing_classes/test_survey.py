from survey import AnonymousSurvey

def test_single_response():
    '''Test that a single response is stored properly'''
    question = "\nWhat language did you first learn to speak? "
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("English")
    assert "English" in language_survey.responses
