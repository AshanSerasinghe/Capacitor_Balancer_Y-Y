def get_input_from_user(self):
    original_data_dict = {'A':[self.lineEdit.text() , self.lineEdit_2.text()] , 'B':[self.lineEdit_3.text() , self.lineEdit_4.text()],
        'C':[self.lineEdit_5.text() , self.lineEdit_6.text()],
        'a':[self.lineEdit_7.text() , self.lineEdit_8.text()] , 'b':[self.lineEdit_11.text() , self.lineEdit_12.text()],
        'c':[self.lineEdit_9.text() , self.lineEdit_10.text()]}
    
    self.ORIGINAL_INPUT = original_data_dict

    print(original_data_dict)



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