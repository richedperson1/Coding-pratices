#include <iostream>
#include <string>
using namespace std;

string replaceSpaces(string &str){
	// Write your code here.
    int l = str.length();
    string rep = "@40";
    for(int i = 0; i<l ; i++)
    {
        if(str[i]==' ')
        {
            str.replace(i,1,rep);
        }
    }
    return str;
}

int main()
{
    string a;
    
    a = "rutvik jaiswal";
    cout<<"The new string is to be : "<<replaceSpaces(a)<<endl;
    return 0;
}