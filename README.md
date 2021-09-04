# Python-exercises
Python exercises
# Online Translator
Artadecht is preparing an online translator for his university dissertation. The online translator that Artadekhet is preparing has a dictionary, and at the end of the day, this translator has to translate a sentence.
In the first line of input, there is a number "n", which represents the number of dictionary
words. Each of the next "n" lines consists of two words, indicating that the second word means the first word. The next line contains a sentence. A sentence contains a few words separated by space. Now you need to help Artadecht and write an interpreter who reads the dictionary and the corresponding sentence from the entrance and translates the sentence. In the translation process, if there is no word in the dictionary, print the word in the output yourself. For more information, pay attention to the sample input and sample output.


Note: The online arbitration system uses Python 3.4, in this version dictionaries do not remember the order of data entry to themselves and may not achieve the desired result if they are sorted, use OrderedDict to fix this problem instead of dict, this data structure can be imported from the collections library in the app.

Sample input:

5
hello salam
goodbye khodafez
say goftan
we ma
you shoma
we say goodbye to you tonight
Sample output:

ma goftan khodafez to shoma tonight
# Calculating twice the vice versa of a 3-digit number
Write a program that reads a three-digit number from the input and prints twice the vise versa of digits in the output. You can be sure that the input must be a three-digit number. For example, if the number 765 is typed in the input, print the number 567 * 2, ie 1134, in the output.

# Working with strings
Saman's just learned the strings. There's a fairly simple question ahead of him to get started with the strings, but he needs your help to do it. Saman should write the program to read a string of words from the entrance and make the following changes to it.

1- Erase all vowels.

2. Print a dot before each silent letter.

3. Write all the remaining silent letters in small numbers.
(Vowels are aeiou)


# Sarah Greets
Sarah has just learned to type and log on to the Internet. Once he got online, he decided to go into a chatroom and say hello to everyone. Sarah put a word into the chatroom. If you can remove some of the letters of the word that Sarah has entered and at the end the word hello remains, that is, Sarah can say hello otherwise no.
It is guaranteed that the entry consists only of lowercase English letters.
Sample input:

ahhellllloou
Sample output:

YES
 
Sample input:

hlelo
Sample output:

NO
 

# Small Letters Capital Letters
Ariamanesh is very upset that on the Internet, people use capital letters and small letters when they write a word. That's why he decided to write a browser that would write words with small letters and capital letters in a new way, so that if a word had more capital letters than the number of small letters, it would write the whole word in capital letters, otherwise it would write the whole word in small letters.


Sample input:

hasTAM
Sample output:

hastam
Is Palindrome?
Zargiso, who has just become familiar with programming, wants to write a program that determines whether a word is a palindrome. It's called a palindrome, whether you read it from the left or from the right. Madam, for example, is a palindrome, but tehran is not a palindrome. Now you have to help Zargiso write this program.
Please note that the small or large letters do not matter as we said Madam is a palindrome as maDAM is a palindrome.

Input sample:

madam
Output sample:

palindrome
 

Input sample:

tehran
Output sample:

not palindrome
 # Substring
 Jahangir works at a computer company. Jahangir is going to write a program that determines whether AB and BA can be found in another discipline without overlap. Ab and BA don't matter either. I mean, if it's ABBA input, there's a YES answer. If there's a BAAB entry, there's still a YES answer. But if it's an ABA entry, there's a NO answer, or if it's an ABHA entry, there's a NO answer. Can you help Jahangir write this program?

Please print YES and NO exactly the same way with capital letters in the output.



# world Kabaddi  Championships 

Officials from the Country's Kabeddi Federation are preparing teams to participate in the World Kabeddi Championships. According to the rules of the World Kabaddi Championships, only five world Kabaddi competitions can be participated. The president of the federation has gathered all the athletes in this field, each player has participated in the world championships a number of times to date. Kabaddi teams consist of exactly 3 people. Now, Mr. Shayegan Ariamehr, the president of the federation, wants to form teams that, if selected by each of those teams, can
participate in the world championships for at least 3 years (i.e. each member of a team has participated in the world championships at most twice) the first line of entry includes the number n, i.e. the number of Kabeddi players. The next line of input consists of n numbers separated by space, indicating that each player has participated in the World Championships several times. Print a number at the output that represents the maximum teams formed under the said conditions.


Sample input:

6
5 0 4 2 1 0
Sample output:

