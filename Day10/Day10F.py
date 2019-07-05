def printEmpskill(name,*skillset):
    print('{0} is skilled in {1} language '.format(name,skillset))
    print('{0} is skilled in {1} language '.format(name,len(skillset)))
    return None
printEmpskill('Alex','Python','html')
printEmpskill('Pravesh','Java','C','C++')
printEmpskill('Ajay')
