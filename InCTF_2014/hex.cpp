//Challenge name dump.exe
#include<iostream>
#include<cstring>
#include<string>
#include<stdio.h>
using namespace std;
int main()
{
    string tmp="3768335f626930735f70343535773072645f69735f48545450343034";
    string flag;
    const char *c = tmp.c_str();
    unsigned int x;
    while(*c != 0) {
        sscanf(c, "%2X", &x);
        tmp += x;
        c += 2;
        }
    for(int i=56;i<tmp.size();i++)
    {
            flag+=tmp[i];
    }
    cout <<"\nWell Congratzzz!!!! Here is your flag:"<<flag;

}
