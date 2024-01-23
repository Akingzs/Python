
def criar_funcao(function):
    
    def inner(*args,**kwargs):
        
        resultado = function(zip_lists(*args))    
        return print(resultado)
    
    return inner

def zip_lists(*args):
    zipped = list(zip(*args))
    return zipped

@criar_funcao
def list_sum(lists):
    result = []
    for item in lists:
        result.append(sum(item))
    return result
    
list1 = [2,4,6,8]
list2 = [1,3,5,7,9]

list3 = [1,3,5,7,9,0]


# agrupamento = zip_lists(list1,list2,list3)

list_sum(list1,list2,list3)

# print(list_sum(agrupamento))
