import java.util.*;

class Main {
	private static Scanner scan = new Scanner( System.in );
	private static ArrayList<String> commands = new ArrayList<String>();
  private static ArrayList<Message> messages = new ArrayList<Message>();
  private static ArrayList<Message> jokes = new ArrayList<Message>();
  private static ArrayList<Message> youknowwhattheysays = new ArrayList<Message>();
  private static ArrayList<Message> mixers = new ArrayList<Message>();
  private static ArrayList<TargetMessage> insults = new ArrayList<TargetMessage>();
  private static ArrayList<TargetMessage> praises = new ArrayList<TargetMessage>();
  private static boolean isParticipating = false;
  private static int currentMessageRate = 7;
  private static int currentHarshnessCap = 9;
  
  
  public static void main(String[] args) {
    addCommands(commands);
    addMessages(messages);
    addInsults(insults);
    addJokes(jokes);
    addPraises(praises);
    addMixers(mixers);
    System.out.println("Start Up Chatbot?");
    String response = scan.nextLine();
    if(response.equals("Yes") || response.equals("yes") || response.equals("Y") || response.equals("y")){
    	System.out.println("Chatbot activated. Start talkin'");
    	activateChatbot();
    	
    }
    
    
  }
  
  public static void activateChatbot(){
  	String response;
  	boolean cont = true;
  	int messageCount = 0;
  	while(cont){
  		response = scan.nextLine();
  		//check to see if message is a command and is valid
  		if(response.indexOf("|") == 0 ){
  			boolean commandHasParams = response.indexOf(" ") != -1;
  			executeCommand(response,commandHasParams);
  		}
  		
  			
  		if(isParticipating && messageCount % (11 - currentMessageRate) == 0){
  			int phraseIndex = (int)(Math.random() * messages.size());
  			while(messages.get(phraseIndex).getHarshness() > currentHarshnessCap){
  				phraseIndex = (int)(Math.random() * messages.size());
  			}
  			String phraseToSay = messages.get(phraseIndex).getPhrase();
  			System.out.println(phraseToSay);
  		}
  		
  		messageCount++;
  	}
  	
  }
  
  public static void executeCommand(String command, boolean commandHasParams){
  	String comm = command;
  	String param = "";
  	if(commandHasParams){
  		comm = command.substring(0,command.indexOf(" "));
  		param = command.substring(command.indexOf(" ") + 1);
  	}
  	if(comm.equals("|help")){
  		help();
  	} else if(comm.equals("|help2")){
  		help2();
  	} else if(comm.equals("|help3")){
  		help3();
  	} else if(comm.equals("|youknowwhattheysay")){
  		youknowwhattheysay();
  	} else if(comm.equals("|participate")){
  		participate();
  	} else if(comm.equals("|leave")){
  		leave();
  	} else if(comm.equals("|addmessage")){
  		addmessage(comm);
  	} else if(comm.equals("|deletemessage")){
  		deletemessage(comm);
  	} else if(comm.equals("|insult")){
  		insult(param);
  	} else if(comm.equals("|praise")){
  		praise(param);
  	} else if(comm.equals("|joke")){
  		joke();
  	} else if(comm.equals("|dosomemath")){
  		dosomemath();
  	} else if(comm.equals("|titaan")){
  		titaan();
  	} else if(comm.equals("|haiku")){
  		haiku();
  	} else if(comm.equals("|meme")){
  		meme();
  	} else if(comm.equals("|introduce")){
  		introduce();
  	} else if(comm.equals("|messagerateup")){
  		messagerateup();
  	} else if(comm.equals("|messageratedown")){
  		messageratedown();
  	} else if(comm.equals("|messageharshness")){
  		if(isInteger(param)){
  			messageharshness(Integer.parseInt(param));
  		} else {
  			System.out.println("Sorry, that parameter is not valid. Check to see that there is only one space between the command and parameter and that there is nothing after it.");
  		}
  		
  	} else if(comm.equals("|messagerate")){
  		if(isInteger(param)){
  			messagerate(Integer.parseInt(param));
  		} else {
  			System.out.println("Sorry, that parameter is not valid. Check to see that there is only one space between the command and parameter and that there is nothing after it.");
  		}
  	} else if(comm.equals("|soften")){
  		soften();
  	} else if(comm.equals("|harshen")){
  		harshen();
  	} else if(comm.equals("|refer")){
  		refer();
  	} else {
  		System.out.println("Sorry, this command is not valid. Do \"|help\" for a list of valid commands.");
  	}
  	
  }
  
  public static void help(){
  	System.out.println("[youknowwhattheysay]:provides a simple saying\n[participate]:gets this little bot in the conversation\n[leave]:gets this little bot out of the conversation\n[addmessage]:adds a message to the bot's vernacular\n[deletemessage]:deletes a message from the bot's vernacular\n[insult <target>]:insults someone\n[praise <target>]:praises someone\n[joke]:tells a joke\n[dosomemath]:does some math\n[titaan]:does a mini-\"Things I Think About At Night\" episode, based on previous vocabulary\n\nRemember, use the | character before each line in order to call the command correctly.");
  }
  
  public static void help2(){
  	System.out.println("[haiku]:makes a little haiku about life and stuff I guess\n[meme]:gives a nice little meme\n[introduce]:introduces this bot talking right now\n[messagerateup]:increases the rate that the bot sends messages\n[messageratedown]:decreases the rate that the bot sends messages\n[messagerate]:sets the rate that the bot sends messages\n\nRemember, use the | character before each line in order to call the command correctly.");
  }
  
  public static void help3(){
  	System.out.println("This command has not been implemented yet. Tell Shelton to get on that.");
  }
  
  public static void youknowwhattheysay(){
  	System.out.println("This command has not been implemented yet. Tell Shelton to get on that.");
  }
  
  public static void participate(){
  	if(isParticipating){
  		System.out.println("The bot is already participating in the conversation. If you can't see the messages, try increasing the message rate.");
  	} else {
  		isParticipating = true;
  	}
  }
  
  public static void leave(){
  	if(!isParticipating){
  		System.out.println("The bot is not participating currently.");
  	} else {
  		isParticipating = false;
  	}
  }
  
  public static void addmessage(String s){
  	Message adder = new Message(s);
  	messages.add(adder);
  }
  
  public static void deletemessage(String s){
  	for(int i = 0; i < messages.size(); i++){
  		if(messages.get(i).getPhrase().equals(s)){
  			messages.remove(i);
  		}
  	}
  }
  
  public static void insult(String s){
  	if(s.indexOf("@") != 0){
  		System.out.println("Use the @ symbol to target someone");
  		return;
  	}
  	int phraseIndex = (int)(Math.random() * insults.size());
  	String phraseToSay = insults.get(phraseIndex).getPhrase(s);
 		System.out.println(phraseToSay);
  }
  
  public static void praise(String s){
  	if(s.indexOf("@") != 0){
  		System.out.println("Use the @ symbol to target someone");
  		return;
  	}
  	int phraseIndex = (int)(Math.random() * praises.size());
  	String phraseToSay = praises.get(phraseIndex).getPhrase(s);
 		System.out.println(phraseToSay);
  }
  
  public static void joke(){
  	int phraseIndex = (int)(Math.random() * jokes.size());
  	String phraseToSay = jokes.get(phraseIndex).getPhrase();
 		System.out.println(phraseToSay);
  }
  
  public static void dosomemath(){
  	int r1Index = (int)(Math.random() * mixers.size());
  	String r1 = mixers.get(r1Index).getPhrase();
  	int r2Index = (int)(Math.random() * mixers.size());
  	String r2 = mixers.get(r2Index).getPhrase();
  	int endIndex = (int)(Math.random() * mixers.size());
  	String end = mixers.get(endIndex).getPhrase();
  	int signDeterminer = (int)((Math.random() * 4) + 1);
  	String sign;
  	if(signDeterminer == 1){
  		sign = " + ";
  	} else if(signDeterminer == 2){
  		sign = " - ";
  	} else if(signDeterminer == 3){
  		sign = " * ";
  	} else {
  		sign = " / ";
  	}
  	System.out.println(r1 + sign + r2 + " = " + end);
 		
  }
  
  public static void titaan(){
  	System.out.println("This command has not been implemented yet. Tell Shelton to get on that.");
  }
  
  public static void haiku(){
  	System.out.println("This command has not been implemented yet. Tell Shelton to get on that.");
  }
  
