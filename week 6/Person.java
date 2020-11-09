public class Person{
    private String name;
    private int age;

    public Person(String n, int a){
        this.name = n;
        this.age = a;
    }

    public String toString(){
        return "Name: " + this.name + " Age: " + this.age;
    }

    public void setAge(int n){
        if (n < 0){

            return;
        }

        this.age = n;
    }

    public static void main(String[] args){
        Person a = new Person("John", 23);
        Person b = new Person("Paul", 55);
        System.out.println(a);
        a.age = -1;
        // a.setAge(40);
        System.out.println(a);
        System.out.println(b);
    }
}