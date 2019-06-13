// Compile by cmd:
//   gcc -m32 -g -O0 test.c  -c -o test.o
//

void reverseArray(int arr[], int start, int end)
{
    while (start < end)
    {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}
