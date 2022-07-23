class CollegeSubject:
    def __init__(self, name):
        self.subjectName = name
        self.testScore = []

    def addSubjectScore(self, score):
        self.testScore.append(score)

class Student:
    def __init__(self, name = None, num = None):
        self.studentName = name
        self.registration = num
        self.studentSubjects = []

    def createStudent(self, name, num):
        self.studentName = name
        self.registration = num

    def createStudentSubjects(self, subject):
        self.studentSubjects.append(subject)

    def registerStudent(self):
        counter = 0
        key = False

        print('\n| REGISTRAR ESTUDANTE NO SISTEMA |')
        name = input ('Informe o nome do estudante: ')
        registration = int (input('Informe a matrícula do estudante: '))
        student = Student(name, registration)
        stop = input (f'\nDeseja cadastrar alguma disciplina para {name}? (Responda Sim ou Não) ')

        stop = stop.upper()
        if stop == 'SIM':
            key = True
        else:
            print('\n< Estudante cadastrado sem nenhuma disciplina! >\n')

        while key:
            print('\n| INFORME |')
            subjectName = input ('Nome da disciplina: ')
            score1 = int (input('Nota do aluno da primeira unidade (Digite -1 caso o aluno não tenha nota): '))
            score2 = int (input('Nota do aluno da segunda unidade (Digite -1 caso o aluno não tenha nota): '))
            subject = CollegeSubject(subjectName)
            subject.addSubjectScore(score1)
            subject.addSubjectScore(score2)
            student.createStudentSubjects(subject)
            counter += 1
            stop = input (f'\nDeseja continuar cadastrando disciplinas para {name}? (Responda Sim ou Não): ')
            stop = stop.upper()
            if stop == 'SIM':
                key = True
            else:
                key = False
                print(f'\n < Estudante cadastrado com {counter} disciplina! >\n')

        return student

    def printStudent(self):
            print('\n\n< FICHA ALUNO >')
            print(f'Nome: {self.studentName}, Matrícula: {self.registration}')
            if len(self.studentSubjects):
                for i in range(len(self.studentSubjects)):
                    print(f'- Disciplina {i+1}: {self.studentSubjects[i].subjectName}')
                    for j in range (2):
                        if self.studentSubjects[i].testScore[j] >= 0:
                            print(f'| Nota {j+1}: {self.studentSubjects[i].testScore[j]} |')
                        else:
                            print(f'| Nota {j+1}: Sem nota |')
            else:
                print('Sem disciplinas cadastradas!')
            print('\n\n')

