import time
from formula_client import formula_client as fc

def check_input():
    print("\n")
    res = input("Y/N: ")
    print("\n")
    if(res.upper() == 'Y'):
        return True
    else:
        return False

def main():
    
    exit = False

    while(not exit):
        formula = fc()
        formula.connect()
        formula.handle_project()

        formula.handle_event()

        res_prop = False
        while(not res_prop):
            formula.handle_property()
            res_prop = check_input()

        print("Please press Y after selection \n")
        formula.handle_object()
        while(formula.res_obj == False):
            time.sleep(1)

        formula.end_handle_object()

        formula.set_properties()

        print("Formula complete! \n")

        res = input("Exit? Y/N: ")
        if(res.upper() == 'Y'):
            exit = True
        else:
            exit = False
    
        formula.disconnect()


if __name__ == "__main__":
    main()