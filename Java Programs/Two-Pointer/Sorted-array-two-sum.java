/*using Binary Search*/


class Solution {
    public int[] twoSum(int[] nums, int target) {
        int start=0,sum=0;
        int end=nums.length-1;
        int a[]=new int[2];
        while(start<end)
        {
            sum=nums[start]+nums[end];
            
            if(sum==target)
            {
               if(start!=end)
               {  
                a[0]=start;
                a[1]=end;
                break;
               }
            }
            if(sum<target)
            {
             start++;   
            }else
            {
                end--;
            }  
        }
        return a;
    }
}
