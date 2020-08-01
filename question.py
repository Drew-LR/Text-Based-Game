from constants import term

def yn_answer(self, val, y_con, n_con): # method to handle y/n answers
    if val == 'y':
        return y_con
    else:
        return n_con