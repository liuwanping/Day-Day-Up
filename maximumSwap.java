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


import java.util.ArrayList;


public class maximumSwap 
{
	public static void main(String[] args) 
	{
		
	}
	public int maximumSwap(int num) 
	{
		String s=new String(Integer.toString(num));
        int max=0;
        int min=0;
        int cur=0;
        int point=0;
        while (num%10!=0) 
        {
			cur=num%10;
			if(cur>max)
				max=point;
			if(cur<min)
				min=point;
			point++;
		}
        char temp;
        temp=s.charAt(min);
        
    }
}

