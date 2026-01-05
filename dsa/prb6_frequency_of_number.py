from pprint import pprint

def calculate_freq(no_lst):
    no_freq={}
    for i in no_lst:
        no_freq[i] = no_freq.get(i,0) + 1
    return no_freq
    

lst = [1,1,3,2,3,4,5,6,7]
result_dictionary = calculate_freq(lst)

pprint(result_dictionary)