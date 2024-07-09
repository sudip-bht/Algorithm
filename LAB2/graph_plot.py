from quick import quick_sort
from merge import merge_sort
from timecalculation import cal_time,current_time
from randomarray import generate_random_array
import matplotlib.pyplot as plt
start_time = current_time()
time_array_insertion = []
time_array_selection = []
increment_size = 10
MAX_ARRAY_SIZE=400
for i in range(MAX_ARRAY_SIZE):
    increment_size += 10
    array = generate_random_array(0,increment_size)
    start_time = current_time()
    quick_sort(array,0,len(array)-1)
    end_time = current_time()
    time_array_insertion.append(cal_time(start_time, end_time))
    start_time = current_time()
    merge_sort(array,0,len(array)-1)
    end_time = current_time()
    time_array_selection.append(cal_time(start_time, end_time))
plt.plot(time_array_insertion, label='Quick Sort')
plt.plot(time_array_selection, label='Merge Sort')
plt.xlabel('Array Size(array size)')
plt.ylabel('Time(Second)')
plt.title('Comparison of Sorting Algorithms')
plt.legend()
plt.show()