from Functionality_Incar_2 import *
from Libraries import math
from Test_Case import test_case_incar_2

class error_cal_incar_2:

    actual_value = [1.192054493, 2.384108986, 3.576163480, 4.768217973, 5.960272466]
    absolute_err = []
    relative_err = []
    def error_cal(self):
        test_case_incar_2.tc2_obj.impl_incr_2()
        for i in range(0, 5):
            func_def_obj_i_2.round_out = True
            self.absolute_err.append(func_def_obj_i_2.round_off_val(
                self.actual_value[i] - test_case_incar_2.tc2_obj.length_data[i]))
        # Relative error calculation
            func_def_obj_i_2.round_out = True
            self.relative_err.append(func_def_obj_i_2.round_off_val(
                self.absolute_err[i] / self.actual_value[i]))

        for j in range(0, 5):
            print("Radius: ", "Computed Length", "\t", "Expected Length", "\t", "Absolute error: ", "\t", "Relative error:")
            print(j+1, "\t\t", test_case_incar_2.tc2_obj.length_data[j], "\t\t", self.actual_value[j], "\t\t",
                  self.absolute_err[j], "         \t\t", self.relative_err[j])


error_cal_incar_2_obj = error_cal_incar_2()
error_cal_incar_2_obj.error_cal()