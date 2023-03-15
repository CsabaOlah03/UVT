import random
import time
import csv

number_of_elements = 10000
range_of_numbers = 100000
number_of_runs = 1

def randomNumberGeneratorFiles():
    with open("random_numbers", 'w') as g:
        global number_of_elements
        for _ in range(1, number_of_elements):
            x = random.randint(1, range_of_numbers)
            g.write(str(x))
            g.write(" ")

def readInList(l, file_with_numbers):
    ls = []
    global number_of_elements
    with open(file_with_numbers, 'r') as f:
        for i in range(1, number_of_elements):
            x = f.read()
            ls = x.split(" ")
            for y in ls:
                if y != "":
                    l.append(int(y))

class sorting:
    def __init__(self,array):
        self.sortArr = []
        self.sortArr[:] = array

    def insertion_sort(self):
        start_time = time.time()
        for i in range(1, len(self.sortArr)):
            key = self.sortArr[i]
            j = i - 1
            while j >= 0 and self.sortArr[j] > key:
                self.sortArr[j + 1] = self.sortArr[j]
                j = j - 1
            self.sortArr[j + 1] = key
        return self.sortArr, time.time() - start_time

    def selection_sort(self):
        start_time = time.time()
        for i in range(0, len(self.sortArr)):
            min_index = i
            for j in range(i + 1, len(self.sortArr)):
                if self.sortArr[min_index] > self.sortArr[j]:
                    min_index = j
            self.sortArr[i], self.sortArr[min_index] = self.sortArr[min_index], self.sortArr[i]
        return self.sortArr, time.time() - start_time

    def bubble_sort(self):
        start_time = time.time()
        n = len(self.sortArr)

        for i in range(n):
            for j in range(0, n - i - 1):
                if self.sortArr[j] > self.sortArr[j + 1]:
                    self.sortArr[j], self.sortArr[j + 1] = self.sortArr[j + 1], self.sortArr[j]
        return self.sortArr, time.time() - start_time

    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_array = arr[:mid]
            right_array = arr[mid:]
            sorting.merge_sort(left_array)
            sorting.merge_sort(right_array)
            i, j, k = 0, 0, 0
            while i < len(left_array) and j < len(right_array):
                if left_array[i] <= right_array[j]:
                    arr[k] = left_array[i]
                    i += 1
                else:
                    arr[k] = right_array[j]
                    j += 1
                k += 1
            while i < len(left_array):
                arr[k] = left_array[i]
                i += 1
                k += 1
            while j < len(right_array):
                arr[k] = right_array[j]
                j += 1
                k += 1

    def __partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(arr, low, high):
        if low < high:
            pivot = sorting.__partition(arr, low, high)
            sorting.quick_sort(arr, low, pivot - 1)
            sorting.quick_sort(arr, pivot + 1, high)

    def counting_sort(arr):
        max_element = int(max(arr))
        min_element = int(min(arr))
        range_of_elements = max_element - min_element + 1

        count_arr = [0 for _ in range(range_of_elements)]
        output_arr = [0 for _ in range(len(arr))]

        for i in range(0, len(arr)):
            count_arr[arr[i] - min_element] += 1

        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
            count_arr[arr[i] - min_element] -= 1

        for i in range(0, len(arr)):
            arr[i] = output_arr[i]

        return arr

    def __heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            (arr[i], arr[largest]) = (arr[largest], arr[i])

            sorting.__heapify(arr, n, largest)

    def heap_sort(arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            sorting.__heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            (arr[i], arr[0]) = (arr[0], arr[i])
            sorting.__heapify(arr, i, 0)

    def __counting_sort_radix(array, place):
        size = len(array)
        output = [0] * size
        count = [0] * 10

        for i in range(0, size):
            index = array[i] // place
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = size - 1
        while i >= 0:
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, size):
            array[i] = output[i]

    def radix_sort(array):
        max_element = max(array)

        place = 1
        while max_element // place > 0:
            sorting.__counting_sort_radix(array, place)
            place *= 10

    def counting_sort_reversed(array):
        start_time = time.time()
        maxValue = 0
        for i in range(len(array)):
            if array[i] > maxValue:
                maxValue = array[i]

        buckets = [0] * (maxValue + 1)

        for i in array:
            buckets[i] += 1

        i = 0
        for j in range(maxValue, -1, -1):
            for a in range(buckets[j]):
                array[i] = j
                i += 1

        return array, time.time() - start_time


    def __array_swap(A, i, j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp

    # take median of three elements
    def __median_three(a, b, c):
        return sorted([a, b, c])[1]

    def __qs_part(A, lo, hi):
        mid = lo
        p = sorting.__median_three(A[lo], A[(lo + hi) // 2], A[hi])  # pivot set to median of 3, as described in handout

        while mid <= hi:
            if A[mid] < p:
                sorting.__array_swap(A, mid, lo)
                mid += 1
                lo += 1
            elif A[mid] > p:
                sorting.__array_swap(A, mid, hi)
                hi -= 1
            else:
                mid += 1
        return (lo - 1), mid

    # Quicksort implementation as described in handout.
    # A: Array to sort
    # write:    name of file to write sorted results to
    # out:      name of file to write runtime to
    # lo:       start index (1 after pivot in first case)
    # hi:       end index
    def quick_sort_improved(A, lo, hi):
        if lo >= hi:
            return  # if there are 0 or 1 elements in A

        if lo - hi == 1:
            if A[lo] < A[hi]:  # if 2 elements, sort them
                sorting.__array_swap(A, lo, hi)
            return

        i, j = sorting.__qs_part(A, lo, hi)
        sorting.quick_sort_improved(A, lo, i)  # recursively sort partition 1 (elements < pivot)
        sorting.quick_sort_improved(A, j, hi)  # recursively sort partition 2 (elements > pivot)
        # no need to sort between 'i' and 'j' because those items == pivot

def write_in_file(output_list,array):
    with open(output_list, 'w') as g:
        running_times = []

        temp = sorting.insertion_sort(sorting(array))
        g.write(f"Insertion sort: {temp[1]}s\n")
        # for x in temp[0]:
        #     g.write(f"{x} ")
        g.write("\n")
        running_times.append(temp[1])

        temp = sorting.selection_sort(sorting(array))
        g.write(f"Selection sort: {temp[1]}s\n")
        # for x in temp[0]:
        #     g.write(f"{x} ")
        g.write("\n")
        running_times.append(temp[1])

        temp = sorting.bubble_sort(sorting(array))
        g.write(f"Bubble sort: {temp[1]}s\n")
        # for x in temp[0]:
        #     g.write(f"{x} ")
        g.write("\n")
        running_times.append(temp[1])

        temp = []
        temp[:] = array
        start_time = time.time()
        sorting.merge_sort(temp)
        running_time = time.time() - start_time
        g.write(f"Merge sort: {running_time}s\n")
        # for x in temp:
        #     g.write(f"{x} ")
        g.write("\n")
        running_times.append(running_time)

        '''
        temp[:] = array
        start_time = time.time()
        sorting.quick_sort(temp, 0, len(temp) - 1)
        running_time = time.time() - start_time
        g.write(f"Quick sort: {running_time}s\n")
        for x in temp:
            g.write(f"{x} ")
        g.write("\n")
        running_times.append(running_time)
        '''

        temp[:] = array
        start_time = time.time()
        sorting.quick_sort_improved(temp, 0, len(temp) - 1)
        running_time = time.time() - start_time
        g.write(f"Quick sort improved: {running_time}s\n")
        # for x in temp:
        #     g.write(f"{x} ")
        g.write("\n")
        running_times.append(running_time)

        temp[:] = array
        start_time = time.time()
        sorting.counting_sort(temp)
        running_time = time.time() - start_time
        g.write(f"Counting sort: {running_time}s\n")
        # for x in temp:
        #     g.write(f"{x} ")
        g.write("\n")
        running_times.append(running_time)

        temp[:] = array
        start_time = time.time()
        sorting.heap_sort(temp)
        running_time = time.time() - start_time
        g.write(f"Heap sort: {running_time}s\n")
        # for x in temp:
        #     g.write(f"{x} ")
        g.write("\n")
        running_times.append(running_time)

        temp[:] = array
        start_time = time.time()
        sorting.radix_sort(temp)
        running_time = time.time() - start_time
        g.write(f"Radix sort: {running_time}s\n")
        # for x in temp:
        #     g.write(f"{x} ")
        g.write("\n")
        running_times.append(running_time)

        return running_times


def sortNearlySortedArray(arr, k):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Check if the previous element is greater than the current
        # element, and shift elements to the right until the correct
        # position is found, but only if the current element is more
        # than k positions away from its correct position
        while j >= max(0, i - k) and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def prepare_output_files(csv_file):
    with open(csv_file, "w") as g:
        writer = csv.writer(g)
        writer.writerow(["Insertion sort", "Selection sort", "Bubble sort", "Merge sort", "Quick sort (improved)", "Counting sort", "Heap sort", "Radix sort"])

def just_work_already_pls(running_times_collection,csv_file):
    with open(csv_file, "a") as g:
        writer = csv.writer(g)
        writer.writerows(running_times_collection)

number_of_elements = int(input("(1/3) How many numbers do you want your list to have? "))
range_of_numbers = int(input("(2/3) How large should the range be? (Eg. '10000' for the range 1-10000)? "))
number_of_runs = int(input("(3/3) For how many iterations would you like your program to run? "))

prepare_output_files("average_from_random.csv")
prepare_output_files("average_from_reversed.csv")
prepare_output_files("average_from_nearly_sorted.csv")

for i in range(number_of_runs):

    array = []
    running_times = []
    avg_running_times_random = []
    avg_running_times_reversed = []
    avg_running_times_nearly_sorted = []
    #Generate random numbers and read them from a file into a list
    randomNumberGeneratorFiles()
    readInList(array, file_with_numbers="random_numbers")

    #--------------------------------------------------

    #Run the sorting algorithms on previously randomised list
    #and save running times in a list.
    running_times[:] = write_in_file("sorted_from_random", array)
    avg_running_times_random.append(running_times)

    #Empty the list for use down the line
    running_times = []

    #--------------------------------------------------

    #Create a reverse-sorted list and read them from a file to a list
    with open("sorted_reversed", 'w') as g:
        temp = []
        temp[:] = array
        temp = sorting.counting_sort_reversed(array)
        for x in temp[0]: #write only the array in file, temp[1] being execution time
            g.write(f"{x} ")
    array = []
    readInList(array, file_with_numbers="sorted_reversed")

    #Run the sorting algorithms on reverse-sorted list
    #and save running times in a list.
    running_times[:] = write_in_file("sorted_from_reversed", array)
    avg_running_times_reversed.append(running_times)

    # Empty the list for use down the line
    running_times = []

    # --------------------------------------------------

    # Create a nearly-sorted list and read them from a file to a list
    with open("nearly_sorted", 'w') as g:
        temp = []
        temp[:] = array
        sortNearlySortedArray(temp, 1000)
        for x in temp:
            g.write(f"{x} ")
    array = []
    readInList(array, file_with_numbers="nearly_sorted")

    # Run the sorting algorithms on nearly-sorted list
    # and save running times in a list.
    running_times[:] = write_in_file("sorted_from_nearly_sorted", array)
    avg_running_times_nearly_sorted.append(running_times)

    # Empty the list
    running_times = []

    # Write the average running times in a file
    just_work_already_pls(avg_running_times_random,csv_file="average_from_random.csv")
    just_work_already_pls(avg_running_times_reversed,csv_file="average_from_reversed.csv")
    just_work_already_pls(avg_running_times_nearly_sorted,csv_file="average_from_nearly_sorted.csv")

