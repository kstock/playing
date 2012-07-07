/*

PURPOSE:
    Prints prime numbers <=n,
    as well as the time in milliseconds it took to compute!

USAGE:
      java Sieve_of_Erastosthenes [integer]

      If no number is specified, it will default to n=100
      If non-integer input is given, it will default to n=0 and
        print an error message
            

SPACE COMPLEXITY:

    Requires O(n) space! : / 

    large numbers might break it!

    On my macbook:
    java Sieve_of_Erastosthenes 61838635
    Printing primes 2..61838635
    ...
    It took about 2135 milliseconds to compute these!

    java Sieve_of_Erastosthenes 61838636
    Printing primes 2..61838636
    Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
      at Sieve_of_Erastosthenes.main(Sieve_of_Erastosthenes.java:45)


TIMING NOTE:

    Timing only takes into account the sieve algorithm code,
    not the array creation or anything.

    For comparison:

    java Sieve_of_Erastosthenes 61838635
    It took about 2135 milliseconds to compute these!//without array creation
    It took about 2183 milliseconds to compute these!//with array creation


MORE INFO:
    http://en.wikipedia.org/wiki/Sieve_of_Erastosthenes
*/

public class Sieve_of_Erastosthenes{

  /*
  having the array store the even numbers is a waste of space,
  because there is only 1 even prime!


  

  */
  public static int indexToNum(int index){
    

  }//end public static int indexToNum(int index){


  public static int numToIndex(int num){
    if (num % 2 == 0)
      return null;
    else
    {
      return 1 + num / 2;
    }


   }

  public static void main(String[]args){
    boolean[] sieve;
    long timing;

// default values!
    int n = 100;
    int sqrtN = 10;

    if (args.length == 0)
    {
      System.out.println("Specify a number to print primes up to that number!");
      System.out.println( String.format ("EX:%s\n%s\n%s\n%s\n%s\n%s\n%s\n\n",
        "java Sieve_of_Erastosthenes 10",
        "Printing primes 2..10!",
        "2",
        "3",
        "5",
        "7",
        "It took about 0 milliseconds to compute these!") );
      
      
      System.out.println("Defaulting to 2..100");

    }
    else
    {
      try
      {
        n = Integer.parseInt(args[0]) ;
      }
      catch(NumberFormatException e)
      {
        System.out.println("input must be an integer!");  
        n = 0;
      }

      sqrtN = 1 + (int)Math.sqrt(n);
      System.out.println("Printing primes 2.." + n);
    }

    
    timing = System.currentTimeMillis();
    sieve = new boolean[n+1];//+1 to map index->num

    //actualy sieve algorithm!
    for(int i = 2;i < sqrtN; i++)
    {
      if (sieve[i] == false)
      {
        for (int j = i*i; j < n; j = j + i)
        {
          sieve[j] = true;
        }//end inner for!
      }//end if sieve is false
    }//end outer for

  timing = System.currentTimeMillis() - timing;


  //edge case println for n == 2
  if (n == 2)
  {
    System.out.println(2);
  }

  //The indices set to false are primes!! 
  for (int i = 2; i < n; i++)
  {
      if(sieve[i] == false)
      {
          System.out.println(i);
      }
  }//end print out primes!

  System.out.println("It took about "+ timing + " milliseconds to compute these!");

  }//end public static void main(){
} //end public class Sieve{
