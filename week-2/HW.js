// 1
function calculate(min, max){
    var sum = 0;
    for (var i=min; i<=max; i++){
        sum += i;    
    } 
    console.log(sum);
}
    calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6 
    calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30

// 2
function avg(data){
    var [sum,count] = [0,0];
    var employee;
    for (const [key, value] of Object.entries(data)){
        if (key === "count"){
            count = parseInt(data[key]);
        }
        if (key === "employees"){
            employee = data[key];
        }
    }
    
    for (var i =0; i<count; i++){  
        for (var [key, value] of Object.entries(employee[i])){
            if (key === "salary"){
                var temp = employee[i];
                sum += parseInt(temp[key]);
            }
        } 
    }
    console.log(Math.round(sum / count));
}
    avg({
    "count":3,
    "employees":[ {
    "salary":30000 },
    {
    "name":"Bob",
    "salary":60000 },
    {
    "name":"Jenny",
    "salary":50000 }
    ]
    }); // 呼叫 avg 函式


// 3. using sorting approach
function maxProduct1(nums){  
    var arr1 = new Array();
    nums.sort(function( a , b){
        if(a > b) return 1;
        if(a < b) return -1;
        return 0;
    });
    if (nums.length < 2){
        console.log("The numbers are not in pairs.");
        return;
    }
    var num1 = nums[nums.length-1], num2 = nums[nums.length-2];
    var ans = num1*num2, temp = nums[0]*nums[1];
    if (ans < temp) {
        ans = temp;
    } 
    console.log(ans);
}  
// 3. not using sorting approach
function maxProduct(nums){  
    if (nums.length<2){
        console.log("The list is not in pairs");
        return;
    }
     
    var positive = [], negative = [];
    for (var i = 0; i<nums.length;i++){
        if (nums[i] >= 0){
            positive.push(nums[i]);
        }
        else{
            negative.push(nums[i]);
        }
    }
    

    if (positive.length === 0) {
        var num3 = negative[0], num4 = 1;
        for (var i = 0; i<negative.length;i++){
            var temp1 = Math.max(num3, num4);
            var temp2 = Math.min(num3, num4);
            if (negative[i]<temp1){
                num3 = temp2;
                num4 = negative[i];
            }
            
        }
        
        console.log(num3*num4);
        return;
    }
     
    else if (negative.length === 0){
        var num3 = positive[0], num4 = 1;
        for (var i = 0;i<positive.length;i++){
            var temp1 = Math.max(num3, num4);
            var temp2 = Math.min(num3, num4);
            if (positive[i]>temp2){
                num3 = positive[i];
                num4 = temp1;
            }      
        }      
        console.log(num3*num4);
        return;
    }
     
    else if (nums.length === 2){
        console.log(nums[0]*nums[1]);
        return;
    }
    
    else{
        var num1 = positive[0], num2 = 0, num3 = negative[0], num4 = 0;
        for (var i=0; i<positive.length-1;i++){
            var temp1 = Math.max(num1, num2);
            var temp2 = Math.min(num1, num2);
            if (positive[i+1]>temp2){
                num1 = positive[i+1];
                num2 = temp1;
            }  
            
        }
        
        var ans1 = num1*num2
        for (var i= 0 ;i<negative.length-1;i++){
            var temp1 = Math.max(num3, num4);
            var temp2 = Math.min(num3, num4);
            if (negative[i+1]<temp1){
                num3 = temp2;
                num4 = negative[i+1];
            }
             
        }
        
        var ans2 = num3*num4;
        if (ans1 > ans2){
            console.log(ans1);
        }
        
        else{
            console.log(ans2);
        }
           
    }
}
    maxProduct([5, 20, 2, 6]) // 得到 120 
    maxProduct([10, -20, 0, 3]) // 得到 30 
    maxProduct([-1, 2]) // 得到 -2 
    maxProduct([-1, 0, 2]) // 得到 0 
    maxProduct([-1, -2, 0]) // 得到 2

// 4
function twoSum(nums, target){
    //create object of type hash table
    const hash_table = {}; 
    for (var i = 0; i<nums.length;i++){
        hash_table[nums[i]]=i;
    }
    for (var i = 0; i<nums.length;i++){
        if ((target-nums[i]) in hash_table){
            if (hash_table[target-nums[i]] != i){
                return [i, hash_table[target-nums[i]]];
            }
        }
    }
}
let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9
