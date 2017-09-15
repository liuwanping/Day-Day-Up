//Given an unsorted array of integers, find the length of longest continuous increasing subsequence.
//
//Example 1:
//Input: [1,3,5,4,7]
//Output: 3
//Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
//Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
//Example 2:
//Input: [2,2,2,2,2]
//Output: 1
//Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
//Note: Length of the array will not exceed 10,000.
public class findLengthOfLCIS 
{
	public static void main(String[] args) 
	{
		int nums[]={1,3,2,3,4,7};
//		int nums[]=new int[5];
		System.out.println(another_findLengthOfLCIS(nums));
	}
	 public static int findLengthOfLCIS(int[] nums) 
	 {
		 if(nums.length==0)
			 return 0;
		 if(nums.length==1)
			 return 1;
		 int count=1;
		 int length=1;	
		 int a=0;
         for(int i=0;i<(nums.length-1);i++)
         {
        	 if(nums[i+1]>nums[i])
        		 count++;
        	 else
        	 {
        		 length=length>count?length:count;
        		 count=1;
        	 }
         }        
		 return length>count?length:count;
	 }
	 public static int another_findLengthOfLCIS(int[] nums) 
	 {
		 int count=0;
		 int length=0;	
         for(int i=0;i<nums.length;i++)
         {
        	 if(i==0||nums[i]<=nums[i-1])
        		 count=0;
        	 length=Math.max(++count, length);
         }        
		 return length;
	 }
}








