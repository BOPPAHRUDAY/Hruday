/*Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.*/

public class solution
{
    public int LengthOfLongestSubstring(String s)
    {
        int a_pointer=0;
        int b_pointer=0;
        int max=Integer.MIN_VALUE;
        
        HashSet<String> h=new HashSet<String>();
        
        while(b_pointer<s.length())
        {
            if(!h.containts(s.charAt(b_pointer)
            {
                h.add(s.charAt(b_pointer);
                b_pointer++;
                max=Math.max(h.size(),max);
                
            }else{
                h.remove(s.charAt(a_pointer);
                a_pointer++;
            }
        }
        return max;
    }
}
