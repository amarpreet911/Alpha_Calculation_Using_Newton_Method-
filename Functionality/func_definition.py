from Functionality.constants import const
class func_def:
    def cheers_cal_inc_1(radius, precision, precision_out):
    # check radius range
        if (radius < const.radius_floor || radius >const.radius_ceil):
            print("Kindly help to enter radius value in range [1 to 5]")
        