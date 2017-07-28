import Functionality_Incar_2 as func_i_2


class ui_start_incar_2:

    def main_start():
        print("1. Calculate degree of overlap between the coasters")
        print("2. exit")
        input_val = input("Enter one of the given options")
        print("The value entered is ", input_val)

        if input_val == func_i_2.const_incar_2_obj.oper_calculate:
            radius = input("Enter Radius range[1 to 5]:")
            precision = input("Enter precision for intermediate value calculation range[1 to 5]:")
            precision_out = input("Enter Precision value for output range[1 to 5]:")
            print("...........calculating.................")
            # Calling the required functionality
            func_i_2.func_def_obj_i_2.cheers_cal_inc_2(radius, precision, precision_out)
            print("Now we will calculate length")
            length = func_i_2.func_def_obj_i_2.cal_length()
            print("The length val calculated is ", length)
            #  print("calculate pi ", func.func_def_obj.cal_pi())
        elif input_val == func_i_2.const_incar_2_obj.oper_exit:
            print("User wants to exit the scenario")
        else:
            print("please select either value 1 or 2")
    main_start()


