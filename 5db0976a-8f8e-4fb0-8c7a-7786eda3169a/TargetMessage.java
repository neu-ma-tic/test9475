import java.util.*;

public class TargetMessage extends Message{	
	private String secondHalf;
	
	public TargetMessage(int h, String s1, String s2){
		super(h,s1);
		secondHalf = s2;
	}
	
	public TargetMessage(String s1, String s2){
		super(s1);
		secondHalf = s2;
	}
	
	public int getHarshness(){
		return super.getHarshness();
	}
	
	public String getPhrase(String target){
		return super.getPhrase() + target + secondHalf;
	}
	
}