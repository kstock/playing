#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
/**
 * playing with C and higher order functions
 */

/*
 * TODO: must be some clever type subversion hack to get more
 * general types, look into
 */
typedef int (*int1_f)(int a);
typedef int (*int2_f)(int a,int b);

/*
 * HOFS
 * map, filter, foldl
 */


/** takes array and function, applies function to each element of the array
 *
 *[1,2,3..] -> [f(1),f(2),f(3)..]
 */
int *map(int *numbers, int count, int1_f f)
{
    int *target = malloc(count * sizeof(int));
    int i;
    for ( i = 0; i < count; i++)
    {
        target[i] = f(numbers[i]);
    }

    for( i = 0; i < count; i++) {
        printf("%d ", target[i]);
    }

    printf("\n");


    return target;
}


/* filter function, takes array and int->boolean(well, int ->int)
 * function, returns list of only elements that is true for*/
int *filter(int *numbers, int count, int1_f f)
{
    int i;
    int *target;
    int *targetSize;
    int num_pass = 0;

    //copy so can't destroy input
    //if destroying input didn't matter could just overwrite it
    //i.e, numbers[num_pass] = numbers[i];
    target = malloc(count * sizeof(int));
    for( i = 0; i < count; i++) {
        target[i] = numbers[i];
    }


    for ( i = 0; i < count; i++)
    {
        if (  f( numbers[i] )  ){
            target[num_pass] = numbers[i];
            num_pass += 1;
        }
    }

    targetSize = malloc(num_pass * sizeof(int));
    for( i = 0; i < num_pass; i++) {
        targetSize[i] = numbers[i];
        printf("%d ", targetSize[i]);
    }

    printf("\n");


    return targetSize;
}


int foldl(int *numbers,int count,int2_f f, int acc) {
    int i;
    for (i = 0; i < count; i++){
        acc = f(acc, numbers[i]);
    }

    printf(" %d \n",acc);
    return acc;
}

/*
 * functions to pass into HOFs
 */



int times2(int a)
{
    return 2 * a;
}

int isOdd(int a)
{
    return a % 2;
}

int isEven(int a){

    return !(a % 2);
}

int add(int a,int b){

    return a + b;
}

int multiply(int a,int b){

    return a * b;
}


/*
 * test
 */

int main(int argc, char **argv){

    if(argc < 2){
        printf("USAGE: functionalC 4 3 1 5 6\n");
        exit(1);
    }

    int count = argc - 1;
    int i = 0;
    char **inputs = argv + 1;

    int *numbers = malloc(count * sizeof(int));
    if(!numbers){
        printf("Memory error.");
        exit(1);
    }

    printf("the original array is : ");
    for(i = 0; i < count; i++) {
        numbers[i] = atoi(inputs[i]);
        printf(" %s ",inputs[i]);
    }
    printf("\n\n");

    printf("Now using map *2:        ");
    map(numbers,count,times2);
    printf("Now using map isEven:    ");
    map(numbers,count,isOdd);
    printf("Now using map isOdd:     ");
    map(numbers,count,isEven);

    printf("\n\n");

    printf("Now using filter isOdd:  ");
    filter(numbers,count,isOdd);
    printf("Now using filter isEven: ");
    filter(numbers,count,isEven);

    printf("\n\n");

    printf("Now using fold +,(sum):  ");
    foldl(numbers,count,add,0);
    printf("Now using fold*,(prod):  ");
    foldl(numbers,count,multiply,1);


    free(numbers);

    return 0;
}
