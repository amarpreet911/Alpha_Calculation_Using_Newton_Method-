from Functionality_Incar_1 import *

# Created on 2017/07/28 for Incarnation 1
#
# @author Amarpreet Singh and Anish Talwar
# The static values taken in the below test cases for comparison have been computed from https://www.wolframalpha.com/

# In test cases involving alpha and length I have showed in the output that how residue f(x) turns zero after certain
# iterations and thus f'(x) also stops changing helping us to converge Newton's method for our calculations.

class test_case_incar_1:

    # intermediate calculation precision is the precision for intermediate calculations
    # while the output_calculation_precision is for the final output_precision

    intermediate_calculation_precision = 10
    output_calculation_precision = 8
    length_data = []
    def impl_incar_1(self):

        #The loop will calculate the corresponding length for radius 1 to 7
        for radius in range(1, 6):
            func_def_obj.cheers_cal_inc_1(radius, self.intermediate_calculation_precision, self.output_calculation_precision)
            length = func_def_obj.cal_length()
            self.length_data.append(length)
            print("The value of length for radius: ", float(radius),  "is: ", length, "\n")
            print("**************************************************************")
        print("The value of alpha is : ", func_def_obj.cal_alpha(), "\n\n")

        # The static values taken for comparison have been computed from https://www.wolframalpha.com/
        # Testing individual values
        print("Calculating individual cases::::::::::::::::::::::::::::::::\n")

        calculated_pi = func_def_obj.cal_pi()
        func_def_obj.round_intermediate = True
        compute_pi = (calculated_pi - 3.14159265358979323846)
        # value < 1.0e-5 means value tends to be zero
        if (compute_pi < 1.0e-5):
            print("Test case for pi is PASSED with value::::::::: ", calculated_pi, "\n")
        else:
            print("Sorry the test case for pi has FAILED")

        calculated_cos = func_def_obj.cal_cos(func_def_obj.degree_to_radian(45))
        func_def_obj.round_intermediate = True
        compute_cos = func_def_obj.round_off_val(calculated_cos - 0.7071067811865476)
        # value < 1.0e-5 means value tends to be zero
        if (compute_cos < 1.0e-5):
            print("Test case for cos(x) is PASSED with value:::::::::: ", calculated_cos, "\n")
        else:
            print("Sorry the test case for cos(x) has FAILED")
        calculated_sin = func_def_obj.cal_sin(func_def_obj.degree_to_radian(45))
        func_def_obj.round_intermediate = True
        compute_sin = func_def_obj.round_off_val(calculated_sin - 0.7071067811865475)
        # value < 1.0e-5 means value tends to be zero
        if (compute_sin < 1.0e-5):
            print("Test case for sin(x) is PASSED with value:::::::::::::", calculated_sin, "\n")
        else:
            print("Sorry the test case for sin(x) has FAILED\n")
# Alpha will be taken out for a value of which residue tends to be zero(shown in the output)
        # i.e f(x)-->0 and f'(x) doesn't change any more(Newtons Method: x(n+1) = x(n) - f(x)/f'(x))
        calculated_alpha = func_def_obj.cal_alpha()
        func_def_obj.round_intermediate = True
        compute_alpha = func_def_obj.round_off_val(calculated_alpha - 2.3098814600100572609)
        # value < 1.0e-5 means value tends to be zero
        if (compute_alpha < 1.0e-5):
            print("Test case for alpha is PASSED with value::::::::::: ", calculated_alpha, "\n")
        else:
            print("Sorry the test case for alpha has FAILED\n")

# Length test case:: radius = 7 as radius last computed in the for loop is 7
# for changing Radius just change the "for in range(1, (radius-1))" to change radius for the below computation
# For example range(1, 8) will compute radius till seven and making instance value at this point as 7
        calculated_length = func_def_obj.cal_length()
        func_def_obj.round_intermediate = True
        compute_length = func_def_obj.round_off_val(calculated_length - 8.3443431928404250)
        if (compute_length < 1.0e-5):
           print("Test case for length is PASSED with value::::::::::::: ", calculated_length, "\n")
        else:
           print("Sorry the test case for length has FAILED")
        return calculated_length

tc1_obj = test_case_incar_1()
tc1_obj.impl_incar_1()
