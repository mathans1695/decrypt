# Decrypt
## Geektrust 'A Golden Crown' problem
*You can view the problem statement by visiting this link - [A Golden Crown](https://www.geektrust.in/coding-problem/backend/tame-of-thrones)*

### Main file - geektrust.py:
- *Run this file and provide path to input file. It will tell you, whether King Shan successfully form alliances or not*

### Modules:
- *circular_ll.py*:
  - Circular linked list data structure used for this problem. This datastructure is limited in functionality and specifically designed to solve this problem
  - You can push new node to the end, move forward and backward using this datastructure

- *binary_search.py*:
  - Binary Search perform binary search on letters list, not on circular linked list.
  - This module was added to improve the performance of circular linked list. 
  - It helps the circular linked list to make decision, whether to move forward or backward in linked list to search for particular element in linked list

- *decrypt.py*:
  - Perform decryption of message based on kingdom using decrypt function
  - Records number of occurrences of each letters in decrypted message

- *emblem.py* and *letters_clock.py*:
  - Both file provide required data to solve the problem
  
### Tests:
- Run each test using *python filename*
- Tests were provided for every modules, expect 'emblem' and 'letters_clock'
- success_data and failure_data files were added to test whole app
- You have to run test files individually, I will add automation to it soon
