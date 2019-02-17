from Nov_7_1 import AnonymousSurvey

question='what language did you first learn to  speak?'
my_survey=AnonymousSurvey(question)
my_survey.show_question()
print('enter q to quit')
while True:
    response=input('language:')
    if response=='q':
        break
    my_survey.store_response(response)

print('\nthank you who participated')
my_survey.show_results()