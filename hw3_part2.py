def get_palindrom_dict(str):
    palindrom_dict = {}

    for t in range(len(str)):
        
        for i in range(len(str) - t):
            partial_string = str[i:(t + i + 1)]
            reverse_string = partial_string[-1: -(t + 1) -1 : -1]

            if(partial_string == reverse_string):
                
                if((t + 1) in palindrom_dict):
                    palindrom_dict[t + 1].append(partial_string)

                else:
                    palindrom_dict[t + 1] = [partial_string]

    return palindrom_dict



def check_match(str):

    if(len(str) % 2 == 1):
        return False
    
    help_dictionary = {}

    for even_index in range(0, len(str), 2):
        odd_index = even_index + 1

        if(str[even_index] in help_dictionary):
            
            if(help_dictionary[str[even_index]] != str[odd_index]):
                return False

        else:
            help_dictionary[str[even_index]] = str[odd_index]

    return True
           

                    

