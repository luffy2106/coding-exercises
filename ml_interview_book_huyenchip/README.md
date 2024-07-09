## These question taken from ML interview book of Huyen Chip

https://huyenchip.com/ml-interviews-book/contents/6.1-algorithms.html


Examples of classic algorithms you should know include various sorting algorithms (quicksort, radix sort), shortest path algorithms (Dijkstra’s, A*), tree algorithms (pre-, in-, post-order traversal), and solutions to popular problems such as the stable marriage problem and traveling salesman problem. You will probably never have to implement them since there already exist many efficient implementations, but it’s important to understand their underlying design principles and implementation tradeoffs in case you have to make similar decisions in your job.

There are also programming techniques that you should be comfortable with, such as dynamic programming, recursions, string manipulation, matrix multiplication, regular expression, and memory allocation. Below are some of the questions that you might want to go over to refresh your memory.

1. Write a Python function to recursively read a JSON file.
2. Implement an sorting algorithm, preferably quick sort or merge sort.
3. Find the longest increasing subsequence in a string.
4. Find the longest common subsequence between two strings.
5. Traverse a tree in pre-order, in-order, and post-order.
6. Given an array of integers and an integer k, find the total number of continuous subarrays whose sum equals . The solution should have runtime.
7. There are two sorted arrays and with and elements respectively. Find the median of the two sorted arrays. The solution should have runtime.
8. Write a program to solve a Sudoku puzzle by filling the empty cells. The board is of the size . It contains only 1-9 numbers. Empty cells are denoted with *. Each board has one unique solution.
9. Given a memory block represented by an empty array, write a program to manage the dynamic allocation of that memory block. The program should support two methods: malloc() to allocate memory and free() to free a memory block.
10. Given a string of mathematical expression, such as 10 * 4 + (4 + 3) / (2 - 1), calculate it. It should support four operators +, -, :, /, and the brackets ().
11. Given a directory path, descend into that directory and find all the files with duplicated content.
12. In Google Docs, you have the Justify alignment option that spaces your text to align with both left and right margins. Write a function to print out a given text line-by-line (except the last line) in Justify alignment format. The length of a line should be configurable.
13. You have 1 million text files, each is a news article scraped from various news sites. Since news sites often report the same news, even the same articles, many of the files have content very similar to each other. Write a program to filter out these files so that the end result contains only files that are sufficiently different from each other in the language of your choice. You’re free to choose a metric to define the “similarity” of content between files.