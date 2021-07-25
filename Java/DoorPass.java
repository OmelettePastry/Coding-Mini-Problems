import java.util.Arrays;

public class DoorPass
{
    public static final boolean open = true;
    public static final boolean closed = false;

    private boolean doorHall[];

    public DoorPass()
    {

    }

    public DoorPass(int numDoors)
    {
        doorHall = new boolean[numDoors];
        Arrays.fill(doorHall, false);
    }

    public void openDoors(int numOpenDoors)
    {
        for(int i = 1; i <= doorHall.length; i++)
        {

            System.out.println(i);
            int doorCounter = i - 1;

            while(doorCounter < doorHall.length)
            {
                doorHall[doorCounter] = !doorHall[doorCounter];
                doorCounter += i;
            }
        }
    }

    public String toString()
    {

        String string = "";
        String indexOpen = "";

        for(int j = 0; j < doorHall.length; j++)
        {
            if(doorHall[j] == true)
            {
                string += "[]";
                indexOpen += String.valueOf(j + 1) + " ";
           }
            else
                string += "X";
        }

        String fullString = string + "\n" + indexOpen;
        return fullString;
    }

}