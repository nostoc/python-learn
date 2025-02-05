from survey import AnonymousSurvey

# Define a question and make a survey
question = "\nWhat language did you first learn to speak? "
language_survey = AnonymousSurvey(question)
#show the question and store the responses
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response.lower() =='q':
        break
    language_survey.store_response(response)
    
# show the survey results
language_survey.show_results()