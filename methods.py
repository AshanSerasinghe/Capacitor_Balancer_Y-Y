import itertools


def isFloat(num):
    try:
        x = float(num)
        return True
    except:
        return False



def get_input_from_user(self):
    original_data_dict = {'A':[self.lineEdit.text() , self.lineEdit_2.text()] , 'B':[self.lineEdit_3.text() , self.lineEdit_4.text()],
        'C':[self.lineEdit_5.text() , self.lineEdit_6.text()],
        'a':[self.lineEdit_7.text() , self.lineEdit_8.text()] , 'b':[self.lineEdit_11.text() , self.lineEdit_12.text()],
        'c':[self.lineEdit_9.text() , self.lineEdit_10.text()]}
    
    self.ORIGINAL_INPUT = original_data_dict

    original_data_list = [self.lineEdit.text() , self.lineEdit_2.text() , self.lineEdit_3.text() , self.lineEdit_4.text(), 
            self.lineEdit_5.text() , self.lineEdit_6.text(), self.lineEdit_7.text() , self.lineEdit_8.text(), 
            self.lineEdit_11.text() , self.lineEdit_12.text(), self.lineEdit_9.text() , self.lineEdit_10.text()]
    
    return original_data_list


def check_not_num(original_data_list):
    map = {1:"C(1,0)", 2:'C(1,1)', 3:'C(1,2)', 4:'C(1,3)', 5:"C(1,4)", 6:'C(1,5)', 7:'C(2,0)', 8:'C(2,1)' , 9:"C(2,2)", 10:'C(2,3)', 11:'C(2,4)', 12:'C(2,5)'}
    msg = ""
    counter = 1
    for d in original_data_list:
        if not isFloat(d):
            if msg == "":
                msg = msg + map[counter]
            else:
                msg = msg + '/' + map[counter]
        counter+=1
            
    if msg == "":
        return [True , msg]
    else:
        return [False , msg+' '+'are NOT valid capacitor values']



def reset_to_origial(self):
    self.label_13.setStyleSheet("background-color: rgb(240, 240, 240)") #rgb(240, 240, 240)
    self.label_14.setStyleSheet("background-color: rgb(240, 240, 240)")
    self.label_15.setStyleSheet("background-color: rgb(240, 240, 240)")
    self.label_16.setStyleSheet("background-color: rgb(240, 240, 240)")
    self.label_17.setStyleSheet("background-color: rgb(240, 240, 240)")
    self.label_18.setStyleSheet("background-color: rgb(240, 240, 240)")
    
    self.label_19.setStyleSheet("background-color: rgb(240, 240, 240)") #rgb(240, 240, 240)
    self.label_20.setStyleSheet("background-color: rgb(240, 240, 240)")
    self.label_21.setStyleSheet("background-color: rgb(240, 240, 240)")
    self.label_22.setStyleSheet("background-color: rgb(240, 240, 240)")
    self.label_23.setStyleSheet("background-color: rgb(240, 240, 240)")
    self.label_24.setStyleSheet("background-color: rgb(240, 240, 240)")
    
    
    # reset texts
    self.label_13.setText("C(1,0)")
    self.label_14.setText("C(1,1)")
    self.label_15.setText("C(1,3)")
    self.label_16.setText("C(1,2)")
    self.label_17.setText("C(1,5)")
    self.label_18.setText("C(1,4)")
    
    self.label_19.setText("C(2,1)")
    self.label_20.setText("C(2,0)")
    self.label_21.setText("C(2,5)")
    self.label_22.setText("C(2,4)")
    self.label_23.setText("C(2,3)")
    self.label_24.setText("C(2,2)")
    
    R = self.ORIGINAL_INPUT['A']
    Y = self.ORIGINAL_INPUT['B']
    B = self.ORIGINAL_INPUT['C']
    
    a = self.ORIGINAL_INPUT['a']
    b = self.ORIGINAL_INPUT['b']
    c = self.ORIGINAL_INPUT['c']
    
    
    self.lineEdit.setText(R[0]); self.lineEdit_2.setText(R[1])
    self.lineEdit_3.setText(Y[0]); self.lineEdit_4.setText(Y[1]) 
    self.lineEdit_5.setText(B[0]); self.lineEdit_6.setText(B[1]) 
    
    self.lineEdit_7.setText(a[0]); self.lineEdit_8.setText(a[1])
    self.lineEdit_11.setText(b[0]); self.lineEdit_12.setText(b[1])
    self.lineEdit_9.setText(c[0]); self.lineEdit_10.setText(c[1])



