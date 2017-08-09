from Functionality_Incar_1 import *
from Test_Case import test_case_incr_1

class error_cal_incar_1:

    actual_value = [1.1920544, 2.3841089, 3.5761634, 4.7682179, 5.9602724]
    absolute_err = []
    relative_err = []
    def absolute_error_cal(self):
        test_case_incr_1.tc1_obj.impl_incar_1()
        for i in range(0, 5):
            self.absolute_err.append(self.actual_value[i] - test_case_incr_1.tc1_obj.length_data[i])
            # print(test_case_incr_1.tc1_obj.data[i])
        for j in range(0, 5):
            print("for radius: ", j+1, "absolute error is ", self.absolute_err[j])

    def relative_error_cal(self):
        for k in range(0, 5):
            self.relative_err.append(self.absolute_err[k] / self.actual_value[k])
            print("calculated relative error for radius ", k+1, " is ", self.relative_err[k])


error_cal_incar_1_obj = error_cal_incar_1()
error_cal_incar_1_obj.absolute_error_cal()
error_cal_incar_1_obj.relative_error_cal()