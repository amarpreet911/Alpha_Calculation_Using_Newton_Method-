from Functionality_Incar_1.constants_incar_1 import const_obj
import Libraries as lb

class func_def:
    precision_pi = const_obj.pi_precision_val
    round_intermediate = False
    round_out = False

    # def __init__(self):
    #     self.pi = self.cal_pi()

# This funtion to checks whether the input values provided exist within the range or not
    def cheers_cal_inc_1(self, radius, precision, precision_out):
        self.radius = radius
        self.precision_input = precision
        self.precision_out = precision_out
        # if (self.radius < const_obj.radius_floor) or (self.radius > const_obj.radius_ceil):
        #     print("Kindly help to enter radius value in range [1 to 10]")
        # if (self.precision_input < const_obj.precision_floor) or (self.precision_input > const_obj.precision_ceil):
        #     print("Kindly help to enter precision value in range [1 to 10]")
        # if (self.precision_out < const_obj.precision_output_floor) or \
        #         (self.precision_out > const_obj.precision_output_ceil):
        #     print("Kindly help to enter the output precision value in range [1 to 10]")
            # ck if needed to assign the val to self
        self.pi = self.cal_pi()

# For calculating the value of pi
    def cal_pi(self):
        print("calculating pi.......")
        pi_val = 0
        sign = -1
        n = 1
        while n <= self.precision_pi:
            sign = -1 * sign
            pi_val = pi_val + (sign / n)
            n = n + 2
        self.round_intermediate = True
        pi_final_val = self.round_off_val(4 * pi_val)

        # This is where the pdb debugger will start while calculating pi
        # lb.pdb.set_trace()
        print("pi val is ", pi_final_val)
        return pi_final_val

# Alpha calculated with the help of Newton's Method x(n + 1) = x(n) - f(x(n)) / f'(x(n))
    def cal_alpha(self):
        alpha = 1
        print("in cal_alpha")
         # after 32 alpha_iterations the residue value tends to 0 and derivative stops changing
        for i in range(1, const_obj.alpha_iteration):
            residue = alpha - self.cal_sin(alpha) - (self.pi / 2)
            derivative = (1 - self.cal_cos(alpha))
            alpha = alpha - (residue / derivative)
            if residue == 0:
                print("the val of i::::when we got residual as zero is ::::::: ", i)
                break
        print("the val of func is(residual) ", residue)
        print("the val of the (derivative) is  ", derivative)
        self.round_intermediate = True
        alpha_round_off_val = self.round_off_val(alpha)
        print("the val of alpha to go next or x  is ::::::::  ", alpha_round_off_val)
        return alpha_round_off_val  # 2.304129659127962

# This function round off's the value to the describes precision
    def round_off_val(self, pi_arg):
        prec = 1
        if self.round_intermediate:
            for i in range(0, int(self.precision_input)):
                prec = prec * 10
        elif self.round_out:
            for i in range(0, int(self.precision_out)):
                prec = prec * 10
        else:
            print("neither its is for intermediate nor output ")
        int_val = int((pi_arg * prec))
        # print("integer val is", int_val)
        pi_arg = int_val / prec
        # print("pi_arg val is", pi_arg)
        self.round_out = False
        self.round_intermediate = False
        return pi_arg

# This function calculates the required length
    def cal_length(self):
        print("in cal_length")
        # Below mentioned command will allow us to debug at this point
        # lb.pdb.set_trace()
        cos_val = self.cal_cos(self.cal_alpha()/2)
        #print("the calculated cos after alpha, in cal_length is________-fun1 ", cos_val)
        length_val = 2 * float(self.radius) * float(1-cos_val)
        #print("the length is comming ", length_val)
        self.round_out = True
        round_off_length = self.round_off_val(length_val)
        return round_off_length

# cos(x) calculated with the help of Taylor Series
    def cal_cos(self, c_alpha):  # x_alpha is in radian
        # print("entering cal_cos")
        cos_series_sum = 1
        temp_val_cos = 1
        for i in range(1, const_obj.cos_iteration, +2):
            temp_val_cos = temp_val_cos * (-1) * (c_alpha * c_alpha) / (i * (i + 1))
            cos_series_sum = cos_series_sum + temp_val_cos
        # lb.pdb.set_trace()
        self.round_intermediate = True
        cos_ser_numb = self.round_off_val(cos_series_sum)
        # print("cos series numb is ", cos_ser_numb)
        return cos_ser_numb

# sin(x) calculated with the help of Taylor Series
    def cal_sin(self, s_alpha):  # s_alpha is in radian
        # print("entering cal_sin")
        sin_series_sum = s_alpha
        temp_val_sin = s_alpha
        for i in range(2, const_obj.sin_iteration, +2):
            a = temp_val_sin * (-1)
            b = s_alpha * s_alpha
            c = (i * (i + 1))
            temp_val_sin = a * (b / c)  # temp_val_sin*(-1) * (s_alpha * s_alpha)/(i(i+1))
            sin_series_sum = sin_series_sum + temp_val_sin
        # lb.pdb.set_trace()
        self.round_intermediate = True
        sin_ser_numb = self.round_off_val(sin_series_sum)
        # print("cos series numb is ", sin_ser_numb)
        return sin_ser_numb  # nothing round off???cos done in alpha while call

    def degree_to_radian(self, degree):
        self.round_intermediate = True
        return self.round_off_val(degree * (self.pi / const_obj.straight_line_angle))


func_def_obj = func_def()
