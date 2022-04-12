# File Overlap
# two lists of 1000 items

def main():
    primenumbers_list = []
    happynumbers_list = []

    with open('/PythonStuff/PracticePythonDotOrg/primenumbers.txt', 'r') as f:
        primenumbers_list = f.read()
        primenumbers_list = primenumbers_list.split()

    with open('/PythonStuff/PracticePythonDotOrg/happynumbers.txt', 'r') as f:
        happynumbers_list = f.read()
        happynumbers_list = happynumbers_list.split()

    overlap_count = [x for x in primenumbers_list for y in happynumbers_list if x == y]
    
    print(f'The items that overlap are: {overlap_count}')
    


if __name__ == '__main__':
    main()