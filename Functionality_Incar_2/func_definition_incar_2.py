from Functionality_Incar_2.constants_incar_2 import const_incar_2_obj
import Libraries as lb


class func_def:
    precision_pi = const_incar_2_obj.pi_precision_val
    round_intermediate = False
    round_out = False

    # This funtion to checks whether the input values provided exist within the range or not
    def cheers_cal_inc_2(self, radius, precision, precision_out):
        self.radius = radius
        self.precision_input = precision
        self.precision_out = precision_out
        # if (self.radius < const_incar_2_obj.radius_floor) or (self.radius > const_incar_2_obj.radius_ceil):
        #     print("Kindly help to enter radius value in range [1 to 10]")
        # if (self.precision_input < const_incar_2_obj.precision_floor) or (self.precision_input > const_incar_2_obj.precision_ceil):
        #     print("Kindly help to enter precision value in range [1 to 10]")
        # if (self.precision_out < const_incar_2_obj.precision_output_floor) or \
        #         (self.precision_out > const_incar_2_obj.precision_output_ceil):
        #     print("Kindly help to enter the output precision value in range [1 to 10]")
        # ck if needed to assign the val to self
        self.pi = self.cal_pi()

# For calculating the value of pi
    def cal_pi(self):
        pi_val = lb.math.pi
        self.round_intermediate = True
        pi_final_val = self.round_off_val(pi_val)
        print("pi val is ", pi_final_val)
        return pi_final_val

 # Alpha calculated with the help of Newton's Method x(n + 1) = x(n) - f(x(n)) / f'(x(n))
    def cal_alpha(self):
        alpha = 1
        #print("in cal_alpha")
        # after 32 alpha_iterations the residue value tends to 0 and derivative stops changing
        for i in range(1, const_incar_2_obj.alpha_iteration):
            self.round_intermediate = True
            residue = alpha - self.round_off_val(lb.math.sin(alpha)) - self.pi/2
            self.round_intermediate = True
            derivative = (1 - self.round_off_val(lb.math.cos(alpha)))
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
        self.round_intermediate = True
        cos_val = (lb.math.cos(self.cal_alpha()/2))
        length_val = 2 * float(self.radius) * float(1-cos_val)
        # print("the length is comming ", length_val))
        self.round_out = True
        round_off_length = self.round_off_val(length_val)
        self.form_xml()
        return round_off_length

    def form_xml(self):
        print("xyz")
        # create XML
        # print("was used to print xml, kindly delete and Cheers.xml if you want to generate it again")
        # data_file = "Cheers.xml"
        # if lb.os.path.exists(data_file) != True:
        #     tmp = open(data_file, 'a')
        #     tmp.write("<list>Radius=1<\list>")
        #     tmp.write("1.192054")
        #     tmp.write("<list>Radius=2<\list>")
        #     tmp.write("2.384108")
        #     tmp.write("<list>Radius=3<\list>")
        #     tmp.write("3.576163")
        #
        #     tmp.close()
        # xmID = lb.etree.parse(data_file)
        # root = xmID.getroot()
        # print(root)


        # root = lb.etree.Element('Incarnation_2')
        # lb.etree.tree = lb.etree.ElementTree(root)
        # name = lb.etree.Element('Length Value')
        # root.append(name)
        # name.text = length_result
        # root.set('For_Radius', self.radius)
        # print(lb.etree.tostring(root))
        # lb.etree.tree.write("Cheers_1.xml")
       # # if lb.os.path.exists(data_file):



    def degree_to_radian(self, degree):
        self.round_intermediate = True
        return self.round_off_val(degree * (lb.math.pi / const_incar_2_obj.straight_line_angle))


func_def_obj_i_2 = func_def()
