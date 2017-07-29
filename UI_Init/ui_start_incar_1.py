import Functionality_Incar_1 as func


class ui_start_incar_1:

    def main_start(self):
        while True:
             print("1. Calculate degree of overlap between the coasters")
             print("2. exit")
             input_val = input("Enter one of the given options")

             if input_val.isdigit():
                if input_val == func.const_obj.oper_calculate or input_val == 2:
                    self.radius_precision_handling()

                elif input_val == func.const_obj.oper_exit:
                    print("Thank you for using the software, BYE-BYE")
                    quit()
                else:
                     print("please select either value 1 or 2")

             else:
                self.error_handling(input_val)

    def radius_precision_handling(self):
        radius = input("Enter Radius range[1 to 10]:")
        precision = input("Enter precision for intermediate value calculation range[1 to 10]:")
        precision_out = input("Enter Precision value for output range[1 to 10]:")
        if radius.isdigit() & precision.isdigit() & precision_out.isdigit():
            if not(radius < func.const_obj.radius_floor) or not(radius > func.const_obj.radius_ceil):
                if not(precision < func.const_obj.precision_floor) or not(precision > func.const_obj.precision_ceil):
                    if not(precision_out < func.const_obj.precision_floor) or not(precision_out > func.const_obj.precision_ceil):
                        func.func_def_obj.cheers_cal_inc_1(radius, precision, precision_out)
                        print("Now we will calculate length")
                        length = func.func_def_obj.cal_length()
                        print("The length value calculated in Incarnation-1 is ", length)
                    else:
                        print("Kindly help to enter precision output value in range [1 to 10]")
                        self.radius_precision_handling()
                else:
                    print("Kindly help to enter precision value in range [1 to 10]")
                    self.radius_precision_handling()
            else:
                print("Kindly help to enter radius value in range [1 to 10]")
                self.radius_precision_handling()
        else:
            self.error_handling()
            self.radius_precision_handling()

    def error_handling(self, input_val):

        if input_val.__str__():
            print("You have entered a string value, kindly put some numeric value")
        else:
            print("You cannot put a blank entry, Kindly help to put sme numeric value")

ui_1_main_obj = ui_start_incar_1()
ui_1_main_obj.main_start()


