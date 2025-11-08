from pathlib import Path
from typing import List
from icecream import ic
import inspect
import os

def get_modules(lines:List[str],auto_install_function_name:str)->List[str]:

    out_lis_modules:List[str] = []
    we_inside_user_code=False
    for line in lines:
        if False:
            i+=1
            ic(i,line)
            ic(we_inside_user_code)
        # here we iterate over each line 
        # if there is an module in the current line we append it to the list

        if not we_inside_user_code:
            if line == f"{auto_install_function_name}(True)":
                we_inside_user_code=True
                    
        else: 

            if not "import " in line: 
                continue
            
            if "from " in line and " import" in line:
        
                start_idx:int= line.find("from ") + len("from ")
                end_idx:int= line.find(" import")

                module = line[start_idx:end_idx]
                out_lis_modules.append(module)
                continue

            if "import " in line and " as " in line:

                start_idx:int= line.find("import ") + len("import ")
                end_idx:int= line.find(" as ")

                module = line[start_idx:end_idx]
                out_lis_modules.append(module)
                continue

            if "import " in line:

                start_idx:int= line.find("import ") + len("import ")

                module = line[start_idx:]
                out_lis_modules.append(module)
                continue

            ic("somthing wrong here",line)
            ic(line)
            raise ValueError


    return out_lis_modules


def auto_install(should_we:bool):

    auto_install_function_name = auto_install.__name__

    if not isinstance(should_we,bool):  
        raise ValueError

    if should_we==False:return 

    #we take the file content and place each line in an list
    script = Path(inspect.stack()[1].filename)
    lines:List[str] = script.read_text(encoding="utf-8").splitlines()
    lines = [line.strip() for line in lines]
    
    # here we get the modules 
    lis_modules:List[str] = get_modules(lines,auto_install_function_name)
    if not lis_modules: 
        print('there is no modules')
        return 
    
    green_start = "\033[92m"
    green_end = '\033[0m'

    print('-'*30)
    print()
    print(f"[{green_start}{"pip"}{green_end}] we update ")
    os.system(f"python.exe -m pip install --upgrade pip")
    print()
    for module in lis_modules:
        print('-'*30)
        print()
        print(f"[{green_start}{module}{green_end}]")
        print(f"[{green_start}{module}{green_end}] we install with pip")
        os.system(f"pip install {module}")
        print()
    print('-'*30)
    print()

    