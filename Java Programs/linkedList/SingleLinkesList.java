public class Main{
    public static Node head=null;
    public static Node tail=null;
    public static class Node{
        int value;
        Node next;
        
        public Node(int value){
            this.value=value;
            this.next=null;
        }
    }
    public static void insertBeg(int value){
        Node newnode=new Node(value);
        if(head==null)
        {
            head=newnode;
            tail=newnode;
        }else{
            newnode.next=head;
            head=newnode;
        }
    }
    public static void insert(int value){
        Node newnode=new Node(value);
        if(head==null){
            head=newnode;
            tail=newnode;
        }else{
            tail.next=newnode;
            tail=newnode;
        }
        
    }    
    public static void insertMid(int value,int node_value){
        Node newnode=new Node(value);
        Node current=head;
        if(head.value==node_value){
           newnode.next=head;
           head=newnode;
        }else{
            while(current.next.value!=node_value){
                current=current.next;
            }
            newnode.next=current.next;
            current.next=newnode;
        }
    
    }
    public static void delete(int node_value)
    {
        Node current=head;
        if(head.value==node_value)
        {
            head=head.next;
        }
        else{
            while(current.next.value!=node_value)
            {
                current=current.next;
            }
            if(current.next.next==null)
            {
                current.next=null;
            }else{
                current.next=current.next.next;
            }
        } 
    }
    public static void display(){
        Node current=head;
        while(current!=null){
            System.out.print(current.value+" ");
            current=current.next;
        }
        System.out.println();
    }
    public static void main (String[] args) {
        
         insert(10);
         insert(20);
         insert(30);
         insert(40);
         insert(50);
         insert(60);
         insert(70);
         display();
         insertBeg(205);
         insertBeg(207);
         display();
         insertMid(1000,30);
         insertMid(2000,1000);
         display();
         delete(2000);
         display();
         delete(207);
         display(); 
         delete(70);
         display();
    }
}
