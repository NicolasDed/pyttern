# Author: Timothé Paquet
# Date: 2024-10-31
# Description: Functions useful to apply complex pattern matching (composed of multiple patterns)
# Modified by: Julien Liénard
import sys
from os import listdir

from loguru import logger

from .matcher import match_files


class SingleFileError(Exception):
    pass

def retrieve_feedbacks(path):
    """
    Retrieves all feedbacks, stores them into a dictionary with the key-value pair misconception_name-feedback and returns the dictionary.
    """
    pyt_feedback = {}
    for pyttern in listdir(path):
        for f in listdir(f"{path}/{pyttern}"):
            if f[-8:] == "feedback":
                with open(f"{path}/{pyttern}/{f}", 'r') as file:
                    logger.debug(f"Reading feedback from {path}/{pyttern}/{f}")
                    pyt_feedback[pyttern] = file.read().replace('\n', '')
    return pyt_feedback


def retrieve_pytterns_and_explore(path, code, pyt_dict):
    """
    Browses the pyttern folder, matches the misconceptions and the code, stores the results in a dictionary and returns this dictionary.
    """
    logger.debug(f"Retrieving pytterns from {path}")
    for pyttern in listdir(path):
        for f in listdir(f"{path}/{pyttern}"):
            if f[-8:] != "feedback":
                logger.debug(f"Starting exploration on {path}/{pyttern}/{f}")
                pyt_dict[pyttern] = match_misconception(f"{path}/{pyttern}", f, code)



def match_misconception(path, current, code):
    """
    Explores a misconception folder and returns a boolean representing if the misconception is matched or not.
    """

    new_path = f"{path}/{current}"
    logger.debug(f"Exploring {path}/{current}")
    file_ext = current.split('.')[-1]
    
    # Matches code with a pyttern
    if file_ext == "pyt":
        logger.debug(f"Matching {new_path} with {code}")
        return match_files(new_path, code)
    
    # Matches code with a regex
    elif file_ext == "re":
        # return regex_match_function(...)
        pass

    # Apply "and" operator to items in the "and" folder
    elif current == "and":
        for f in listdir(new_path):
            if not match_misconception(new_path, f, code):
                return False
        return True
    
    # Apply "or" operator to items in the "or" folder
    elif current == "or":
        for f in listdir(new_path):
            if match_misconception(new_path, f, code):
                return True
        return False
    
    # Apply "not" operator to the unique file or folder in the "not" folder
    elif current == "not":
        f = listdir(new_path)[0]
        if len(listdir(new_path)) > 1:
            print(f"Error: 'not' folder should contain only one file or folder. {f} taken as default", file=sys.stderr)
        return not match_misconception(new_path, f, code)


