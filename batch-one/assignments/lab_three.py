###########   Assignment 4 ########## 
#  
# Define Stock Class - initialize attributes via __init__ function
#        The attributes details are: 
#                close_index - Closing NSE Index 
#                open_index  -  NSE Opening Index 
#                high_index   - NSe Maximum Index 
#                low_index   - NSe Low Index 
#                date_s      - date for which index numbers are captured 
#   You need to complete the Stock Class code & sort the instances defined
#   below code. 
#
########################### 
 
from datetime import datetime
class Stock(object):
         def __init__(self, date_s, open_index, high_index,low_index, close_index):
               #TODO  define remaining attributes
            self.date_s = datetime.strptime(date_s, "%d-%b-%Y")


         def __repr__(self):
            pass 
            #TODO - define string which can help human read the Stock Instance.  
         
  



def getClosingIndex(S):
   pass 
   #TODO  - define function to return closing Index number


s1  = Stock("04-Jan-2016",     7924.55,     7937.55,     7781.10,     7791.30)
s2  = Stock("05-Jan-2016",     7828.40,     7831.20,     7763.25,     7784.65)
s3  = Stock("06-Jan-2016",     7788.05,     7800.95,     7721.20,     7741.00)
s4  = Stock("07-Jan-2016",     7673.35,     7674.95,     7556.60,     7568.30)
s5  = Stock("08-Jan-2016",     7611.65,     7634.10,     7581.05,     7601.35)
s6  = Stock("11-Jan-2016",     7527.45,     7605.10,     7494.35,     7563.85)
s7  = Stock("12-Jan-2016",     7587.20,     7588.30,     7487.80,     7510.30)
s8  = Stock("13-Jan-2016",     7557.90,     7590.95,     7425.80,     7562.40)
s9  = Stock("14-Jan-2016",     7467.40,     7604.80,     7443.80,     7536.80)
s10 = Stock("15-Jan-2016",     7561.65,     7566.50,     7427.30,     7437.80)
s11 = Stock("18-Jan-2016",     7420.35,     7463.65,     7336.40,     7351.00)
s12 = Stock("19-Jan-2016",     7381.80,     7462.75,     7364.15,     7435.10)
s13 = Stock("20-Jan-2016",     7357.00,     7470.90,     7241.50,     7309.30)

my_index = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13]

#TODO - sort my_index based on closing price
