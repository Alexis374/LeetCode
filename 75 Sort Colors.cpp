/*
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.


Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
*/
//常规解法：
class Solution {
public:
    void sortColors(int A[], int n) {
        int n_0=0,n_1=0,n_2=0;
        for(int i=0;i<n;i++){
            if(A[i]==0)n_0++;
            else if(A[i]==1)n_1++;
            else n_2++;
        }
        for(int i=0;i<n_0;i++)
            A[i]=0;
        for(int i=0;i<n_1;i++)
            A[n_0+i]=1;
        for(int i=0;i<n_2;i++)
            A[n_0+n_1+i]=2;
    }
};
//进阶解法，遍历数组，若为0，则放到前面，若为2，则放到后边,若要赋值的位置是1，则要与该位置交换
