# Question

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self, answer):
        return self.answer == answer         

q1 = Question('En iyi programlama dili hangisidir ? ', ['C# ', 'Python' , 'javascript' , 'java'], 'python')
q2 = Question('En popüler programlama dili hangisidir ? ', ['Python ', 'javascript' , 'C#' , 'java'], 'python')
q3 = Question('En çok kazandıran programlama dili hangisidir ? ', ['C# ', 'java' , 'javascript' , 'Python'], 'python')

list = [q1,q2,q3]

# print(q1.checkAnswer('python'))
# print(q2.checkAnswer('python'))


# Quiz

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionsIndex = 0 

    def getQuestion(self):
        return self.questions[self.questionsIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionsIndex +1 }: {question.text}')        

        for q in question.choices:
            print('-'+q)

        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score +=1
        self.questionsIndex +=1

            
              
    def loadQuestion(self):
        if len(self.questions) == self.questionsIndex:
            self.showScore()  

        else:
            self.displayProgress()
            self.displayQuestion()           

    def showScore(self):
        print('Score: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionsNumber = self.questionsIndex +1

        if questionsNumber > totalQuestion:
            print('Quiz bitti')
        else:
            print(f'Question {questionsNumber} of {totalQuestion}'.center(100,'*'))    

q1 = Question('En iyi programlama dili hangisidir ? ', ['C# ', 'Python' , 'javascript' , 'java'], 'python')
q2 = Question('En popüler programlama dili hangisidir ? ', ['Python ', 'javascript' , 'C#' , 'java'], 'python')
q3 = Question('En çok kazandıran programlama dili hangisidir ? ', ['C# ', 'java' , 'javascript' , 'Python'], 'python')

questions = [q1,q2,q3]  

quiz = Quiz (questions)

quiz.loadQuestion()