class TreeSystem(Student):
    def __init__(self, student = None):
        self.data = student
        self.left = None
        self.right = None
            
    def addStudent(self, student, registration):
        if not self.data:
            self.data = student
        else:
            if registration < self.data.registration:
                if self.left:
                    self.left.addStudent(student, registration)
                else:
                    self.left = TreeSystem(student)
            elif registration > self.data.registration:
                if self.right:
                    self.right.addStudent(student, registration)
                else:
                    self.right = TreeSystem(student)

    def printOut(self):
        if self.data:
            print('\n\n< FICHA ALUNO >')
            print(f'Nome: {self.data.studentName}, Matrícula: {self.data.registration}')
            if len(self.data.studentSubjects):
                for i in range(len(self.data.studentSubjects)):
                    print(f'- Disciplina {i+1}: {self.data.studentSubjects[i].subjectName}')
                    for j in range (2):
                        if self.data.studentSubjects[i].testScore[j] >= 0:
                            print(f'| Nota {j+1}: {self.data.studentSubjects[i].testScore[j]} |')
                        else:
                            print(f'| Nota {j+1}: Sem nota |')
            else:
                print('Sem disciplinas cadastradas!')
            print('\n\n')
        if self.left:
            self.left.printOut()
        if self.right:
            self.right.printOut()
    
    def addSubject(self, subjectName, score1, score2, numRegistration):
        subject = None
        if self.data.registration == numRegistration:
            subject = CollegeSubject(subjectName)
            subject.addSubjectScore(score1)
            subject.addSubjectScore(score2)
            self.data.createStudentSubjects(subject)
        if self.left:
            self.left.addSubject(subjectName, score1, score2, numRegistration)
        if self.right:
            self.right.addSubject(subjectName, score1, score2, numRegistration)

    def averageScore(self, numRegistration, subjectName, average):
        if self.data.registration == numRegistration:
            for i in range(len(self.data.studentSubjects)):
                if self.data.studentSubjects[i].subjectName == subjectName:
                    for j in range (2):
                        if self.data.studentSubjects[i].testScore[j] >= 0:
                            average += self.data.studentSubjects[i].testScore[j]
                        else:
                            average = -100
            if average >= 0:
                print(f'\n\n< A média do aluno na disciplina é {average/2}! >\n\n')
            else:
                print('\n\n< O estudante não possui média na disciplina informada! >\n\n')
        if self.left:
            self.left.averageScore(numRegistration, subjectName, average)
        if self.right:
            self.right.averageScore(numRegistration, subjectName, average)

    def removeSubject(self, numRegistration, subjectName, i, j):
        if self.data.registration == numRegistration:
            i = len(self.data.studentSubjects)
            while i != 0:
                if self.data.studentSubjects[j].subjectName == subjectName:
                    self.data.studentSubjects.pop(j)
                    print('\n\n< Disciplina removida com sucesso! >\n\n')
                    j += -1
                i -= 1
                j += 1
        if self.left:
            self.left.removeSubject(numRegistration, subjectName, i, j)
        if self.right:
            self.right.removeSubject(numRegistration, subjectName, i, j)

    def removeScore(self, numRegistration, subjectName, score):
        if self.data.registration == numRegistration:
            for i in range(len(self.data.studentSubjects)):
                if self.data.studentSubjects[i].subjectName == subjectName:
                    for j in range (2):
                        if j == score-1:
                            self.data.studentSubjects[i].testScore[j] = -1
                            print('\n\n< Nota removida com sucesso! >\n\n')
        if self.left:
            self.left.removeScore(numRegistration, subjectName, score)
        if self.right:
            self.right.removeScore(numRegistration, subjectName, score)

    def changeSubject(self, option, registrationNum, subjectName, newSubject, score1, score2):
        if option == 1:
            if self.data.registration == registrationNum:
                for i in range(len(self.data.studentSubjects)):
                    if self.data.studentSubjects[i].subjectName == subjectName:
                        self.data.studentSubjects[i].subjectName = newSubject
                print('\n\n< Nome da disciplina atualizada com sucesso! >\n\n')
            if self.left:
                self.left.changeSubject(option, registrationNum, subjectName, newSubject, score1, score2)
            if self.right:
                self.right.changeSubject(option, registrationNum, subjectName, newSubject, score1, score2)
        elif option == 2:
            if self.data.registration == registrationNum:
                for i in range(len(self.data.studentSubjects)):
                    if self.data.studentSubjects[i].subjectName == subjectName:
                        for j in range (2):
                            if j == 0:
                                self.data.studentSubjects[i].testScore[j] = score1
                            else:
                                self.data.studentSubjects[i].testScore[j] = score2
                print('\n\n< Nota da disciplina atualizada com sucesso! >\n\n')
            if self.left:
                self.left.changeSubject(option, registrationNum, subjectName, newSubject, score1, score2)
            if self.right:
                self.right.changeSubject(option, registrationNum, subjectName, newSubject, score1, score2)
        elif option == 3:
            if self.data.registration == registrationNum:
                for i in range(len(self.data.studentSubjects)):
                    if self.data.studentSubjects[i].subjectName == subjectName:
                        self.data.studentSubjects[i].subjectName = newSubject
                        for j in range (2):
                            if j == 0:
                                self.data.studentSubjects[i].testScore[j] = score1
                            else:
                                self.data.studentSubjects[i].testScore[j] = score2
                print('\n\n< Nota e nome da disciplina atualizada com sucesso! >\n\n')
            if self.left:
                self.left.changeSubject(option, registrationNum, subjectName, newSubject, score1, score2)
            if self.right:
                self.right.changeSubject(option, registrationNum, subjectName, newSubject, score1, score2)

    def consultStudent(self, registrationNum):
        if self.data.registration == registrationNum:
            self.data.printStudent()
        if self.left:
            self.left.consultStudent(registrationNum)
        if self.right:
            self.right.consultStudent(registrationNum)

    def approvedStudents(self, average, subject):
        if self.data:
            if len(self.data.studentSubjects):
                for i in range(len(self.data.studentSubjects)):
                    average = 0
                    if self.data.studentSubjects[i].subjectName == subject:
                        for j in range (2):
                            if self.data.studentSubjects[i].testScore[j] >= 0:
                                average += self.data.studentSubjects[i].testScore[j]
                            else:
                                average = -100
                        average = average / 2
                        if average >= 7:
                            print(f'< Aluno {self.data.studentName} aprovado com média {average}! >')
        if self.left:
            self.left.approvedStudents(average, subject)
        if self.right:
            self.right.approvedStudents(average, subject)

    def failedStudents(self, average, subject):
        if self.data:
            if len(self.data.studentSubjects):
                for i in range(len(self.data.studentSubjects)):
                    average = 0
                    if self.data.studentSubjects[i].subjectName == subject:
                        for j in range (2):
                            if self.data.studentSubjects[i].testScore[j] >= 0:
                                average += self.data.studentSubjects[i].testScore[j]
                            else:
                                average = -100
                        average = average / 2
                        if average >= 0 and average < 7:
                            print(f'< Aluno {self.data.studentName} reprovado com média {average}! >')
        if self.left:
            self.left.failedStudents(average, subject)
        if self.right:
            self.right.failedStudents(average, subject)

    def saveTree(self, vector, registrationNum):
        if self.data.registration != registrationNum:
            vector.append(self.data)
        if self.left:
            self.left.saveTree(vector, registrationNum)
        if self.right:
            self.right.saveTree(vector, registrationNum)

    def eraseTree(self):
        if self.data:
            if self.left:
                self.left.eraseTree()
            if self.right:
                self.right.eraseTree()
            del self.data
            del self

    def newTree(self, vector):
        for i in range(len(vector)):
            self.addStudent(vector[i], vector[i].registration)

    def studentList(self, vector):
        if self.data:
            vector.append(self.data.studentName)
        if self.left:
            self.left.studentList(vector)
        if self.right:
            self.right.studentList(vector)

