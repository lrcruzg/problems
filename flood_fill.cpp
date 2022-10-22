#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/flood-fill/

class Solution {
public:
	// O(m * n) time.
	// O(m + n) space.
	// where n = len(image), m = len(image[0])
	vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
		vector<vector<bool>> visited(image.size(), vector<bool>(image[0].size(), false));
		vector<vector<int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

		int starting_color = image[sr][sc];

		queue<pair<int, int>> q;
		q.push(make_pair(sr, sc));

		while(not q.empty()) {
			auto[i, j] = q.front();
			q.pop();
			visited[i][j] = true;
			image[i][j] = color;
			for(auto d : directions) {
				if(is_valid(i + d[0], j + d[1], image, visited, starting_color))
					q.push({i + d[0], j + d[1]});
			}
		}

		return image;
	}

	bool is_valid(int i, int j, vector<vector<int>>& image, vector<vector<bool>>& visited, int starting_color) { 
		return 0 <= i and i < image.size() and 0 <= j and j < image[0].size() and image[i][j] == starting_color and not visited[i][j];
	}
};
