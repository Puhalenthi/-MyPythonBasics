def FileReader(filename):
    try:
        with open(filename, 'r') as f:
            words = 0
            sentences = 0
            for counter in f.read():
                if counter == '.':
                    sentences += 1
                elif counter == ' ':
                    words += 1
            words += 1
        print('The number of words is {}. The number of sentences is {}'.format(words,sentences))
    except FileNotFoundError:
        print('OOPS! The File could not be found')
    except Exception as error:
        print('OOPS! An error occured: {}'.format(error))
    finally:
        print('Function is over')


FileReader(r'C:\Python\PythonExceptionHandling.txt')