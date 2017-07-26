import Functionality as func

class ui_start:
    def main_start():
        print("1. Calculate degree of overlap between the coasters")
        print("2. exit")
        input_val = input("Enter one of the given options")
        print("The value entered is ", input_val)

        if input_val == func.const_obj.oper_calculate:
            print("lets start with option 1")
            radius = input("Enter Radius range[1 to 5]:")
            precision = input("Enter precision for intermediate value calculation range[1 to 5]:")
            precision_out = input("Enter Precision value for output range[1 to 5]:")
            print("...........calculating.................")
# calculation
            func.func_def_obj.cheers_cal_inc_1(radius, precision, precision_out)
            print("Now we will calculate length")
            func.func_def_obj.cal_length()
            print("The length calculated is ", func.func_def_obj.cal_length())
        elif input_val == func.const_obj.oper_exit:
            print("User wants to exit the scenario")
        else:
            print("please select either value 1 or 2")
    main_start()


