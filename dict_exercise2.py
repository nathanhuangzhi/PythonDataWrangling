data= [
{'Exp1':'A', 'A': {'count':1, 'click': 0}},
{'Exp1':'A', 'A':{'count':1, 'click': 1}},
{'Exp1':'B', 'B':{'count':1, 'click': 0}},
{'Exp1':'B', 'B':{'count':1, 'click': 0}},
{'Exp2':'A', 'A':{'count':1, 'click': 0}},
{'Exp2':'A', 'A':{'count':1, 'click': 1}},
{'Exp2':'B', 'B':{'count':1, 'click': 0}},
{'Exp2':'B', 'B':{'count':1, 'click': 0}}
]

class Experiment(object):

    def __init__(self,object):
        self.data = object
        self.exp1_A_count = 0
        self.exp1_A_click = 0
        self.exp1_B_count = 0
        self.exp1_B_click = 0
        self.exp2_A_count = 0
        self.exp2_A_click = 0
        self.exp2_B_count = 0
        self.exp2_B_click = 0
        self.sum_stat(self.data)
        self.summary = self.print_sum()

    def print_sum(self):
        return {'Exp1': {'A': {'Total Count': self.exp1_A_count, 'Total Click': self.exp1_A_click},
                         'B': {'Total Count': self.exp1_B_count, 'Total Click': self.exp1_B_click}},
                'Exp2': {'A': {'Total Count': self.exp2_A_count, 'Total Click': self.exp2_A_click},
                         'B': {'Total Count': self.exp2_B_count, 'Total Click': self.exp2_B_click}}}
    def sum_stat(self,inp):
        for i in inp:
            if list(i.keys())[0] == 'Exp1':
                if i['Exp1'] == 'A':
                    self.exp1_A_count += i['A']['count']
                    self.exp1_A_click += i['A']['click']

                elif i['Exp1'] == 'B':
                    self.exp1_B_count += i['B']['count']
                    self.exp1_B_click += i['B']['click']
                else:
                    raise KeyError
            elif list(i.keys())[0] == 'Exp2':
                if i['Exp2'] == 'A':
                    self.exp2_A_count += i['A']['count']
                    self.exp2_A_click += i['A']['click']

                elif i['Exp2'] == 'B':
                    self.exp2_B_count += i['B']['count']
                    self.exp2_B_click += i['B']['click']
                else:
                    raise KeyError
            else:
                raise KeyError



    def update(self, input_data):
        self.sum_stat(input_data)
        self.summary = self.print_sum()

    def performance(self):

        if self.exp1_A_count==0 or self.exp1_B_count==0 or self.exp2_A_count ==0 or self.exp2_B_count==0:
            raise ValueError

        exp1_A_CTR = self.exp1_A_click/self.exp1_A_count
        exp1_B_CTR = self.exp1_B_click/self.exp1_B_count
        exp2_A_CTR = self.exp2_A_click/self.exp2_A_count
        exp2_B_CTR = self.exp2_B_click/self.exp2_B_count

        if exp1_A_CTR > exp1_B_CTR:
            print('A better in Exp 1')
        elif exp1_A_CTR <= exp1_B_CTR:
            print('B better in Exp 1')
        else:
            raise ValueError

        if exp2_A_CTR > exp2_B_CTR:
            print('A better in Exp 2')
        elif exp2_A_CTR <= exp2_B_CTR:
            print('B better in Exp 2')
        else:
            raise ValueError


aa = Experiment(data)
print(aa.summary)
print(aa.performance())
aa.update([
{'Exp1':'A', 'A': {'count':1, 'click': 0}},
{'Exp1':'B', 'B':{'count':1, 'click': 1}}])
print(aa.summary)
print(aa.performance())