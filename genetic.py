#Initialisation, scoring, transforming, mutating, recheck scoring, repeat
#The goal of the project is to create a genetic algorithm

import string
import random


def initialisation_(number_of_words, target):
    #creating elements while calculating fitness
    ret = {}
    for x in range (0, number_of_words):
        dict_word = ''
        for y in range (0, len(target)):
            dict_word += random.choice(string.ascii_lowercase)
        ret[dict_word] = fitness(dict_word, target)
    return ret


def fitness(word, target):
    fitness_ret = 0
    for i in range (0, len(word)):
        if word[i] == target[i]:
            fitness_ret += 100/len(word)
    return fitness_ret


def fitness_all(target, words):
    for word in words:
        fitness_ret = 0
        for i in range(0, len(word)):
            if word[i] == target[i]:
                fitness_ret += 100 / len(word)
        words[word] = fitness_ret
    return words


def cross_over(words):
    # calculate total fitness
    sum = 0
    cur = 0
    for fitness in words.values():
        sum += fitness

    # generate percentage for each one
    if sum != 0:
        for word in words:
            words[word] = words[word] / sum * 100
            if words[word] != 0:
                words[word] += cur
                cur = words[word]

        # generation of a random number upgrade: float and not int
        random1 = random.randint(1, 99)
        random2 = random.randint(1, 99)

        # finding 2 reandom numbers (by percentage)
        fitnessmin1 = 101
        fitnessmin2 = 101
        selected_word1 = None
        selected_word2 = None

        # finding the correct words percentage wise
        for word in words:
            if words[word] < fitnessmin1 and words[word] >= random1:
                fitnessmin1 = words[word]
                selected_word1 = word

            if words[word] < fitnessmin2 and words[word] >= random2:
                fitnessmin2 = words[word]
                selected_word2 = word

        # crossing upgrade do both at same time
        copy = ""
        for char in range (0, len(selected_word1)):
            random1 = random.randint(1, 100)
            if random1 < 90:
                copy += selected_word1[char]
            else:
                copy += selected_word2[char]
        del words[selected_word1]
        words[copy] = 0
    return words


def mutation(mutation_rate, words):
    copy = ''
    ret = {}
    for word in words:
        for char in range(0, len(word)):
            random1 = random.randint(1, 100)
            if random1 <= mutation_rate:
                copy += random.choice(string.ascii_lowercase)
            else:
                copy += word[char]
        ret[copy] = 0
        copy = ''

    return ret


def add_missing(words, target, props_number):
    # creating elements while calculating fitness
    for x in range(0, props_number - len(words)):
        dict_word = ''
        for y in range(0, len(target)):
            dict_word += random.choice(string.ascii_lowercase)
        words[dict_word] = 0
    return words


def main():
    #we want to time the execution
    import time
    start_time = time.time()
    PROPS_NUMBER = 400
    word = "hello"
    list_of_words = initialisation_(PROPS_NUMBER, word)
    # YAY WE HAVE A STARTING POPULATION

    finished = False
    iteration = 0

    while not finished:
        for i in range (0, PROPS_NUMBER):
            list_of_words = cross_over(list_of_words)
        list_of_words = mutation(2, list_of_words)

        # adding missing elements
        list_of_words = add_missing(list_of_words, word, PROPS_NUMBER)

        list_of_words = fitness_all(word, list_of_words)
        iteration += 1

        for fitness in list_of_words.values():
            if fitness == 100:
                finished = True

    return [iteration, time.time() - start_time]


main()