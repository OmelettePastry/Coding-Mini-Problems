import java.util.ArrayList;

public class Hailstone
{
    public static ArrayList<Integer> sequence (int number)
    {
        return sequenceHelper (new ArrayList<Integer>(), number);
    }
    
    public static ArrayList<Integer> sequenceHelper(ArrayList<Integer> sequenceList, int number)
    {
        if (number == 1)
        {
            sequenceList.add(number);
            return sequenceList;
        }
        
        sequenceList.add(number);
        
        if (number % 2 == 0)
            return sequenceHelper(sequenceList, number / 2);
        else
            return sequenceHelper(sequenceList, (3 * number) + 1);
    }
    
    public static void main (String args[])
    {
        int number = 27;
        System.out.println(sequence(number).toString());
    }
}
        
        