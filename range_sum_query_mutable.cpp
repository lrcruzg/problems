#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/range-sum-query-mutable/

class SegmentTree {
private:
	vector<int> st;
	vector<int> nums;
	int n;

	int left(int p) { return p << 1; }

	int right(int p) { return (p << 1) + 1; }

	void build(int p, int l, int r) {
		if(l == r) {
			st[p] = nums[l];
			return;
		}

		int mid = l + (r - l) / 2;

		build(left(p) , l      , mid);
		build(right(p), mid + 1, r  );

		st[p] = st[left(p)] + st[right(p)];
	}

	int RSQ(int p, int l, int r, int l_query, int r_query) {
		if(r < l_query or r_query < l)  // [l, r] \cap [l_query, r_query] = \emptyset
			return 0;

		if(l_query <= l and r <= r_query)  // [l, r] \subseteq [l_query, r_query]
			return st[p];

		int mid = l + (r - l) / 2;
		return RSQ(left(p) , l      , mid, l_query, r_query) 
			 + RSQ(right(p), mid + 1, r  , l_query, r_query);
	}

	void update(int p, int l, int r, int new_value, int pos) {
		if(l == r) {
			nums[pos] = new_value;
			st[p] = new_value;
			return;
		}

		int mid = l + (r - l) / 2;

		if(pos <= mid)
			update(left(p) , l, mid, new_value, pos);
		else
			update(right(p), mid + 1, r, new_value, pos);

		st[p] = st[left(p)] + st[right(p)];
	}

public:
	SegmentTree(vector<int>& nums) {
		this->nums = nums;
		n = (int) nums.size();
		st.assign(4 * n, 0);
		build(1, 0, n - 1);
	}

	int RSQ(int l_query, int r_query) {
		return RSQ(1, 0, n - 1, l_query, r_query);
	}

	void update(int new_value, int pos) {
		update(1, 0, n - 1, new_value, pos);
	}
};

class NumArray {
public:
	SegmentTree* st;

	// O(n) time (segment tree build).
	// O(n) space (segment tree uses a 4n vector).
	NumArray(vector<int>& nums) {
		st = new SegmentTree(nums);
	}
	
	// O(log(n)) time.
	void update(int index, int val) {
		st->update(val, index);
	}
	
	// O(log(n)) time
	int sumRange(int left, int right) {
		return st->RSQ(left, right);
	}
};
