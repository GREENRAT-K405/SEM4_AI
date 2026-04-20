#include <iostream>
#include<bits/stdc++.h>

using namespace std;

class SocialNetwork {
    //This will give me adjacent nodes (direct neighbours/ friends)
    map<string, vector<string>> adj;

public:
    //fxn to add u follows these v
    void addEdge(string u, string v) {
        adj[u].push_back(v); 
    }

    // Helper to sort neighbors for consistent output
    void sortNeighbors() {
        for (auto& pair : adj) {
            sort(pair.second.begin(), pair.second.end());
        }
    }

    void BFS(string startNode) {
        set<string> visited;
        queue<string> q;

        visited.insert(startNode);
        q.push(startNode);

        cout << "BFS Traversal: ";
        while (!q.empty()) {
            string current = q.front();
            q.pop();
            cout << current << " -> ";

            for (string neighbor : adj[current]) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
    }

    void DFSUtil(string node, set<string>& visited) {
        visited.insert(node);
        cout << node << " -> ";

        for (string neighbor : adj[node]) {
            if (visited.find(neighbor) == visited.end()) {
                DFSUtil(neighbor, visited);
            }
        }
    }

    void DFS(string startNode) {
        set<string> visited;
        cout << "DFS Traversal: ";
        DFSUtil(startNode, visited);
        cout << "End (Other nodes unreachable)" << endl;
    }
};

int main() {
    SocialNetwork g;

    // --- Building the DIRECTED Graph ---

    // Sunil's Outgoing
    g.addEdge("Sunil", "Raj");
    g.addEdge("Sunil", "Sneha");
    g.addEdge("Sunil", "Akash");
    g.addEdge("Sunil", "Maya");


    // Raj's Outgoing
    // g.addEdge("Raj", "Akash");
    g.addEdge("Raj", "Neha");

    // Akash's Outgoing
    g.addEdge("Akash", "Sunil");
    g.addEdge("Akash", "Priya");
    // g.addEdge("Akash", "Neha (Center)");

    // Sneha's Outgoing
    g.addEdge("Sneha", "Akash");
    g.addEdge("Sneha", "Rahul");
    g.addEdge("Sneha", "Neha");
    g.addEdge("Sneha", "Maya");

    // Neha (Center)'s Outgoing
    g.addEdge("Neha (Center)", "Sneha");
    g.addEdge("Neha (Center)", "Akash");
    g.addEdge("Neha (Center)", "Aarav");
    g.addEdge("Neha (Center)", "Sneha");

    
    g.addEdge("Priya", "Raj");
    g.addEdge("Priya", "Akash");
    // g.addEdge("Priya", "Neha (Center)");
    g.addEdge("Priya", "Aarav");
    
    g.addEdge("Rahul", "Sneha");
    g.addEdge("Rahul", "Neha (Center)");
    g.addEdge("Rahul", "Neha (Right)");
    g.addEdge("Rahul", "Maya");
    g.addEdge("Rahul", "Pooja");
    g.addEdge("Rahul", "Arjun (Right)");

    g.addEdge("Neha (Right)", "Neha (Center)");
    g.addEdge("Neha (Right)", "Aarav");
    g.addEdge("Neha (Right)", "Priya");
    g.addEdge("Neha (Right)", "Arjun (Right)");
    g.addEdge("Neha (Right)", "Rahul");
    
    g.addEdge("Aarav", "Arjun (Right)");
    g.addEdge("Aarav", "Neha (Right)");
    g.addEdge("Aarav", "Neha (Center)");
    
    // g.addEdge("Arjun (Right)", "Pooja");
    g.addEdge("Arjun (Right)", "Rahul");
    g.addEdge("Arjun (Right)", "Aarav");
    g.addEdge("Arjun (Right)", "Neha (Right)");

    g.addEdge("Pooja", "Arjun (Bottom)");
    g.addEdge("Pooja", "Arjun (Right)");
    g.addEdge("Pooja", "Rahul");

    g.addEdge("Maya", "Arjun (Bottom)");
    g.addEdge("Maya", "Rahul");
    g.addEdge("Maya", "Sneha");
    g.addEdge("Maya", "Sunil");


    g.addEdge("Arjun (Bottom)", "Rahul");
    g.addEdge("Arjun (Bottom)", "Maya");
    g.addEdge("Arjun (Bottom)", "Pooja");


    // Sort for deterministic output
    g.sortNeighbors();

    cout << "Starting Directed Traversals from 'Sunil':\n" << endl;
    
    g.BFS("Sunil");
    cout << endl;
    g.DFS("Sunil");

    return 0;
}