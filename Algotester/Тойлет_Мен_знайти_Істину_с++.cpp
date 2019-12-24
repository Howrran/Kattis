#include <bits/stdc++.h>
#include <iostream>
#define pb push_back

using namespace std;

vector<bool> v;
vector<vector<int> > g;

void edge(int a, int b)
{
    g[a].pb(b);

}

bool bfs(int u, int n)
{
    v.assign(n, false);
    queue<int> q;

    q.push(u);
    v[u] = true;

    while (!q.empty()) {

        int f = q.front();
        q.pop();

        //cout << f + 1<< " ";


        for (auto i = g[f].begin(); i != g[f].end(); i++) {
            if (!v[*i]) {
                q.push(*i);
                v[*i] = true;
            }
        }
    }
    for(int k = 0; k < n; k++){
        if( v[k] == false)
            return false;
    }
    return true;
}


int main()
{
    int n, e;
    cin >> n >> e;

    v.assign(n, false);
    g.assign(n, vector<int>());

    int a, b;
    for (int i = 0; i < e; i++) {
        cin >> a >> b;
        edge(a - 1, b - 1);
    }
    for(int i = 0; i < n; i++){
        //cout << v[i] << ' ';
    }
    //cout << endl;

    for (int i = 0; i < n; i++) {
            if (bfs(i, n)){
                cout << i + 1;
                return 0;
            }

    }
    cout << -1;

    return 0;
}
