/*Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.*/

//logic 
 int maxSubarrayOfSizeK(int arr[],int k)
          {
              int sum=0,maxsum=0;
              
              for(int i=0;i<k;i++)
              {
                  sum=sum+arr[i];
              }
               
               maxsum=sum;
              
              for(int i=1;i<=arr.length-k;i++)
              {
                  sum=sum-arr[i-1]+arr[i+k-1];
                  maxsum=Math.max(sum,maxsum);
                  
              }
              return maxsum;
          }
