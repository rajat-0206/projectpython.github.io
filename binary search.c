#include<stdio.h>
int main()
{
    int arr[10],m,n,i,flag=0,beg,mid,end;
printf("Enter the size of the array\n");
scanf("%d",&m);
printf("Enter elements in the array\n");
for(i=0;i<m;i++)
    scanf("%d",&arr[i]);
printf("Enter the element to be searched\n");
scanf("%d",&n);
beg=0;
end=m-1;
while(beg<=end)
{
    mid=(beg+end)/2;
    if(arr[mid]==n)
    {
        flag=1;
        break;
    }
    else
    {

     if(n>mid)
        beg=mid+1;
    else
        end=mid-1;
    }
    }
if(flag)
    printf("Element found at position %d",mid+1);
else
    printf("Elements not found");
}
