import java.util.*;

public class Message{
	private int harshness;
	private String phrase;
	
	
	public Message(int h, String s){
		harshness = h;
		phrase = s;
	}
	
	public Message(String s){
		harshness = 1;
		phrase = s;
	}
	
	public int getHarshness(){
		return harshness;
	}
	
	public String getPhrase(){
		return phrase;
	}
	
}