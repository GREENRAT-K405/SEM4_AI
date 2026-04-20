#include <bits/stdc++.h>
using namespace std;

map <string,vector<pair<string, int>>> graph = {
    {"Chicago", {{"Detroit", 283}, {"Cleveland", 345}, {"Indianapolis",182}}},
    {"Indianapolis", {{"Chicago",182}, {"Columbus",176}}},
    {"Columbus", {{"Indianapolis",176}, {"Cleveland",144}, {"Pittsburgh",185}}},
    {"Cleveland", {{"Chicago",345}, {"Detroit",169}, {"Columbus",144}, {"Pittsburgh",134}}},
    {"Detroit", {{"Chicago",283}, {"Cleveland",169}, {"Buffalo",256}}},
    {"Buffalo", {{"Detroit",256}, {"Cleveland",189}, {"Pittsburgh",215}, {"Syracuse",150}}},
    {"Pittsburgh", {{"Cleveland",134}, {"Columbus",185}, {"Buffalo",215}, {"Philadelphia",305}, {"Baltimore",247}}},
    {"Syracuse", {{"Buffalo",150}, {"New York",254}, {"Boston",312}}},
    {"New York", {{"Syracuse",254}, {"Philadelphia",97}, {"Boston",215}, {"Providence",181}}},
    {"Philadelphia", {{"New York",97}, {"Pittsburgh",305}, {"Baltimore",101}}},
    {"Baltimore", {{"Philadelphia",101}, {"Pittsburgh",247}}},
    {"Boston", {{"Syracuse",312}, {"New York",215}, {"Providence",50}, {"Portland",107}}},
    {"Providence", {{"Boston",50}, {"New York",181}}},
    {"Portland", {{"Boston",107}}}};


void BFS (string start, string goal){
    queue<pair<string, int>> q;
    map<string, bool> visited;
    map<string, string> parent;
    vector<pair<string, string>> bfsTree;

    q.push({start, 0});
    visited[start] = true;

    while(!q.empty()){
        // auto[city,cost]=q.front();
        pair<string,int> p=q.front();
        string city = p.first;
        int cost = p.second;
        q.pop();


        for (auto &neighbor : graph[city]) {
            if (!visited[neighbor.first]) {
                visited[neighbor.first] = true;
                parent[neighbor.first] = city;
                bfsTree.push_back({city, neighbor.first});
                q.push({neighbor.first, cost + neighbor.second});
            }
        }

         //terminating condition
        if(city==goal){
            vector<string> path;
            string cur = goal;
            int totalCost = cost;


            while(cur!= ""){
                path.push_back(cur);
                cur = parent[cur];
            }
            reverse(path.begin(), path.end());
            //reversed to get correct order

            cout << "\nBFS Path: ";
            for (int i = 0; i < path.size(); i++) {
                cout << path[i] << "-->";
            }
            cout << "END";

            cout << "\nTotal Step Cost: " << totalCost << " miles\n";
            
            cout << "\nBFS Tree Edges:\n";
            for(const auto& edge : bfsTree) {
                cout << edge.first << " -> " << edge.second << endl;
            }

            return;
        }
    }
}


void DFS(string start, string goal) {
    stack<pair<string, int>> st;
    map<string, bool> visited;
    map<string, string> parent;

    st.push({start, 0});

    while (!st.empty()) {
        // auto [city, cost] = st.top();
        pair<string,int> p=st.top();
        string city = p.first;
        int cost = p.second;
        st.pop();

        if (visited[city]) continue;
        visited[city] = true;

        if (city == goal) {
            vector<string> path;
            string cur = goal;

            while (cur != "") {
                path.push_back(cur);
                cur = parent[cur];
            }
            reverse(path.begin(), path.end());

            // Calculate actual path cost
            int totalCost = 0;
            for (int i = 0; i < path.size() - 1; i++) {
                for (auto &neighbor : graph[path[i]]) {
                    if (neighbor.first == path[i + 1]) {
                        totalCost += neighbor.second;
                        break;
                    }
                }
            }

            cout << "\nDFS Path: ";
            for (int i = 0; i < path.size(); i++) {
                cout << path[i] << "-->";
            }
            cout << "END";

            cout << "\nTotal Step Cost: " << totalCost << " miles\n";

            return;
        }

        for (auto &neighbor : graph[city]) {
            if (!visited[neighbor.first]) {
                parent[neighbor.first] = city;
                st.push({neighbor.first, cost + neighbor.second});
            }
        }
    }
}





    int main(){
        string startCity="Chicago";
        string goalCity = "New York";

        cout<< "Starting City: " << startCity <<endl;
        cout<<"Goal City: " << goalCity <<endl;

        BFS(startCity, goalCity);
        DFS(startCity, goalCity);

    return 0;


    }