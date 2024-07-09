from insertion import insertion_sort
from selectionsort import selection_sort
from timecalculation import current_time,cal_time
from randomarray import generate_random_array
import matplotlib.pyplot as plt
start_time = current_time()
time_array_insertion = []
time_array_selection = []
increment_size = 10
MAX_ARRAY_SIZE=5000
for i in range(MAX_ARRAY_SIZE):
    increment_size += 10
    array = generate_random_array(0,increment_size)
    start_time = current_time()
    insertion_sort(array)
    end_time = current_time()
    time_array_insertion.append(cal_time(start_time, end_time))
    start_time = current_time()
    selection_sort(array)
    end_time = current_time()
    time_array_selection.append(cal_time(start_time, end_time))
plt.plot(time_array_insertion, label='Insertion Sort')
plt.plot(time_array_selection, label='Selection Sort')
plt.xlabel('Array Size(array size)')
plt.ylabel('Time(Second)')
plt.title('Comparison of Sorting Algorithms')
plt.legend()
plt.show()