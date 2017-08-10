from Functionality_Incar_1 import *
from Test_Case import TestCaseIncar1


class ErrorCalIncar1:

    actual_value = [1.19205449, 2.38410898, 3.57616348, 4.76821797, 5.96027246]
    absolute_err = []
    relative_err = []

    def error_cal(self):
        TestCaseIncar1.tc1_obj.impl_incar_1()
        for i in range(0, 5):
            func_def_obj.round_out = True
            self.absolute_err.append(func_def_obj.round_off_val(
                self.actual_value[i] - TestCaseIncar1.tc1_obj.length_data[i]))

            func_def_obj.round_out = True
            self.relative_err.append(func_def_obj.round_off_val(
                self.absolute_err[i] / self.actual_value[i]))

        for j in range(0, 5):
            print("Radius: ", "Computed Length", "\t", "Expected Length", "\t", "Absolute error: ", "\t", "Relative error:")
            print(j + 1, "\t\t", TestCaseIncar1.tc1_obj.length_data[j], "\t\t", self.actual_value[j], "\t\t",
                  self.absolute_err[j], "          ", self.relative_err[j])


error_cal_incar_1_obj = ErrorCalIncar1()
error_cal_incar_1_obj.error_cal()