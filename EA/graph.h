#include<stddef.h>
#include<map>
#include<unordered_map>
#include<queue>

struct Node{
    int id;
    bool directed;
    int* coordinates;
    int* weights;
};
class Graph{
    public:
        Graph(std::vector<Node> node);
        ~Graph();
        std::vector<Node> BFS(Node *n_s, Node *n_g);
        std::unordered_map<int, std::vector<Node> > DFS();

    private:
        std::vector<Node> *nodes;
        std::unordered_map<int, std::vector<Node> > adj;
};
