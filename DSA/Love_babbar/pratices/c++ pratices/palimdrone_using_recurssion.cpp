#include <iostream>
#include <string>
using namespace std;

bool string_man(string &s, int low, int high)
{
    if (low < high)
    {
        if (s[low] != s[high])
        {
            return false;
        }

        return string_man(s, low + 1, high - 1);
    }
    return true;
}
int main()
{
    string s;
    s = "jaj";
    int high = s.size();
    cout << string_man(s, 0, high - 1) << endl;
    if (string_man(s, 0, high - 1))
    {
        cout<<s<<" is palimdrome"<<endl;
    }

    else{
        cout<<s<<" is not palimdrome"<<endl;
    }
    
    return 0;
}
