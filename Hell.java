import java.util.*;
public class Hell{
    public static void main(String []args){
        System.out.print("Enter the integer no which is to be converted into a binary no : ");  
        Scanner s = new Scanner(System.in);
        int j , n , i = 1;
        int bin_arr [] = new int [100];
        n = s.nextInt();
        while(n != 0){
            bin_arr[i++] = n % 2;
            n = n / 2 ;
        }
        System.out.println("THe Binary Number is :");
        for(j = i - 1 ; j > 0 ; j--){
            System.out.print(bin_arr[j]);
        }
    
        
        }
    }
