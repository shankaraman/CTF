//Challenge Name dump.exe
#include<iostream>
#include<cstdlib>
#include<string>
#include<ctime>
#include<conio.h>
#include<windows.h>
#include<vector>
void flag();
using namespace std;
int main()
{
    int guess=0,number=0,tries=0;
    cout << "*************************************************\n";
	cout << "****** Welcome to Number Guessing Game **********\n";
	cout << "*************************************************\n";
	cout << "Play this game to get your flag!\n";
	cout << "\nWell Good luck!\n\n";
	srand((int)time(NULL));
    guess = rand()%100+1;
    while (guess!=number)
    {

        cout<<"\nEnter a number between 1 and 100:";
        cin >> number;
        tries++;
        if (number > guess)
        {
             cout << "\nGuessed number is high!";
        }
        else if (number < guess)
        {
             cout << "\nGuessed number is low!";
        }
        else 
        {
             cout << "\nBravo! You found in "<<tries<<" tries";
             flag();
             break;
        }      
    }
    return 0;
}
                     

void flag()
{
    string tmp = "1768115a626910715a70141515771072645a69715a48545450141014",decoded="";
    vector<char> decrypt;
    for (int i=0;i<tmp.size();i++)
    {
        if (tmp[i] == 'a')
        {
            decrypt.push_back('f');
        }
        else if (tmp[i] == '1')
        {
            decrypt.push_back('3');
        }
        else
        {
            decrypt.push_back(tmp[i]);
        }
    }
    for(int i=0;i<decrypt.size();i++)
    {
        decoded+=decrypt[i];
    }    
    string FLAG;
    const char *c = decoded.c_str();
    unsigned int x;
    while(*c != 0) 
    {
        sscanf(c, "%2X", &x);
        decoded += x;
        c += 2;
    }
    for(int i=56;i<decoded.size();i++)
    {
            FLAG+=decoded[i];
    }
    cout <<"\nWell Congratzzz!!!! Here is your flag:\t"<<FLAG;
    Sleep(900000);
}
