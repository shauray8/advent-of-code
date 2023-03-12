#include <bits/stdc++.h>

using namespace std;

struct node {
  int val;
  node *left, *right;
};

struct node * tree(int val){
  struct node * node = (struct node *) malloc(sizeof(struct node));
  node->val = val;
  node->right = NULL;
  node->left = NULL;
}

vector<int> s;
vector<int> postorder(node * root){
  if(root){
    postorder(root->left);
    postorder(root->right);
    s.push_back(root->val);
  }
  return s;

}

int main(){
  vector<int> s;
  struct node * root = tree(1);
  root -> left = tree(2);
  root -> right = tree(3);
  root -> left ->left = tree(4);
  root -> left -> right = tree(5);
  root -> right -> right = tree(6);

  s = postorder(root);
  for(int i=0; i<s.size(); i++){
    printf("%d",s[i]);
  }



}
