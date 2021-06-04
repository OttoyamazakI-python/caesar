"""
@class definitions
@brief
			   Definitions class to support caesar algorithm
@author Elias Silva
@date 2021-06-04
"""

class Cconfiguration_caesar:
    
    INITIAL_INT_PARAMETER = 0 
    INCREMENTAL_PARAMETER = 1
    DECREMENTAL_PARAMETER = -1  
    DUAL_PARAMETER = 2  
   
    ALPHABET_LIMIT = 26
    ALPHABET_LOWER_INDEX = 97
    ALPHABET_LOWER_LIMIT = 122
    ALPHABET_UPPER_INDEX = 65
    ALPHABET_UPPER_LIMIT = 90
    
class CextraStatusDefinition:

    SINGLETON_CLASS_ERROR = "SINGLETON CLASS ERROR"
    COMMAND_LINE_EERROR = "Usage: python caesar.py k"
