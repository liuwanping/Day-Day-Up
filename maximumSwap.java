//Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.
//
//Example 1:
//Input: 2736
//Output: 7236
//Explanation: Swap the number 2 and the number 7.
//Example 2:
//Input: 9973
//Output: 9973
//Explanation: No swap.
//Note:
//The given number is in the range [0, 108]

public class maximumSwap 
{
	public static void main(String[] args) 
	{	
		System.out.print(maximumSwap(9973));
	}
	public static int maximumSwap(int num) 
	{
        char numArray[]=String.valueOf(num).toCharArray();
     
        int max = num;
        
        for(int i=0;i<numArray.length;i++)
        {
        	for (int j = i+1; j < numArray.length; j++) 
        	{
				char tmp1=numArray[i];
				numArray[i]=numArray[j];
				numArray[j]=tmp1;
				int tmp2=Integer.parseInt(new String(numArray));
	        	if(tmp2>max)
	        		max=tmp2;
				numArray[j]=numArray[i];
				numArray[j]=tmp1;        		
			}      	
        }
        
		return max;
    }
}

