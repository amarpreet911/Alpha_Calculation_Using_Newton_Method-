import Functionality_Incar_1 as func


class UiStartIncar1:

    def main_start(self):
        while True:
            print("1. Calculate degree of overlap between the coasters")
            print("2. exit")
            input_val = input("Enter one of the given options")

            if input_val.isdigit():
                if input_val == func.const_obj.oper_calculate:
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
        while not radius.isdigit():
            self.error_handling(radius)
            radius = input("Enter Radius range[1 to 10]:")
        while (int(radius) < int(func.const_obj.radius_floor)
               or int(radius) > int(func.const_obj.radius_ceil)):
            print("Sorry radius not in range")
            radius = input("Enter Radius range[1 to 10]:")

        precision = input("Enter precision for intermediate value calculation range[1 to 10]:")
        while not precision.isdigit():
            self.error_handling(precision)
            precision = input("Enter intermediate precision range[1 to 10]:")
        while (int(precision) < int(func.const_obj.precision_floor)
               or int(precision) > int(func.const_obj.precision_ceil)):
            print("Sorry intermediate precision not in range")
            precision = input("Enter intermediate precision range[1 to 10]:")

        precision_out = input("Enter Precision value for output range[1 to 10]:")
        while not precision_out.isdigit():
            self.error_handling(precision_out)
            precision_out = input("Enter output precision range[1 to 10]:")
        while (int(precision_out) < int(func.const_obj.precision_output_floor)
               or int(precision_out) > int(func.const_obj.precision_output_ceil)):
            print("Sorry output precision not in range")
            precision_out = input("Enter output precision range[1 to 10]:")
        func.func_def_obj.cheers_cal_inc_1(radius, precision, precision_out)
        print("Now we will calculate length")
        length = func.func_def_obj.cal_length()
        print("The length value calculated in Incarnation-1 is ", length)

    def error_handling(self, input_val):

        if input_val.__str__():
            print("You have entered a string value, kindly put some numeric value")
        else:
            print("You cannot put a blank entry, Kindly help to put sme numeric value")

ui_1_main_obj = UiStartIncar1()
ui_1_main_obj.main_start()


