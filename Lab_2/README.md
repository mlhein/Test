## 1.0 Part 2 - Discussion
Q: You have implemented several types of sorting algorithm in Lab 2. Discuss the advantages and the disadvantages of each algorithm in terms of it’s complexity and practicality.

### 1.1 Advantages and disadvantages
| Algorithms    | Advantages | Disadvantages | Notes|
|----------     |----------|----------|----------|
| Bubble sort   | <ul>1. Easy to understand</ul><ul>2. Easy to implement</ul>  <ul>3. Performs grealty when the arry is almost sorted</ul>  <ul>4. In-place, no external memory is needed</ul><ul>5. | <ul>1. Very expensive, **O(n^2)** in worst case and average case.</ul> | It is the best algorithm to begin learning sorting algorithms because it is the simplest. It is very easy to implement in every programming language. In computer graphics it is popular for its capability to detect a very small error (like swap of just two elements) in almost-sorted arrays and fix it with just linear complexity (2n). Also, the bubble sort is considered a comparison algorithm, as it compares the elements at each run. |
| Counting sort | <ul>1. Complexity **O(n + k)**, where *n* is the size of the sorted array and *k* is the size of the helper array.(FAST)</ul><ul>2. Stable</ul>     | <ul>1. If non-primitive (object) elements are sorted, another helper array is needed to store the sorted elements.</ul><ul>2. Can only be use for sorting discrete values (integer), otherwise the array of frequencies cannot be constructed. </ul> <ul>3. Not recommended on large sets of data</ul>     | Counting sort may for example be the best algorithm for sorting numbers whose range is between 0 and 100, but it is probably unsuitable for sorting a list of names alphabetically. However, counting sort can be used with radix sort to sort a list of integers whose range is too large for counting sort to be suitable alone. |
| Bucket sort   | <ul>1. The user knows the range of the elements; </ul><ul>2. Time complexity is good compared to other algorithms.</ul>      | <ul>1. Extra memory is required</ul> <ul>2. You are limited to having to know the greatest element.</ul| If you know the range of the elements, the bucket sort is quite good, with a time complexity of only O(n+k). At the same time, this is a major drawback, since it is a must to know the greatest elements. It is a distribution sort and a cousin of radix sort. |
| Shell sort    | <ul>1. Only efficient for medium size lists  </ul><ul>2. 5 times faster than the bubble sort and a little over twice as fast as the insertion sort, its closest competitor </ul>    |   <ul>1. It is a complex algorithm and its not nearly as efficient as the merge, heap, and quick sorts. </ul><ul>2. Significantly slower than the merge, heap, and quick sorts</ul>  |Shell sort is faster than bubble sort or insert sort, but it’s efficient only on medium size lists. It is a complex algorithm, and defining the increments play a big role in the speed of the algorithm. Knuth defined a good formula, but Robert Sedgewick came with a sequence that he claims to be 20-30% faster than the one that Knuth recommended. |

## 2.0 Quick reference.

1. Reference:
 - https://github.com/OmkarPathak/Python-Programs/tree/master/Programs
 - https://www.geeksforgeeks.org/sorting-algorithms/
 - https://en.wikipedia.org/wiki/Sorting_algorithm
 - http://www.exforsys.com/tutorials
