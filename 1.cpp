#include<iostream>

using namespace std;

int main(){
    string s , s2;
    cin >> s2 >> s;
    bool flag = false;
    // for(int i = 0;i < s.size();i++){
    //     int cnt = 0;
    //     for(int j = 0;j < s2.size() ; j++){
    //         if(s[i+j] == s2[j]){
    //             cnt++;
    //         }
    //         if(cnt == s2.size()){
    //             flag = true;
    //             break;
    //         }
    //     }
    //     if(flag){
    //         break;
    //     }
    // }
int k = 0;
    for(int i = 0; i < s.size();i++){
        if(s[i] == s2[k]){
            k++;
        }else{
            i-=k;
            k = 0;
        }
        if(k == s2.size() ){
            flag =true;
            break;
        }
        // cout << k << " ";
    }

    if(flag){
        cout << "yes";
    }else cout << "no";



    return 0;
}