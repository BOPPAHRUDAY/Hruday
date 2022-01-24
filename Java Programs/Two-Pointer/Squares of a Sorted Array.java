
//normal approach

class Solution {
    public int[] sortedSquares(int[] nums) {
       for(int i=0;i<=nums.length-1;i++){
              nums[i]=(int)Math.pow(nums[i],2);
       }
        
        Arrays.sort(nums);
        return nums;    
    }
}

//divide and conquer approach

class Solution {
    public int[] sortedSquares(int[] nums) {
        
        int res[]=new int[nums.length];
        int start=0;
        int end=nums.length-1;
        
        for(int i=nums.length-1;i>=0;i--){
            
            if(Math.abs(nums[start])>=Math.abs(nums[end])){
                
                res[i]=nums[start]*nums[start];
                start++;
            }else{
             res[i]=nums[end]*nums[end];
                end--;
                
            }
        }
        return res;
    }
}

