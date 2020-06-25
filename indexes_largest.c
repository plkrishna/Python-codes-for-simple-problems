#include <stdio.h>
#include<stdlib.h>
int main(void) {
int t,i,n=20,max_index=0;
int a[2000000]={21,13,1,2,15,17,12,13,11,4,6,14,16,19,9,32,21,6,4,5};
/*for(i=0;i<n;i++)
a[i]=rand()%20000000;*/
for(i=0;i+2<n;i=i+2)
{
   if(a[i]>a[i+1]&&a[i]>a[i+2])
       if(a[max_index]>=a[i])
	       max_index=i;
   else if(a[i+1]>a[i+2])
	   if(a[max_index]>=a[i+1])
		   max_index=i;
   else if(a[max_index]>=a[i+2])
          max_index=i+2;	   
}
t=a[max_index];
a[max_index]=a[i-2];
a[i-2]=t;
if((n-1)%2!=0)
   if(a[n-2]>a[n-1])
   {
       t=a[n-2];
       a[n-2]=a[n-1];
       a[n-1]=t;
   }
printf("Max:%d",a[n-2]);
return 0;
}
