/*Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.

Return 0 if no such subarray exists.*/

class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        
        int minl=Integer.MAX_VALUE;
        int start=0;
        int sum=0;
        
        for(int i=0;i<=nums.length-1;i++) 
            {
            sum=sum+nums[i];
            
            while(sum>=target) 
                {
                minl=Math.min(minl, i+1-start) ;
                
               sum=sum-nums[start];
                start++;
               }
            
            }
        if(minl==Integer.MAX_VALUE) 
            return 0;
        else 
            return minl;
        
    }
}