def menu1(self):
    studentObject = Student()
    studentObject = studentObject.registerStudent()
    aux = studentObject.registration
    self.addStudent(studentObject, aux)

def menu2(self):
    self.printOut()

def menu3(self):
    registration = int (input('\n\nMatrícula do aluno que deseja fazer a inserção: '))
    subject = input('\n\nNome da disciplina que deseja adicionar: ')
    score1 = int (input('Nota 1 (Insira -1 caso o aluno não tenha essa nota): '))
    score2 = int (input('Nota 2 (Insira -1 caso o aluno não tenha essa nota): '))
    self.addSubject(subject, score1, score2, registration)
    print('\n\n')

def menu4(self):
    average = 0
    registration = int (input('\n\nMatrícula do aluno: '))
    subject = input ('Nome da disciplina que deseja calcular a média (informe igual está no sistema): ')
    self.averageScore(registration, subject, average)

def menu5(self):
    i = 0
    j = 0
    registration = int (input('\n\nInforme a matrícula do aluno: '))
    subject = input('Nome da disciplina que deseja remover (informe igual está no sistema): ')
    self.removeSubject(registration, subject, i, j)

def menu6(self):
    registration = int (input('\n\nMatrícula do aluno: '))
    subject = input ('Nome da disciplina que deseja remover a nota (informe igual está no sistema): ')
    score = int (input('Informe a nota de qual unidade deseja remover (1 ou 2): '))
    self.removeScore(registration, subject, score)

