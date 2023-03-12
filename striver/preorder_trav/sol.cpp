#include <bits/stdc++.h>

using namespace std;

struct node{
  int val;
  node * left, * right;
};

struct node * tree(int val){
  struct node * node = (struct node *) malloc(sizeof(struct node ));
  node -> val = val;
  node -> left = NULL;
  node -> right = NULL;
}

//vector<int> preorder(node * root){
//  if (root){
//    s.push_back(root->val);
//    preorder(root->left);
//    preorder(root->right);
//  }
//  return s;
//}

vector<int> it_preorder(node * root){
  vector<int> s;
  stack<node *> st;
  while(true){
    if(root){
      s.push_back(root->val);
      st.push(root);
      root = root->left;
    }
    else{
      if (s.empty()) {break;}
      root = st.top();
      st.pop();
      root = root -> right;
    }
  }
  return s;
}

int main(){
    vector<int> is;
    struct node * root = tree(1);
    root -> right = tree(2);
    root -> right -> left = tree(3);


    is = it_preorder(root);
    for(int i=0; i<is.size(); i++){
      printf("%d",is[i]);
    }
    

}
