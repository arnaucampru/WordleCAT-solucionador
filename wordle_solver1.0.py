# INTRO ----------------------------------------------------------------------
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 16:53:36 2022
@author: Arnau Camprubí Pujol
@mail: acamprubi1@gmail.com
"""
# IMPORTS --------------------------------------------------------------------
import os
import random

# FUNCTIONS ------------------------------------------------------------------
"""
Changes the current path to the working path
"""
def change_path():
    os.chdir('C:/Users/Campru/Documents/Arnau/wordle')
    current_directory = os.getcwd()
    return(current_directory)

"""
Gets a list including all the words with 5 letters of the file DISC2-LP.txt
"""
def words_dictionary():
    words_dictionary = list()
    file = open('DISC2-LP.txt')
    lines = file.readlines()
    for word in lines:
        if (len(word)==6):
            word = word[0:-1]
            words_dictionary.append(word)
    file.close()
    return(words_dictionary)

"""
Creates a .txt including all the words of DISC2-LP.txt with 5 letters
"""
def five_letters_txt(dic):
    file = open("DISC2-LP (5 letters).txt", "w")
    for word in dic:
        file.write(word + "\n")
    file.close()
    return()

"""
Gets a list including all the words with unique letters from a list
"""
def unique_words_dictonary():
    unique_words_dictonary = list()
    for word in words_dictionary:
        aux = list()
        letters_cont = 0
        for letter in word:
            if (letter in aux):
                break
            aux.append(letter)
            letters_cont += 1
            if (letters_cont == 5): unique_words_dictonary.append(word)
    return(unique_words_dictonary)
    
"""
Gets a random word from a list
"""
def get_random_word(dic):
    return(random.choice(dic))

"""
Updates the 'multilist_correct_word' list
"""
def update_multilist_correct_word():
    for x in range(5):
        if (correct_word[x] != 0):
            aux = [correct_word[x], x]
            if (aux not in multilist_correct_word):
                multilist_correct_word.append([correct_word[x], x])
    return(multilist_correct_word)

#-----------------------------------------------------------------------------
"""
Updates the 3 lists (correct_word, letters_to_use, wrong_letters)
"""
def update_3_lists():
    pos = 0
    for x in results:
        if x[1] == 'b':
            validate_right()
    for x in results:
        if x[1] == 'c' and x[0] not in letters_to_use and x[0] not in correct_word:
            letters_to_use.append(x[0])
        pos += 1
    for x in results:
        if x[1] == 'm' and x[0] not in correct_word and x[0] not in letters_to_use:
            wrong_letters.append(x[0])
    return()

"""
An update_3_lists function. Updates the 'correct_word' list
"""
def validate_right():
    pos = 0
    for letter in results:
        if letter[1] == 'b':
            correct_word[pos] = letter[0]
        pos += 1
    return()

"""
Updates the list 'results' from a 'input_attempt' and a 'word' used
"""
def update_results(attempt, word):
    cont = 0
    for letter in attempt:
        results[cont][1] = letter
        cont += 1
    cont = 0
    for letter in word:
        results[cont][0] = letter
        cont += 1
    return(results, word)

#-----------------------------------------------------------------------------
"""
Computes attempt 1
"""
def compute_attempt1(dic):
    word1 = get_random_word(dic)
    print("INITIAL WORD:   ", word1)
    print("INTRODUCE RESULTS:   ")
    input_attempt1 = input()
    print("\n")
    return(input_attempt1, word1)

"""
Computes attempts 2 to 5. Reduces 'words_dictionary' by considering the 3 current conditions
"""
def compute_other_attempts():
    dic1 = check_correct_word(words_dictionary)
    dic2 = check_letters_to_use(dic1)
    dic3 = check_wrong_letters(dic2)
    word = get_random_word(dic3)
    while word in chosen_words:
        word = get_random_word(dic3)
    print("WORD:   ", word)
    print("INTRODUCE RESULTS:   ")
    input_attempt = input()
    print("\n")
    return(input_attempt, word)
                
"""
A compute_other_attempts function. Respects the 'correct_word'
"""
def check_correct_word(dic):
    return_dic = list()
    for word in dic:
        stay_in = True
        for character in multilist_correct_word:
            if (character[0] != word[character[1]]): # respectar correct_word
                stay_in = False
                break
        if stay_in == True:
            return_dic.append(word)
    return(return_dic)

"""
A compute_other_attempts function. Respects the 'letters_to_use'
"""
def check_letters_to_use(dic):
    return_dic = list()
    for word in dic:
        stay_in = True
        for character in letters_to_use:
            if character not in word: # respectar letters_to_use
                stay_in = False    
                break
        if stay_in == True:
            return_dic.append(word)
    return(return_dic)

"""
A compute_other_attempts function. Respects the 'wrong_letters'
"""
def check_wrong_letters(dic):
    return_dic = list()
    for word in dic:
        stay_in = True
        for character in wrong_letters:
            if character in word: # no fer servir wrong_letters
                stay_in = False    
                break
        if stay_in == True:
            return_dic.append(word)
    return(return_dic)
 
# CHANGING THE PATH ----------------------------------------------------------
current_directory = change_path()
#print(current_directory)
   
# INITIALIZING GLOBAL VARIABLES ----------------------------------------------
correct_word = [0,0,0,0,0]
multilist_correct_word = []
letters_to_use = []
wrong_letters = []

words_dictionary = words_dictionary()
five_letters_txt(words_dictionary)
unique_words_dictonary = unique_words_dictonary()

results = [[0,0],[0,0],[0,0],[0,0],[0,0]] # input results of each iteration

chosen_words = []

# ATTEMPT 1 ------------------------------------------------------------------
input_attempt1, word1 = list(compute_attempt1(unique_words_dictonary))
chosen_words.append(word1)
results, word1 = update_results(input_attempt1, word1)
print("results:   ", results)

update_3_lists()
print("correct_word:   ", correct_word)
print("letters_to_use:   ", letters_to_use)
print("wrong_letters:   ", wrong_letters)

update_multilist_correct_word()
print("multilist_correct_word:   ", multilist_correct_word)
print("==============================================================")

# ATTEMPTS 2-5 ---------------------------------------------------------------
cont = 2
while True:
    input_attempt, word = compute_other_attempts()
    chosen_words.append(word)
    if input_attempt == 'bbbbb': 
        print("WELL PLAYED! You needed",cont,"attempts to solve the game")
        break
    results, word = update_results(input_attempt, word)
    
    print("results:   ", results)
    
    update_3_lists()
    print("correct_word:   ", correct_word)
    print("letters_to_use:   ", letters_to_use)
    print("wrong_letters:   ", wrong_letters)
    
    update_multilist_correct_word()
    print("multilist_correct_word:   ", multilist_correct_word)
    print("==============================================================")
    cont += 1