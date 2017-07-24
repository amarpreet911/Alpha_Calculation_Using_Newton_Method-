from Functionality.constants import const_obj


class func_def:
    precision_pi = const_obj.pi_precision_val
    def cheers_cal_inc_1(radius, precision, precision_out):
        # check range for input values
        if (radius < const_obj.radius_floor) or (radius >const_obj.radius_ceil):
            print("Kindly help to enter radius value in range [1 to 5]")
        if (precision < const_obj.precision_floor) or (precision >const_obj.precision_ceil):
            print("Kindly help to enter precision value in range [1 to 5]")
        if (precision_out < const_obj.precision_output_floor) or (precision_out > const_obj.precision_output_ceil):
            print("Kindly help to enter the output precision value in range [1 to 5]")
            # ck if needed to assign the val to self

    def cal_pi(self):
        # precision_pi = const_obj.pi_precision_val
        pi_val = 0
        sign = -1
        n = 1
        # while n <= self.precision_pi:
        while n <= 4:
                sign = -1 * self.sign
                pi_val = pi_val + (sign/n)
                n = n+2
        return self.round_intermediate_val(4 * self.pi_val)

    def round_intermediate_val(self,pi_arg):
        prec = 1
        for i in (1, self.precision_pi+1):
            prec = prec*10
        pi_arg = pi_arg * prec
        int(pi_arg)
        pi_arg = pi_arg/prec
        return pi_arg

func_def_obj = func_def()
