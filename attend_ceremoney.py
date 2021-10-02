# Program to check whether student is able to attend the university ceremony or not 

class ceremony:
    def __init__(self, days=0, miss_class=4):
        self.days = days
        self.miss_class = miss_class
        self.total_possibility = None
        
    def get_possibility_to_attend_ceremony(self):
        '''
            This method will help to get the total possibility to attend the class in the university, and probability to attend the univerity ceremony
        '''
        # total possibility to attend the classes
        self.total_possibility = pow(2, self.days)
        cant_attend_ceremony = self.not_possible_to_attend()
        can_attend_ceremony =  self.possible_to_attend()
        print("possible to attend the ceremony is : ", can_attend_ceremony)
        print("possible to not attend the ceremony is : ", cant_attend_ceremony)

      
    def not_possible_to_attend(self):
        i = self.miss_class
        possibility = 0
        while self.days - i >= 0:
            print(self.days - i)
            possibility += ((self.days - i)*(self.days - i + 1))/2 + 1   # used n(n+1)/2,    
                                                                         # to calculate sum 
            i += 1
        return possibility
        
        
    def possible_to_attend(self):
        return self.total_possibility - self.not_possible_to_attend()
    
    
c = ceremony(5, 4)
c.get_possibility_to_attend_ceremony()
