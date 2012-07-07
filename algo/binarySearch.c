#include <stdio.h>

int binSearch(int arr[],int length, int lookFor);

//test!
int main(int argc,char *argv[])
{

  int arr[7];
  int i = 0;

  for(i = 0; i < sizeof(arr)/sizeof(arr[0]);i++)
  {
    arr[i] = i;
  }

  printf("looking for 0 in [0..6] == %d \n",binSearch(arr,sizeof(arr)/sizeof(arr[0]),0));
  printf("looking for 1 in [0..6] == %d \n",binSearch(arr,sizeof(arr)/sizeof(arr[0]),1));
  printf("looking for 2 in [0..6] == %d \n",binSearch(arr,sizeof(arr)/sizeof(arr[0]),2));
  printf("looking for 3 in [0..6] == %d \n",binSearch(arr,sizeof(arr)/sizeof(arr[0]),3));
  printf("looking for 4 in [0..6] == %d \n",binSearch(arr,sizeof(arr)/sizeof(arr[0]),4));
  printf("looking for 5 in [0..6] == %d \n",binSearch(arr,sizeof(arr)/sizeof(arr[0]),5));
  printf("looking for 6 in [0..6] == %d \n",binSearch(arr,sizeof(arr)/sizeof(arr[0]),6));
  printf("looking for 10 in [0..6] == %d \n",binSearch(arr,sizeof(arr)/sizeof(arr[0]),10));

  return 0;
}



int binSearch(int arr[], int length, int lookFor)
{

  int begin = 0;
  int middle;
  int end = length;
    
    while(begin <= end )
    {	
      middle = begin + (int)(((end - begin)/2));
      //printf("begin=%d\nmiddle = %d\nend = %d\n\n\n",begin,middle,end);

      if (lookFor == arr[middle])
      {
        return middle;
      }
      else if (lookFor > arr[middle])
      {
        begin = middle + 1;
      }
      else 
      {
        end = middle -1;
      }

    }//end while 
  return -1;
}
