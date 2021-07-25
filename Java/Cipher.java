public class Cipher
{
    public static String encXOR(String pass, String pString)
    {
        int passIndex = 0;
        String encodedText = "";
        
        for (int a = 0; a < pString.length(); a++)
        {
            encodedText += (char) (pass.charAt(passIndex) ^ pString.charAt(a));
            passIndex++;
            
            if (passIndex >= pass.length())
                passIndex = 0;
        }
        
        return encodedText;
    }
    
    public static void main (String args[])
    {
        String text = "Hello. How are you?";
        String password = "Ankara";
        
        String encodedText = encXOR(password, text);
        System.out.println(encodedText);
        
        String decodedText = encXOR(password, encodedText);
        System.out.println(decodedText);
    }
    
}