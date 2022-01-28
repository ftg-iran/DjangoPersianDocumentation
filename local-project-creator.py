#===== Imports
import os
import shutil

#===== Setting
django_docs_path         = 'django docs'  # The main Django documentation project directory ( 'django docs' directory name is expected)
project_docs_path_github = 'docs'  # Django Persian documentation project directory ( 'docs' directory name is expected if you've not changed its name)
project_docs_path_local  = 'local docs'  # A local documentation directory which will be made and includes the latest updates to the 'Django Persian documentation' Project

#===== Funcs
def find_paths(root_path):

    dirs_dic = {}
    list_of_paths = []

    for root, dirs, files in os.walk(root_path):
        # level shows the folder's position relative to the root path
        level = root.replace(root_path, '').count(os.sep)

        # the current directory name
        dir_name = os.path.basename(root)

        # checks if current path is in the root directory
        if level != 0 :
            # if directory information has already created it just adds new information otherwise it creates a new key,value on this level
            try:
                dirs_dic[level] += [[dir_name,dirs]]
            except:
                dirs_dic[level] = [[dir_name,dirs]]

            # parent path is just for ease of addressing and add internal directories
            parent_path = root_path + '/'
           
            # list of directories's levels which should be check in dirs_dic to complete the path
            levels = list(range(1,level))[::-1]
           
            # checks for emptiness and detects it as a level 1 directory
            if levels:
                # over than level 1

                parent_name = dir_name
                parent_list = [dir_name]

                for level_number in levels:
                
                    # get's parent's level and checks which one belongs to it
                    parent_dirs_list = dirs_dic.get(level_number)

                    # checking to find its own parent
                    for item in parent_dirs_list:
                        if parent_name in item[1]:
                            # add parent path to parents list
                            parent_name = item[0]
                            parent_list.append(parent_name)

                parent_path += '/'.join(parent_list[::-1])
                # adding final paths to list_of_paths
                for file in files:
                    list_of_paths.append('/'.join([parent_path,file]))
            else:

                # level is 1
                parent_path += dir_name
                # adding final paths to list_of_paths
                for file in files:
                    the_path = '/'.join([parent_path,file])
                    list_of_paths.append(the_path)
        else:
            # It's root directory

            # adding final paths to list_of_paths
            for file in files:
                list_of_paths.append('/'.join([root_path,file]))
    
    return list_of_paths

def copying():
    path_list_1 = find_paths(django_docs_path)
    path_list_2 = find_paths(project_docs_path_github)

    path_list_1 = ['/'.join(path.split('/')[1:]) for path in path_list_1 ]
    path_list_2 = ['/'.join(path.split('/')[1:]) for path in path_list_2 ]

    try:
        os.mkdir(project_docs_path_local)
    except:
        shutil.rmtree(project_docs_path_local)
        os.mkdir(project_docs_path_local)
    print('Directory is ready...')

    shutil.copytree(django_docs_path,project_docs_path_local,dirs_exist_ok=True)

    for file_path in path_list_2:
        os.makedirs(os.path.dirname(f'{project_docs_path_local}/{file_path}'), exist_ok=True)
        shutil.copy(f'{project_docs_path_github}/{file_path}',f'{project_docs_path_local}/{file_path}')
        print(f'{project_docs_path_github}/{file_path} to {project_docs_path_local}/{file_path} ☑️')


#===== Run
def main():
    print(f'Django documentation directory path : {django_docs_path}')
    print(f'Django Persian documentation directory path : {project_docs_path_github}')
    print(f'Local documentation directory path : {project_docs_path_local}')
    print('---')
    print('Make sure that these values ​​match the names of the directories to avoid problems')
    print('---')
    res = input(f'This process will delete the entire "{project_docs_path_local}" folder wirh all files! are you sure? y/n :')
    print('---')
    if res in ['y','Y']:
        copying()
        print('=====')
        print('Task Done')
        print('=====')

    else:
        print('Aborted')

if __name__ == '__main__':
    main()