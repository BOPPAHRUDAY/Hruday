import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner s=new Scanner(System.in);
	    int n=s.nextInt();
	    int mod=(int)1e9+7;
	    int max=(int)1e6;
	    int dp[]=new int[max+1];
	    for(int i=1;i<=n;i++)
	    {
	        dp[i]=max;
	        int m=i;
	        while(m!=0)
	        {
	            dp[i]=Math.min(dp[i],1+dp[i-m%10]);
	            m=m/10;
	        }
	    }
	    System.out.println(dp[n]);
	}
}