def all_pairs(lst):
        if len(lst) < 2:
            yield []
            return
        if len(lst) % 2 == 1:
            # Handle odd length list
            for i in range(len(lst)):
                for result in all_pairs(lst[:i] + lst[i+1:]):
                    yield result
        else:
            a = lst[0]
            for i in range(1,len(lst)):
                pair = (a,lst[i])
                for rest in all_pairs(lst[1:i]+lst[i+1:]):
                    yield [pair] + rest




def generate_groups(lst, n):
        if not lst:
            yield []
        else:
            for group in (((lst[0],) + xs) for xs in itertools.combinations(lst[1:], n-1)):
                for groups in generate_groups([x for x in lst if x not in group], n):
                    yield [group] + groups






def phase_capacitance(C1,C2): #to find capacitance of each branch
    try:
        #phase_capatnce = ( 1/float(C1) ) +( 1/float(C2) )
        phase_capatnce = float(C1)*float(C2)/(float(C1) + float(C2))
    except:
        phase_capatnce = 0

    return phase_capatnce

def diff(d1,d2): #to find difference of capacitance of each branch and calculate addition of that
    try:
        d=abs(float(d1)-float(d2))
    except:
        d = 0
    return d


def get_best_shuffel(a):

    final=[] #total of each shuffle
    for shuffle in a:
        sp_cap=[] #shuffled phase capacitance
        for x in shuffle: #find total capacitance of each branch
            sp_cap.append(phase_capacitance(x[0],x[1]))
        
        dif=[] #difference of capacitance of each branch
        for i in range(3):
            dif.append(diff(sp_cap[i],sp_cap[i+3]))
            
        sum=0
        for ele in range(0, len(dif)):
            sum = sum + dif[ele]
        
        final.append(sum)


    best_10 = []
    for i in range(0,10):
        ind= final.index( min(final) )
        best_10.append(a[ind])
        try:
            final.pop(ind)
            a.pop(ind)
        except:
            print("Error in pop")
    
    return best_10



def generate_strings(self, best):
    best_res_list = []

    
    
    for b in best:
        best_res_list.append( round(phase_capacitance(b[0] , b[1]) , 2))
    
    

    total_list_1 = best_res_list[0:3]
    total_list_2 = best_res_list[3:6]
    
    diff_list = []

    for i,j in zip(total_list_1, total_list_2):
        diff_list.append(abs(round(i-j, 4)))

    
    self.label_28.setText("Difference = " + str( diff_list ) + ' μF')
    self.label_26.setText("Total 1 = " + str( total_list_1 ) + ' μF')
    self.label_27.setText("Total 2 = " + str( total_list_2 ) + ' μF')


def display_best10_itteratively(self, best_10):
    R = best_10[0]
    Y = best_10[1]
    B = best_10[2]
    
    a = best_10[3]
    b = best_10[4]
    c = best_10[5]
    
    
    self.lineEdit.setText(R[0]); self.lineEdit_2.setText(R[1])
    self.lineEdit_3.setText(Y[0]); self.lineEdit_4.setText(Y[1]) 
    self.lineEdit_5.setText(B[0]); self.lineEdit_6.setText(B[1]) 
    
    self.lineEdit_7.setText(a[0]); self.lineEdit_8.setText(a[1])
    self.lineEdit_11.setText(b[0]); self.lineEdit_12.setText(b[1])
    self.lineEdit_9.setText(c[0]); self.lineEdit_10.setText(c[1])

    #==============================================================
    generate_strings(self, best_10)
    #==============================================================


    



# class get_all_permutations():
#     # cap_list = [13.47 , 13.505 , 13.615 , 13.385 , 13.52 , 13.64 , 13.61 , 13.63 , 13.78 , 13.65 , 13.655 , 13.545]
#     #print(cap_list)

#     def __init__(cap_list):
#         self.cap_list = cap_list
    
#     def all_pairs(lst):
#         if len(lst) < 2:
#             yield []
#             return
#         if len(lst) % 2 == 1:
#             # Handle odd length list
#             for i in range(len(lst)):
#                 for result in all_pairs(lst[:i] + lst[i+1:]):
#                     yield result
#         else:
#             a = lst[0]
#             for i in range(1,len(lst)):
#                 pair = (a,lst[i])
#                 for rest in all_pairs(lst[1:i]+lst[i+1:]):
#                     yield [pair] + rest

#     y = all_pairs(cap_list)
#     z = list(y)
#     #print(z[1])
#     # for x in z:
#     #     print (x)

#     # print (len(z))

#     def generate_groups(lst, n):
#         if not lst:
#             yield []
#         else:
#             for group in (((lst[0],) + xs) for xs in itertools.combinations(lst[1:], n-1)):
#                 for groups in generate_groups([x for x in lst if x not in group], n):
#                     yield [group] + groups

#     #print(list(generate_groups(cap_list, 2)))






