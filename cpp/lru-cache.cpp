class LRUCache {
public:
    LRUCache(int capacity)
     : size{capacity} { }

    int get(int key) {
        // Return -1 if the key was not in the map
        if (hashmap.count(key) == 0) {
            return -1;
        }
        update_cache(key);
        return hashmap[key];
    }
    
    
    void put(int key, int value) {
        if (hashmap.size() == size and hashmap.count(key) == 0) {
            clear_cache();
        }
        update_cache(key);
        hashmap[key] = value;
    }

private:
    int size;
    list<int> lru;
    unordered_map<int, list<int>::iterator> map_itr;
    unordered_map<int, int> hashmap;

    // clears the lru cache
    void clear_cache() {
        map_itr.erase(lru.back());
        hashmap.erase(lru.back());
        lru.pop_back();
    }

    // adds a new key to the cache
    void update_cache(int key) {
        if (hashmap.count(key) == 1) {
            lru.erase(map_itr[key]);
        }

        lru.push_front(key); // O(1)

        map_itr[key] = lru.begin();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */