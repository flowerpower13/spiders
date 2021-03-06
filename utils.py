import os

def readFileLines(name):
        lines = []
        with open(name, encoding="utf-8") as file_in:
            for line in file_in:
                lines.append(line.strip())
        return lines


def writeFile(fname,content):
    try:
        with open(str(fname), 'w', encoding="utf-8") as file_out:
            file_out.write(content)
    except Exception as e:
        print(e)


def readFile(name):
    content = ""
    with open(name, 'r', encoding="utf-8") as file_in:
        content = file_in.read()
    return content


def getFilesList(folder, extension=None):
    all_files = []
    for file in os.listdir(folder):
        if extension==None or file.endswith(extension):
            all_files.append(file)
    return all_files

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


def saveBinFile(file_name,content): 
    f = open(file_name, 'wb')
    f.write(content)
    f.close()
