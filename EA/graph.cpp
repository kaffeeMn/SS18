#include"graph.h"
#include <string>
#include <iostream>

Graph::Graph(std::vector<Node> nodes){
    this->nodes = &nodes;
}
std::vector<Node> Graph::BFS(Node *n_s, Node *n_g){
    /**
     * Breath First Search
     * :param n_s:  pointer to the note to search from
     * :param n_g:  pointer to the note to find path to
     * :return:     vector of the shortest path
     */
    std::vector<Node> ret_vec;
    std::queue<Node> *nodes_q = new std::queue<Node>;
    nodes_q->push(*n_s);

    std::unordered_map<int,bool> visited;
    for(int i=0; i<this->nodes->size(); ++i){
        visited[this->nodes->at(i).id] = false;
    }

    Node *current;
    int distance = 0;
    int j;
    while(! nodes_q->empty()){
        current = & nodes_q->front();
        nodes_q->pop();
        // marking as visited
        visited[current->id] = true;
        // returning if path was found
        if(current-> id == n_g->id){
            nodes_q = NULL;
            delete nodes_q;
            return ret_vec;
        }
        // checking paths of incident nodes
        for(j=0; j<this->adj[current->id].size(); ++j){
            // visiting all edges
            nodes_q->push(this->adj[current->id][j]);
        }
    }

    nodes_q = NULL;
    delete nodes_q;
    return ret_vec;
}
std::unordered_map<int, std::vector<Node> > Graph::DFS(){
    std::unordered_map<int, std::vector<Node> > ret_map;
    return ret_map;
}
