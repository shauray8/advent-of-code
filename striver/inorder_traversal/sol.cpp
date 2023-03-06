#include <bits/stdc++.h>

using namespace std;

struct node{
  int data;
  struct node * left, *right;
};

struct node * tree(int data){
  struct node * node = (struct node *) malloc(sizeof(struct node));
  node -> data = data;
  node -> left = NULL;
  node -> right = NULL;

  return (node);
}


//void inOrder(node * root){
//  if(!root) {return;}
//  inOrder(root->left);
//  some.push_back(root->data);
//  inOrder(root->right);
//}

vector<int> it_inOrder(node * root){
  vector<int> a_some;
  stack <node *> s;
  while(true){
    if(root != NULL){
      s.push(root);
      root = root->left;
    }
    else{
      if (s.empty()) {break;}
      root = s.top();
      a_some.push_back(root->data);
      s.pop();
      root = root->right;
    }
  }
  return a_some;
}

int main(){

  struct node * root = tree(1);
  root -> left = tree(2);
  root -> right = tree(3);
  root -> left ->left = tree(4);
  root -> left -> right = tree(5);
  root -> right -> left = tree(6);
  
  vector<int> some;
  some = it_inOrder(root);

  for(int i=0; i<some.size(); i++){
    printf("%d",some[i]);
  }
}
