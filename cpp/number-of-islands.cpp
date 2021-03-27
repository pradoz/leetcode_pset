// using DFS
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty() or grid[0].empty()) {
            return 0;
        }

        int count = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == '1') {
                    ++count;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }

private:
    void dfs(vector<vector<char>>& grid, int i, int j) {
        // Mark the cell as seen
        grid[i][j] = '#';

        // Bounds check, if we find '1', call dfs
        // Check above/below
        if (i > 0 and grid[i-1][j] == '1') {
            dfs(grid, i-1, j);
        }
        if (i < grid.size()-1 and grid[i+1][j] == '1') {
            dfs(grid, i+1, j);
        }

        // Check left/right
        if (j > 0 and grid[i][j-1] == '1') {
            dfs(grid, i, j-1);
        }
        if (j < grid[0].size()-1 and grid[i][j+1] == '1') {
            dfs(grid, i, j+1);
        }
    }
};


// Using BFS
class Solution {
public:
    struct Point {
        int row, col;
        Point(int _x, int _y) : row(_x), col(_y) {}
    };

    int nr_row, nr_col;
    int numIslands(vector<vector<char> > &grid) {
        if (grid.empty() or grid[0].empty()) {
            return 0;
        }

        nr_row = grid.size();
        nr_col = grid[0].size();

        int count = 0;
        queue<Point> q;
        
        for (int i = 0; i < nr_row; ++i) {
            for (int j = 0; j < nr_col; ++j) {
                if (grid[i][j] == '0') {
                    continue;
                }
                ++count;

                // push the Point onto the queue
                grid[i][j] = '0';
                q.push(Point(i, j));
                while (!q.empty()) {
                    Point point = q.front();
                    q.pop();

                    // Enqueue all valid neighbords
                    add_neighbor(grid, point, -1,  0, q);
                    add_neighbor(grid, point,  0, -1, q);
                    add_neighbor(grid, point,  1,  0, q);
                    add_neighbor(grid, point,  0,  1, q);
                }
            }
        }
        return count;
    }

    void add_neighbor(vector<vector<char>>& grid, Point point, 
                      int d_row, int d_col, queue<Point> &q) {
        point.row += d_row;
        point.col += d_col;
        if (point.row >= nr_row || point.col >= nr_col || 
                point.row < 0 || point.col < 0 ||
                grid[point.row][point.col] == '0') {
            return;
        }
        grid[point.row][point.col] = '0';

        q.push(point);
    }
};


// using union-find (disjoint-set)
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int sz = grid.size();
        int count = 0;
        vector<int> parent(sz ? sz * grid[0].size() : 0);
        for (int row = 0; row < grid.size(); ++row) {
            for (int col = 0; col < grid[row].size(); ++col) {
                if (grid[row][col] == '1') {
                    ++count;
                    int i = idx(row, col, sz);
                    parent[i] = i;
                    if (row > 0 && grid[row-1][col] == '1' && is_disjoint_set(i, idx(row-1, col, sz), parent))
                        --count;
                    if (col > 0 && grid[row][col-1] == '1' && is_disjoint_set(i, idx(row, col-1, sz), parent))
                        --count;
                }
            }
        }
        return count;
    }

    bool is_disjoint_set(int x, int y, vector<int>& parent) {
        int rootx = find(x, parent);
        int rooty = find(y, parent);
        if (rootx == rooty)
            return false;
        parent[rooty] = rootx;
        return true;
    }

    int find(int x, vector<int>& parent) {
        return (parent[x] == x) ? x : find(parent[x], parent);
    }
    
    inline int idx(int row, int col, int nrows) { return col * nrows + row; }
};