  public static void meme(){
  	System.out.println("This command has not been implemented yet. Tell Shelton to get on that.");
  }
  
  public static void introduce(){
  	System.out.println("Hi! I'm a bot made by Shelton. Right now I can't do much, but I'm coming along. I can give help, participate in conversations, and make some dumb jokes. I may one day even be able to simulate a real person's nightly thoughts, if Shelton gets off his lazy ass to make the method work.");
  }
  
  public static void messagerateup(){
  	if(currentMessageRate < 10){
  		currentMessageRate++;
  		System.out.println("The message rate is now " + currentMessageRate);
  	} else {
  		System.out.println("The message rate can not be raised");
  	}
  }
  
  public static void messageratedown(){
  	if(currentMessageRate > 0){
  		currentMessageRate--;
  		System.out.println("The message rate is now " + currentMessageRate);
  	} else {
  		System.out.println("The message rate can not be lowered");
  	}
  }
  
  public static void messagerate(int x){
  	if(x > 0 && x <= 10){
  		currentMessageRate = x;
  		System.out.println("The message rate is now " + currentMessageRate);
  	} else {
  		System.out.println("Pick a integer between 1 and 10.");
  	}
  	
  }
  
  public static void messageharshness(int x){
  	if(x > 0 && x <= 10){
  		currentHarshnessCap = x;
  		System.out.println("The harshness is now " + currentHarshnessCap);
  	} else {
  		System.out.println("Pick a integer between 1 and 10.");
  	}
  }
  
  public static void soften(){
  	if(currentHarshnessCap >1 ){
  		currentHarshnessCap--;
  		System.out.println("The harshness is now " + currentHarshnessCap);
  	} else {
  		System.out.println("The harshness can not be lowered");
  	}
  }
  
  public static void harshen(){
  	if(currentHarshnessCap < 10 ){
  		currentHarshnessCap++;
  		System.out.println("The harshness is now " + currentHarshnessCap);
  	} else {
  		System.out.println("The harshness is at it's maximum");
  	}
  }
  
  public static void refer(){
  	System.out.println("This command has not been implemented yet. Tell Shelton to get on that.");
  }
  
  //Adding basic commands and messages
  
  public static void addCommands(ArrayList<String> x){
  	x.add("|help");//First help screen
    x.add("|help2");//Second help screen
    x.add("|help3");//Third help screen
    x.add("|youknowwhattheysay");//Provides "You know what they say"
    x.add("|participate");//enters a chat
    x.add("|leave");//leaves chat
    x.add("|addmessage");//adds a message to the roster
    x.add("|deletemessage");//deletes a message from the roster
    x.add("|insult");//insults a person
    x.add("|praise");//praises a person
    x.add("|joke");//tells a joke
    x.add("|dosomemath");//does some math (not actual math)
    x.add("|titaan");//does a pseudo things i think about at night
    x.add("|haiku");//does a haiku
    x.add("|meme");//shows a meme
    x.add("|introduce");//introduces self
    x.add("|messagerateup");//turns up frequency of messages
    x.add("|messageratedown");//turns down frequency of messages
    x.add("|messageharshness");//sets message harshness
    x.add("|messagerate");//sets messagerate
    x.add("|soften");//turns down message harshness
    x.add("|harshen");//turns up message harshness
    x.add("|refer");//gives someone a source for something
  }
  
  public static void addMessages(ArrayList<Message> x){
  	AddingStuff.addMsgs(x);
  }
  
  public static void addSayings(ArrayList<Message> x){
  	AddingStuff.addProverbs(x);
  	
  }
  
  public static void addJokes(ArrayList<Message> x){
  	AddingStuff.addJks(x);
  }
  
  public static void addInsults(ArrayList<TargetMessage> x){
  	AddingStuff.addBads(x);

  }
  
  public static void addPraises(ArrayList<TargetMessage> x){
  	AddingStuff.addGoods(x);
  }
  
  public static void addMixers(ArrayList<Message> x){
  	AddingStuff.addMaths(x);
  }
  
  //Little thing to help see if params are valid for some stuff
  public static boolean isInteger(String s) {
    try { 
        Integer.parseInt(s); 
    } catch(NumberFormatException e) { 
        return false; 
    } catch(NullPointerException e) {
        return false;
    }
    // only got here if we didn't return false
    return true;
	}
  
}