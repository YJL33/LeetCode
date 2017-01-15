/*
Maximum Subtree of Average
*/
import java.util.ArrayList;
class Node { 
    int val;
    ArrayList<Node> children;
    public Node(int val){
        this.val = val;
        children = new ArrayList<Node>();
    }
}