def menu7(self):
    newSubject = 'None'
    print('\n\n1 - Atualizar nome da disciplina;')
    print('2 - Atualizar nota da disciplina;')
    print('3 - Atualizar nota e nome da disciplina.\n')
    option = int (input('\nInforme o que deseja fazer: '))
    registration = int (input('\n\nMatrícula do aluno: '))
    newScore1 = 0
    newScore2 = 0
    subject = input('Nome da disciplina que deseja atualizar (informe igual está no sistema): ')
    if option == 1:
        newSubject = input ('\n\nInforme o novo nome da disciplina: ')
        self.changeSubject(option, registration, subject, newSubject, newScore1, newScore2)
    elif option == 2:
        newScore1 = int (input('\n\nInforme a nova nota da primeira unidade: '))
        newScore2 = int (input('Informe a nova nota da segunda unidade: '))
        self.changeSubject(option, registration, subject, newSubject, newScore1, newScore2)
    elif option == 3:
        newSubject = input ('\n\nInforme o novo nome da disciplina: ')
        newScore1 = int (input('Informe a nova nota da primeira unidade: '))
        newScore2 = int (input('Informe a nova nota da segunda unidade: '))     
        self.changeSubject(option, registration, subject, newSubject, newScore1, newScore2)

def menu8(self):
    registration = int (input('Matrícula do estudante que deseja consultar: '))
    self.consultStudent(registration)

def menu9(self):
    average = 0
    subject = input ('\n\nNome da disciplina que deseja consultar os aprovados (informe igual está no sistema): ')
    print('\n')
    self.approvedStudents(average, subject)
    print('\n\n')

def menu10(self):
    average = 0
    subject = input ('\n\nNome da disciplina que deseja consultar os reprovados (informe igual está no sistema): ')
    print('\n')
    self.failedStudents(average, subject)
    print('\n\n')

def menu11(self):
    vector = []
    registration = int (input('\n\nMatrícula do estudante que deseja excluir do sistema: '))
    self.saveTree(vector, registration)
    self.eraseTree()
    self = TreeSystem()
    self.newTree(vector)
    print('\n\n <Estudante removido do sistema! >\n\n')
    return self

def menu12(self):
    vector = []
    self.studentList(vector)
    vector.sort()
    print('\n\n| Alunos cadastrados em ordem alfabética |')
    for i in range(len(vector)):
        print(f'< {vector[i]} >')
    print('\n\n')

treeStudent = TreeSystem()
loadProgram = True
text = ('-')*15

print('\n| SISTEMA DE ALUNOS E NOTAS |\n')
while loadProgram:
    print(f'{text} MENU {text}')
    print('[0] - Encerrar programa;')
    print('[1] - Cadastrar aluno;')
    print('[2] - Imprimir ficha dos alunos cadastrados;')
    print('[3] - Adicionar disciplina;')
    print('[4] - Calcular média de disciplina;')
    print('[5] - Remover disciplina;')
    print('[6] - Remover nota;')
    print('[7] - Atualizar disciplina;')
    print('[8] - Consultar ficha do aluno;')
    print('[9] - Alunos aprovados;')
    print('[10] - Alunos reprovados;')
    print('[11] - Remover aluno;')
    print('[12] - Listar alunos cadastrados.')
    print(f'{text}------{text}')
    control = int (input('\nInforme o que deseja fazer: '))
    if control == 0:
        print('\n\nFechando programa...')
        loadProgram = False
    elif control == 1:
        menu1(treeStudent)
    elif control == 2:
        menu2(treeStudent)
    elif control == 3:
        menu3(treeStudent)
    elif control == 4:
        menu4(treeStudent)
    elif control == 5:
        menu5(treeStudent)
    elif control == 6:
        menu6(treeStudent)
    elif control == 7:
        menu7(treeStudent)
    elif control == 8:
        menu8(treeStudent)
    elif control == 9:
        menu9(treeStudent)
    elif control == 10:
        menu10(treeStudent)
    elif control == 11:
        treeStudent = menu11(treeStudent)
    elif control == 12:
        menu12(treeStudent)
    else:
        print('\n\nComando não reconhecido. Tente novamente!\n\n')
print('Sistema encerrado!\n')