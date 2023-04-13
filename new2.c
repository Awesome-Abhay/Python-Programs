// HCF
#include<stdio.h>
int main()
{
    system("cls");
    int a,b;
    scanf("%d %d",&a,&b);
    int smaller=a;
    if(a<b)
    {
        if(b%a==0)
        {
            printf("%d\n",a);
            goto label1;
        }
    }
    else
    {
        smaller=b;
        if(a%b==0)
        {
            printf("%d\n",b);
            goto label1;
        }
    }
    int i=2; 
    int gcd=1;
    while(i<=smaller)
    {
        if(a%i==0 && b%i==0)
        {
            gcd=i;
        }
        i++;
    }
    printf("%d",gcd);
    label1:
     {

     }
    return 0;
}