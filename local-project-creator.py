#===== Imports
import os
import shutil

#===== Setting
django_docs_path         = 'django-docs' # The main Django documentation project folder ( 'django-docs' folder name is expected)
project_docs_path_github = 'docs'        # Django Persian documentation project folder ( 'docs' folder name is expected if you've not changed its name)
project_docs_path_local  = 'local-docs'  # A local documentation folder which will be made and includes the latest updates to the 'Django Persian documentation' Project ( 'local-docs' folder name is expected)

#===== Funcs
def find_paths(root_path):

    dirs_dic = {}
    list_of_paths = []

    for root, dirs, files in os.walk(root_path):
        # Level shows the folder's position relative to the root path
        level = root.replace(root_path, '').count(os.sep)

        # The current folder name
        dir_name = os.path.basename(root)

        # Check if the current path is in the root folder or it's root folder
        if level != 0 :
            # If folder information has already created it just adds new information otherwise it creates a new key,value on this level
            try:
                dirs_dic[level] += [[dir_name,dirs]]
            except:
                dirs_dic[level] = [[dir_name,dirs]]

            # Parent path is just for ease of addressing
            parent_path = root_path + '/'
           
            # List of folders's levels which should be check in dirs_dic to complete the path
            # e.g => level is 3 => levels = [2,1] => level of parents
            levels = list(range(1,level))[::-1]
           
            # Check for emptiness and detect it as a level 1 folder
            if levels:
                # Over than level 1

                parent_name = dir_name
                parent_list = [dir_name]

                for level_number in levels:
                
                    # Take parent's level and check which one belongs to it
                    parent_dirs_list = dirs_dic.get(level_number)

                    # Checking to find its own parent
                    for item in parent_dirs_list:
                        if parent_name in item[1]:

                            # Add parent path to parents list
                            parent_name = item[0]
                            parent_list.append(parent_name)

                parent_path += '/'.join(parent_list[::-1])
                
                # Adding final paths to list_of_paths
                for file in files:
                    list_of_paths.append('/'.join([parent_path,file]))
            else:

                # Level is 1
                parent_path += dir_name
                
                # Adding final paths to list_of_paths
                for file in files:
                    the_path = '/'.join([parent_path,file])
                    list_of_paths.append(the_path)
        else:
            # It's root folder
            # Adding pathes to list_of_paths
            for file in files:
                list_of_paths.append('/'.join([root_path,file]))
    
    return list_of_paths

def copying():
    path_list_2 = find_paths(project_docs_path_github)

    path_list_2 = ['/'.join(path.split('/')[1:]) for path in path_list_2 ]

    try:
        os.mkdir(project_docs_path_local)
    except:
        print('Formatting the folder...')
        shutil.rmtree(project_docs_path_local)
        os.mkdir(project_docs_path_local)
    print('Folder is ready...')

    print(f'Copying {django_docs_path} to {project_docs_path_local}')
    shutil.copytree(django_docs_path,project_docs_path_local,dirs_exist_ok=True)

    print('Copying new files ...')

    max_length = len(max(path_list_2, key = len))

    for file_path in path_list_2:
        os.makedirs(os.path.dirname(f'{project_docs_path_local}/{file_path}'), exist_ok=True)
        shutil.copy(f'{project_docs_path_github}/{file_path}',f'{project_docs_path_local}/{file_path}') 
        print(f'{project_docs_path_github}/{file_path:<{max_length}} to {project_docs_path_local}/{file_path} Done!')

#===== Run
def main():
    res = input(f'''Django documentation folder path         : {django_docs_path}
Django Persian documentation folder path : {project_docs_path_github}
Local documentation folder path          : {project_docs_path_local}
---
Make sure that these values ​​match the names of the folders to avoid problems
---
This process will delete the entire "{project_docs_path_local}" folder with all files! are you sure? y/n: ''')

    if res in ['y','Y']:
        copying()
        print('''=====\nTask done!\n=====''')

    else:
        print('=====\nAborted')

if __name__ == '__main__':
    main()