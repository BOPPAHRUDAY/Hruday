//iterative preorder traversal

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> list=new ArrayList<Integer>();
        if(root==null) return list;
        Stack<TreeNode> st=new Stack<TreeNode>();
        TreeNode cur=root;
        st.push(cur);
        while(!st.isEmpty()){
            cur=st.pop();
            list.add(cur.val);
            if(cur.right!=null)
                st.push(cur.right);
            if(cur.left!=null)
                st.push(cur.left); 
        }
        return list;
    }    
}
