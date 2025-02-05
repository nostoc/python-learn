from survey import AnonymousSurvey


def test_single_response():
    """Test that a single response is stored properly"""
    question = "\nWhat language did you first learn to speak? "
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("English")
    assert "English" in language_survey.responses


def test_three_responses():
    """Test that three individual responses are stored properly"""
    question = "\nWhat language did you first learn to speak? "
    language_survey = AnonymousSurvey(question)
    responses = ["Sinhala","English","tamil"]
    for response in responses:
        language_survey.store_response(response)
    
    for response in responses:
        assert response in language_survey.responses
