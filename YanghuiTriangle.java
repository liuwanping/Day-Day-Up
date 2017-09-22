public class YanghuiTriangle {
	public static void main(String[] args) {
		triangle(6);
	}
	public static void triangle(int lines)
	{
		int t[][]=new int[lines][];

		t[0]=new int[1];
		t[0][0]=1;
		
		for (int i = 1; i < t.length; i++) 
		{
			t[i]=new int[t[i-1].length+1];
			t[i][0]=1;
			for (int j = 1; j < t[i].length-1; j++) 
			{
				t[i][j]=t[i-1][j-1]+t[i-1][j];
			}	
			t[i][t[i].length-1]=1;
		}
		for (int i = 0; i < t.length; i++) 
		{
			for (int j = 0; j < t[i].length; j++) 
			{
				System.out.print(t[i][j]+" ");
			}
			System.out.println();
		}
	}
}
