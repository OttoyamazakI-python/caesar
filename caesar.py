"""
@class caesar
@author Elias Silva
@date 2021-06-04
"""

import sys
from Cdefinitions import *

class caesar:
    """
    @class  caesar()
    @brief Caesar algorithm to encript alphabet
    """       
    __instance = None
    @staticmethod 
    def getInstance():
        if caesar.__instance == None:
            caesar()
        return caesar.__instance
    def __init__(self):
        if caesar.__instance != None:
            raise Exception(CextraStatusDefinition.SINGLETON_CLASS_ERROR)
        else:
            caesar.__instance = self    
                
    def encript(self):
        """
        @function encript()
        @brief function to rotate k positions an alphanumerical input
        @parameters k is readed from terminal at the time that is excecuted the script and  plaintext is loaded using input function
        """               
        if (len(sys.argv) == Cconfiguration_caesar.DUAL_PARAMETER) and (int(sys.argv[Cconfiguration_caesar.INCREMENTAL_PARAMETER])>=Cconfiguration_caesar.INITIAL_INT_PARAMETER):
            result = ""
            k = int(sys.argv[Cconfiguration_caesar.INCREMENTAL_PARAMETER])
            plaintext = input("plaintext: ")
            for i in range(len(plaintext)):
              char = plaintext[i]
              if ((Cconfiguration_caesar.ALPHABET_LOWER_INDEX>ord(char)) or (Cconfiguration_caesar.ALPHABET_LOWER_LIMIT<ord(char))) and ((Cconfiguration_caesar.ALPHABET_UPPER_INDEX>ord(char)) or (Cconfiguration_caesar.ALPHABET_UPPER_LIMIT<ord(char))):
                result += char
              elif (char.isupper()):
                result += chr((ord(char) + k-Cconfiguration_caesar.ALPHABET_UPPER_INDEX) % Cconfiguration_caesar.ALPHABET_LIMIT + Cconfiguration_caesar.ALPHABET_UPPER_INDEX)
              else:
                result += chr((ord(char) + k - Cconfiguration_caesar.ALPHABET_LOWER_INDEX) % Cconfiguration_caesar.ALPHABET_LIMIT + Cconfiguration_caesar.ALPHABET_LOWER_INDEX)
            print(f"ciphertext: {result}")
        else:
            print(CextraStatusDefinition.COMMAND_LINE_EERROR)
            exit(Cconfiguration_caesar.INCREMENTAL_PARAMETER)        
              
if __name__ == '__main__':
    handler=caesar.getInstance()
    handler.encript()    
