import java.util.Scanner;
class Main {
  public static void main(String[] args) {

    System.out.println("Hello, this is The Talk Bot");
    System.out.println("I talk to you. I'm here for you. I got your back.");
    System.out.println("How is your day going? [Answer as 'good' or 'bad' [With NO Capitals]]");
    
    while(1 < 2){
    
    Scanner reader = new Scanner(System.in);
    String input = reader.nextLine();

    if(input.equals("good")){
      System.out.println("Thats great, tell me something that made you happy!");
      Scanner reader2 = new Scanner(System.in);
      String input2 = reader2.nextLine();
      System.out.println("That's awesome, make sure the good things keep coming! Do you have another good/bad thing to say [Answer with 'good' or 'bad']. If not, say 'no' [With NO Capitals]");
      Scanner reader3 = new Scanner(System.in);
      String input3 = reader3.nextLine();
      if(input3.equals("no")){
        System.out.println("Ok, see you soon!");
        System.exit(0);
      }
    }

    else if(input.equals("bad")){
      System.out.println("Thats not good, how come your day is bad?");
      Scanner reader2 = new Scanner(System.in);
      String input2 = reader2.nextLine();
      System.out.println("Oh well, I'm sure something good will happen soon! Do you have another good/bad thing to say [Answer with 'good' or 'bad']. If not, say 'no' [With NO Capitals]");
      Scanner reader3 = new Scanner(System.in);
      String input3 = reader3.nextLine();
      if(input3.equals("no")){
        System.out.println("Ok, see you soon!");
        System.exit(0);
      }
    
    }else{
      System.out.println("I'm sorry, that is not on my database, I said to answer with 'good' or 'bad', with no capitals.");
    }

    }
  }
}