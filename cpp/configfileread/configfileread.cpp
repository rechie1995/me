#include <iostream>
#include <fstream>

using namespace std;

string filepath;
int ConfigFileRead();

int main(int argc, char const *argv[])
{
    /* code */
    ConfigFileRead();
    cout << filepath << endl;
    return 0;
}

int ConfigFileRead(){
    ifstream configFile;
    string path = "./setting.conf";
    configFile.open(path.c_str());
    string str_line;
    if(!configFile.is_open()){
        cout << "Cannot open config file!!!" << endl;
        return 0;
    }
    while(!configFile.eof()){
        getline(configFile, str_line);
        if(str_line.compare(0,1,"#")==0){
            continue;
        }
        size_t pos = str_line.find('=');
        string str_key = str_line.substr(0, pos);
        if(str_key == "filepath"){
            filepath = str_line.substr(pos+1);
        }
    }
}