from Functionality.constants import const_obj



class func_def:
    precision_pi = const_obj.pi_precision_val
    round_intermediate = False
    round_out = False
    # pi = 3.14

    def __init__(self):
          self.pi = self.cal_pi()


            #     self.radius = radius
    #     self.precision = precision
    #     self.precision_out = precision_out
    def cheers_cal_inc_1(self, radius, precision, precision_out):
        self.radius = radius
        self.precision = precision
        self.precision_out = precision_out
        # pi = self.cal_pi()
        # self.pi = cal_pi()
        # check range for input values
        if (self.radius < const_obj.radius_floor) or (self.radius > const_obj.radius_ceil):
            print("Kindly help to enter radius value in range [1 to 5]")
        if (self.precision < const_obj.precision_floor) or (self.precision > const_obj.precision_ceil):
            print("Kindly help to enter precision value in range [1 to 5]")
        if (self.precision_out < const_obj.precision_output_floor) or \
                (self.precision_out > const_obj.precision_output_ceil):
            print("Kindly help to enter the output precision value in range [1 to 5]")
            # ck if needed to assign the val to self

    def cal_pi(self):
        # precision_pi = const_obj.pi_precision_val
        print("calculating pi.......")
        pi_val = 0
        sign = -1
        n = 1
        while n <= self.precision_pi:
                sign = -1 * sign
                pi_val = pi_val + (sign/n)
                n = n+2 # ck which one to round off ck if this is workinf fine for n+2
        print("val for pi is", pi_val)
        self.round_intermediate = True
        pi_final_val = self.round_off_val(4 * pi_val)
        print("pi val is ", pi_final_val)
        return pi_final_val

    def cal_alpha(self):
        alpha = 1
        print("in cal_alpha")
        for i in range(1, 2): # const_obj.alpha_iteration):
            self.round_intermediate = True
            residue = alpha - self.round_off_val(self.cal_sin((alpha))) - (3.14159/2)
            self.round_intermediate = True
            derivative = (1 - self.round_off_val(self.cal_cos((alpha))))
            alpha = alpha - ((residue) / derivative)
           # fx = self.pi/2 - alpha + self.cal_sin(self.degree_to_radian(alpha)) # to ck the alpha = 1 (rad)
           #  derivative_fx = -1 + (self.cal_cos(self.degree_to_radian(alpha)))
           #  alpha = alpha - (fx/derivative_fx)
            if residue == 0:
                print("the val of i::::when we got residual as zero is ::::::: "+i)
                break
        print("the val of func is(residual) ", residue)
        print("the val of the (derivative) is  ", derivative)
        self.round_intermediate = True
        print("the val of alpha to go next or x  is ::::::::  ", self.round_off_val(alpha))
        self.round_intermediate = True
        return self.round_off_val(alpha) # 2.304129659127962


            #self.round_intermediate = True
            # print("value returned by sin and cos is in cal alpha", self.cal_sin(self.degree_to_radian(alpha)),
            #       self.cal_cos(self.degree_to_radian(alpha)))
            # return self.round_off_val(alpha)

    def round_off_val(self, pi_arg):  # /////////////ck which one to pres pi which not
        prec = 1
        if self.round_intermediate:
            for i in range(0, self.precision_pi):
                prec = prec*10
        elif self.round_out:
            for i in range(0, self.precision_pi):
                prec = prec*10
        else:
            print("neither its is for intermediate nor output ")
        # float(pi_arg)
        # pi_arg = pi_arg * prec
        # int(pi_arg)
        # pi_arg = pi_arg/prec
        int_val = int((pi_arg * prec))# + 0.5)
        print("integer val is", int_val)
        pi_arg = int_val / prec
        print("pi_arg val is", pi_arg)
        self.round_out = False
        self.round_intermediate = False
        return pi_arg
        # return pi_arg

    def cal_length(self): # length should be arnd 1.0____
        print("in cal_length")
        # alpha_by_two = self.cal_alpha()
        # print("val of pi is: ", self.pi)
        # print("the cal of alpha is ", self.cal_alpha()) #actual val of alpha is 2.30988
       #may b to degree before divide
     #   cos_val = self.cal_cos(2.30988/2)  #print("%.2f" % a)
        print("degree to rad val is " ) # alpha 3861 without rad and 67. wit rad
        print("%.2f" % self.cal_alpha())
#//////////////////
        # to uncomment cos_val = self.cal_cos(self.degree_to_radian((self.cal_alpha())/2)) #const_obj.alpha/2)


      #  print("the calulated cos afetr alpha is ", cos_val)
     #   print("cos afetr alpha is risking calculation in alpha", self.cal_cos(self.degree_to_radian((self.cal_alpha())/2)))

# to uncomment
        # length_val = 2*(float(self.radius))*(1-float(cos_val))
        # self.round_out = True
        # print("val of pi is ", self.pi)
        # return self.round_off_val(length_val)

    def cal_cos(self, c_alpha): # x_alpha is in radian
        print("entering cal_cos")
        cos_series_sum = 1
        temp_val_cos = 1
        for i in range(1, const_obj.cos_iteration, +2):
            temp_val_cos = temp_val_cos * (-1) * (c_alpha * c_alpha) / (i * (i + 1))
            cos_series_sum = cos_series_sum + temp_val_cos
        self.round_intermediate = True
        cos_ser_numb = self.round_off_val(cos_series_sum)
        print("cos series numb is ", cos_ser_numb)
        return cos_ser_numb

    def cal_sin(self, s_alpha): # s_alpha is in radian
        print("entering cal_sin")
        sin_series_sum = s_alpha
        temp_val_sin = s_alpha
        for i in range(2, const_obj.sin_iteration, +2):
            a = temp_val_sin*(-1)
            b = s_alpha * s_alpha
            c = (i*(i+1))
            temp_val_sin = a * (b / c) # temp_val_sin*(-1) * (s_alpha * s_alpha)/(i(i+1))
            sin_series_sum = sin_series_sum + temp_val_sin
        self.round_intermediate = True
        sin_ser_numb = self.round_off_val(sin_series_sum)
        print("cos series numb is ", sin_ser_numb)
        return sin_ser_numb # nothing round off???cos done in alpha while call

    def degree_to_radian(self, degree):
        self.round_intermediate = True
        return self.round_off_val(degree * (self.pi / const_obj.straight_line_angle))

func_def_obj = func_def()