1
At the given sample entry, players who have played 5 and 4 games cannot be in the group according to the question, so only 4 players who have played 0, 2, 1 and 0 can be in groups. With 4 persons, only one group of 3 persons can be formed. Note that you don't have to count the number of modes (permutations).
# Laptop Prices
One day, Sindokht and Irsa were discussing the price of laptops and their quality. Sindokht guesses that the more expensive a laptop is, the better the quality. But Irsa claims to be able to find two laptops that have a lower price than the latter, but the quality is higher than the latter and can reject Sindokht's guess. Now you have to help Irsa review her claim by writing a program.
You'll be given n laptop specifications.
The first line of input contains the number "n" which indicates the number of laptops. Each of the next n lines contains two numbers, which represents the first number of the laptop price, and the second number is the quality of that laptop. If you can find two laptops that meet the requirements stated by IRSA print happy irsa otherwise print poor irsa (please note that the letters are small all letters are written in small form.)
Sample input:

2
1 10
7 3
Sample output:

happy irsa
 

In the first laptop sample entry has a price of 1 and the quality of 10 (the bigger the quality is) the second laptop is priced 7 and the quality 3. Well Irsa has managed to find two laptops that although the second price is higher than the first price but the second quality is less than the first quality.

 

Sample input:

4
1 5
7 9
5 6
20 30
Sample output:

poor irsa
# Vote Counting System
Mr. Jubin Artabaz is the president of the United Nations and is going to cast a vote on the selection of the Board of Directors! Domhar Jamshidi, who is in charge of the UNITED Nations computer, has written a program that counts how many ra'i each country has earned. You're going to help Dodmehr count the votes by writing a program.
The first line of entry contains the number "n", which displays the total number of votes.
Each of the next n lines contains the name of a country. The names of countries are made of lowercase English.
Print a line in output m, which includes the number of votes in each
country. Type the names of countries in alphabetical order in output. For more information, see sample input and sample output.


Note: The online arbitration system uses Python 3.4, in this version dictionaries do not remember the order of data entry to themselves and may not achieve the desired result if they are sorted, use OrderedDict to fix this problem instead of dict, this data structure can be imported from the collections library in the app.

Sample input:

5
sara
hamid
ali
sara
sara
Sample output:

ali 1
hamid 1
sara 3

 
# The Second Root
Write a program that reads a few positive numbers from the input and prints its second root up to 4 decimal places.
The first line shows the input of the number "n", which is the number of numbers you need to calculate the second
root. Each of the next n lines contains a positive number. For more information, pay attention to input and output samples. Tips: In this exercise, you should use the math library and the sqrt function of that library.

Please note that it should not be rounded in any way. Print exactly 4 digits after decimal places.

 

Sample Input

4
1
2
19
100
Sample Output

1.0000
1.4142
4.3588
10.0000
# Meet Nowruz
On the occasion of Nowruz, three old friends want to meet. Azarmehr, Azargoon and Mehr aein plan to meet at one point. The house of these three is located on the right line (axis x) of the house of Azarmehr is located at the x1 point, the house of Azargon is located at the point x2, and mehraein house is located at the x3 point. Overall, they want to travel the lowest distance. With x1 x2 x3 holding, calculate the lowest distance these three have to go through in total to meet at one point. Please print it without decimal point if the answer is integer, for example, in the example below, if you print 6.0 is incorrect.
Note that the distance is desired, not where they are supposed to meet.
Sample input:
6 9 10
Sample output:
4
# Finding the next number which is multiple of 10 after an input number 
Write a program that reads an input number and prints the next first multiple of 10, which is greater than this number. For example, if the number 11 was read from the input, the number 20 should be printed. If the number 40 is read, the number 50 should be printed.
# Finding Prime Number
In this program, read a positive number from the input and determine whether this number is prime or not.
If it was a prime number, print prime in the output, and if it was not a prime number, print not prime in the output. Please make sure the output is exactly as stated. 
# Summing Up Numbers
Somayeh is studying in second grade and is just learning to collect numbers. The class teacher wrote some numbers on the board, and the students had to count the sum of the numbers. To make it easier, the numbers that need to be summed up are just one and two and three. But that's not enough, and students can only do the plural when the numbers are arranged in a non-descending order (i.e. first one, then twos and then threes) you have to read the phrase that the teacher wrote at the foot of the board as input and generate the phrase that was explained in the output so that Somayeh and the other students can count it.
#  Standardization of Names
Mehdi is sending the final list of the names of the participants in the closing ceremony of fajr film for the executive committee so that they can print the entry cards. But there's something wrong. The participants didn't write their names as standard when they registered. Standard means exactly the first letter of the uppercase letter and the rest is lowercase. Write a program that reads 10 names from the input and prints them standardized in the output.
