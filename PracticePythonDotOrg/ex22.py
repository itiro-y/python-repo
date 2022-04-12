# Read From File

def main():
    count_super = 0
    count_child = 0
    with open('/PythonStuff/PracticePythonDotOrg/sun_database.txt', 'r') as f:
        lines = f.read() # this returns a full string '.txt content'
        lines_list = lines.split()
        super_cat_list = []
        child_cat_list = []
        for item in lines_list:
            dash_index = item.find('/', 3)
            if item[1] not in super_cat_list:
                super_cat_list.append(item[1])
            if item[3:dash_index] not in child_cat_list:
                child_cat_list.append(item[3:dash_index])    
        count_super = len(super_cat_list) # super category
        count_child = len(child_cat_list) # its child category
    print(f'Number of categories: {count_super}')
    print(f'Number of subcategories: {count_child}')

if __name__ == '__main__':
    main()