# from answer_questions import answer_question, answer_questions
# response = answer_question("What is wu wei?")
# print(response)
# response = answer_question("Who is Dan Shipper?")
# print(response)
# answer_questions()  # <- use this if you want to chat back and forth with it in the console

from question_answering import QuestionAnswering

qa = QuestionAnswering()
qa.answer_questions()
