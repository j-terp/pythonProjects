def questionify(sentence):
    question = str(sentence) + "?"
    return question
user_sentence = input("Write a sentence: ")
print(questionify(user_sentence))