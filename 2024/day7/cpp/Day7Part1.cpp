#include <vector>
#include <string>
#include <fstream>
#include <iostream>

using namespace std;

vector<string> readFileData(string path) {
    ifstream file(path);
    vector<string> data;
    string line;
    while(getline(file, line)){
        data.push_back(line.substr(':'));
        data[data.size() - 1].erase(data[data.size() - 1].end() - 1);
        cout << data[data.size() - 1] << endl;
    }

    return data;
}

int main() {
    readFileData("../../input.txt");
}