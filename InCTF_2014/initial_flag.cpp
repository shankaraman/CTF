//Challenge name dump.exe
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int fn(int);
int main()
{
    cout << "*************************************************\n";
	cout << "****** Welcome to Number Guessing Game **********\n";
	cout << "*************************************************\n";
	cout << "Play this game to get your flag!\n";
	cout << "Well Good luck!\n\n";
	int num, guess, tries = 0,status=0;
	string secret = "Y0U_D353RV3_TH1S_FL4G";
	srand(time(0)); //seed random number generator
	num = rand() % 100 + 1; // random number between 1 and 100
	cout << "Guess My Number Game\n\n";
	do
	{
		cout << "Enter a guess between 1 and 100 : ";
		cin >> guess;
		tries++;
		if (guess > num)
			cout << "Too high!\n\n";
		else if (guess < num)
			cout << "Too low!\n\n";
		else
		{
			cout << "\nCorrect! You got it in " << tries << " guesses!\n"<<"And your flag:"<<secret;
        }
	} while (guess != num);

	cin.ignore();
	cin.get();
	return 0;
}
