#just some functions to find the average, median, and mode of a given set of numbers.

def find_average(nums):
    ave = round(sum(nums) / len(nums), 2)
    print(f'The average of your numbers is {ave}')

def find_median(nums):
    nums.sort()
    if len(nums) % 2 == 0: #test for whether thsi is an even set of numbers.
        median_index = len(nums)//2 - 1 #floor divided by 2 will result in the first medien index (ie, 6//2 = 3. Need to account for index 0
        median_index2 = median_index + 1 #with the first median index identified, just add 1 to get the second.
        print(f'The medians of this set are {nums[median_index]} and {nums[median_index2 ]}')
    else: #odd set of numbers
        median_index = len(nums) // 2 # index starts at 0
        print(f'The median is {nums[median_index]}')

def find_mode(nums):
    nums_dict = {}
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1
    nums_list = list(nums_dict.items())    #list of tuples
    nums_list.sort(key=lambda tup: tup[1], reverse=True) #sort by second item in each tuple
    mode_pair = []
    mode_pair_one = nums_list[0]
    for tup in nums_list:
        if tup[1] == mode_pair_one[1]:
            mode_pair.append(tup)
    for pair in mode_pair:
        mode = pair[0]
        count = pair[1]
        print(f'mode = {mode} (with a count of {count})')


nums = []
while True:
    new_num = input('Please enter a number, or type \'done\': ')
    if new_num == 'done':
        break
    nums.append(int(new_num))


find_average(nums)
find_median(nums)
find_mode(nums)