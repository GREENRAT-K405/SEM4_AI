#include <iostream>
#include <bits/stdc++.h>

using namespace std;

const vector<int> GOAL_STATE = {0,1,2,3,4,5,6,7,8};
// using State = vector<int>;

int findZero(const vector<int>& state){
    for (int i=0;i<9;i++){
        if(state[i]==0) return i;
    }
    return -1;
}

bool tryMove(const vector<int>& current, vector<int>& next, int direction ){
    int zeroIndex = findZero(current);
    int row = zeroIndex / 3;
    int col = zeroIndex % 3;

    int newRow = row;
    int newCol = col;

    if (direction == 0) newRow--;       // Up
    else if (direction == 1) newRow++;  // Down
    else if (direction == 2) newCol--;  // Left
    else if (direction == 3) newCol++;  // Right

    if (newRow>=0 && newRow<3 && newCol>=0 && newCol<3){
        next = current;
        int newIdx = newRow * 3 + newCol;
        swap(next[zeroIndex], next[newIdx]); // Swap empty tile with target
        return true;
    }
    return false;
}

void solveBFS(const vector<int>& startState) {
    queue<vector<int>> q;
    set<vector<int>> visited;

    q.push(startState);
    visited.insert(startState);

    int statesExplored = 0;
    bool found = false;

    cout << "Starting BFS search..." << endl;

    while (!q.empty()) {
        vector<int> current = q.front();
        q.pop();
        
        // Count this state as explored
        statesExplored++;

        // Check if we reached the goal
        if (current == GOAL_STATE) {
            found = true;
            break;
        }

        // Generate neighbors (Up, Down, Left, Right), i will compute all possible neighbours
        for (int i = 0; i < 4; i++) {
            vector<int> nextState;
            if (tryMove(current, nextState, i)) {
                // add to queue if not visited
                if (visited.find(nextState) == visited.end()) {
                    visited.insert(nextState);
                    q.push(nextState);
                }
            }
        }
    }
    int BFS_states = statesExplored;

    if (found) {
        cout << "Goal Reached!" << endl;
        cout << "Total states explored: " << BFS_states << endl;
    } else {
        cout << "Goal not reachable." << endl;
    }
}

struct Node {
    vector<int> state;
    int depth;
};

void solveDFS(const vector<int>& startState) {
    const int MAX_DEPTH = 47;
    stack<Node> s;
    set<vector<int>> visited;

    s.push({startState,0});
    visited.insert(startState);

    int statesExplored = 0;
    bool found = false;
    int finalDepth =0;

    cout << "Starting DFS (Max Depth:"<<MAX_DEPTH<<") search..." << endl;

    while (!s.empty()) {
        Node current = s.top();
        s.pop();
        
        // Count this state as explored
        statesExplored++;

        // Check if we reached the goal
        if (current.state == GOAL_STATE) {
            found = true;
            finalDepth=current.depth;
            break;
        }

        // Generate neighbors (Up, Down, Left, Right)
        if(current.depth<MAX_DEPTH)
        {
            for (int i = 0; i < 4; i++) {
            vector<int> nextState;
            if (tryMove(current, nextState, i)) {
                // If we haven't visited this state before, add to queue
                if (visited.find(nextState) == visited.end()) {
                    visited.insert(nextState);
                    s.push(nextState);
                }
            }
        }}
    }
    int DFS_states = statesExplored;

    if (found) {
        cout << "Goal Reached!" << endl;
        cout << "Solution Depth (Moves): " << finalDepth << endl;
        cout << "Total states explored: " << statesExplored << endl;
    } else {
        cout << "Goal not found within depth limit of " << MAX_DEPTH << "." << endl;
        cout << "Total states explored: " << statesExplored << endl;
    }
}

int main(){
    vector<int> startState = {7, 2, 4, 5, 0, 6, 8, 3, 1};
    
    solveBFS(startState);
    cout << endl;
    solveDFS(startState);

    return 0;
}