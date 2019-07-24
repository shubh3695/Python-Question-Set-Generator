from question_generator import Generator

'''
@Author : ssaxena36
This is the generator code
This piece of code calls back for all Generator Methods and displays result directly
'''
try:
    results = Generator().analyse_results()
    for result in results:
        print('\n'.join(result[0]))
except Exception as e:
    print(e)
