"""
1. 在函式中使用迴圈計算最小值到最大值之間，所有整數的總和。
"""

def calculate(min, max): # 請用你的程式補完這個函式的區塊
    sum = 0
    for i in range(min,max+1):
        sum += i
    print (sum)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6 
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

"""
2. Python 字典與列表、JavaScript 物件與陣列 完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
"""

def avg(data):
    sum = 0    
    for key,value in data.items():
        if key == "employees":
            employee = data[key]
            for item in employee:
                sum += item['salary'] 
    print(round(sum/ int(list(data.values())[0])))

# 呼叫 avg 函式
avg({
    "count":3, 
    "employees":[{"name":"John","salary":30000 },
    {"name":"Bob","salary":60000},
    {"name":"Jenny","salary":50000}]
    }) 

"""
3. 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。 
提醒:請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。
"""
def maxProduct(nums):

    if len(nums)<2:
        print ("The list is not in pairs") 
        return
   
    positive, negative = [], []
    for i in range(len(nums)):
        if nums[i] >= 0:
            positive.append(nums[i])
        else:
            negative.append(nums[i])

    if not positive:
        num3, num4 = negative[0], 1
        for i in range(len(negative)):
            temp1 = max(num3, num4)
            temp2 = min(num3, num4)
            if negative[i]<temp1:
                num3 = temp2
                num4 = negative[i]
        print (num3*num4)
        return
    elif not negative:
        num3, num4 = positive[0], 1
        for i in range(len(positive)):
            temp1 = max(num3, num4)
            temp2 = min(num3, num4)
            if positive[i]>temp2:
                num3 = positive[i]
                num4 = temp1
        print (num3*num4)
        return
    elif len(nums) == 2:
        print (nums[0]*nums[1])
        return
    else:
        num1, num2, num3, num4 = positive[0], 0, negative[0], 0
        for i in range(len(positive)-1):
            temp1 = max(num1, num2) 
            temp2 = min(num1, num2) 
            if positive[i+1]>temp2:  
                num1 = positive[i+1] 
                num2 = temp1 
        ans1 = num1*num2
        for i in range(len(negative)-1):
            temp1 = max(num3, num4)
            temp2 = min(num3, num4)
            if negative[i+1]<temp1:
                num3 = temp2
                num4 = negative[i+1]
        ans2 = num3*num4
        if ans1 > ans2:
            print (ans1)
        else:
            print (ans2)

maxProduct([5, 20, 2, 6]) # 得到 120 
maxProduct([10, -20, 0, 3]) # 得到 30 
maxProduct([-1, 2]) # 得到 -2 
maxProduct([-1, 0, 2]) # 得到 0 
maxProduct([-1, -2, 0]) # 得到 2

"""
4. Given an array of integers, show indices of the two numbers such that they add up to a specific target. You can assume that each input would have exactly one solution, and you can not use the same element twice.
"""
def twoSum(nums, target):
    hash_table={} 
    for i in range(len(nums)): # build a hash table   
        hash_table[nums[i]]=i 
    for i in range(len(nums)):
        if (target-nums[i]) in hash_table: # see if these two value exist
            if hash_table[target-nums[i]] != i: # when the other number is of different index
                return [i, hash_table[target-nums[i]]]
            

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

"""
5. 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大
長度。 提醒:請勿更動題目中任何已經寫好的程式。
"""
def maxZeros(nums):
        start, end = 0, 0 # index of 1 displayed 
        count = 0 # the number of 1 showing up
        maxLength = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if (nums[0] == 0 and count % 2 != 0):
                    maxLength = i
                    start = i
                if (count % 2 == 0): # a pair of 1
                    end = i
                    temp = end - start - 1
                    if (maxLength < temp):
                        maxLength = temp
                    start = end
                else:
                    start = i
            
            elif (count % 2 != 0 and i == (len(nums)-1)): # the list is finished the iteration  
                temp = len(nums)-1 - start
                if (maxLength < temp):
                    maxLength = temp
            elif (count == 0 and i == (len(nums)-1)):
                maxLength = len(nums)
        print(maxLength)  
        

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4 
maxZeros([1, 1, 1, 1, 1]) # 得到 0 
maxZeros([0, 0, 0, 1, 1]) # 得到 3