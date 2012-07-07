function Sieve_of_Erastosthenes()
{


var n=16,i,j;
var sqrtN= Math.sqrt(n);
var sieve = new Array(n+1);
var primes="";

//actualy sieve algorithm!
  for(i = 2;i < sqrtN; i++)
  {
    if (sieve[i] == undefined)
    {
      for (j = i*i; j < n; j = j + i)
      {
        sieve[j] = true;
      }//end inner for!
    }//end if sieve is false
  }//end outer for
  
  for(i = 2;i < n; i++)
  {
    if (sieve[i] == undefined)
    {
      primes += String(i) + ", ";
    }
  }

document.getElementById("display").innerHTML= primes//"hello world";
}
