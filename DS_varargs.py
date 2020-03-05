def save_ranking(*args):
    print(args)
    return args
save_ranking('m', 'a', 't', 'w', 'r')
print(type(save_ranking('m', 'a', 't', 'w', 'r')))  #<class 'tuple'>

def save_ranking(**kwargs):
    print(kwargs)
    return kwargs
save_ranking(f = 'm', s = 'a',fth = 'w' ,t = 't',fif = 'r')
print(type(save_ranking(f = 'm', s = 'a',fth = 'w' ,t = 't',fif = 'r')))    #<class 'dict'>

def save_ranking(*a, **k):
    print(a)
    print(k)
save_ranking('m', 'a', 't',fth ='w', fif = 'r')