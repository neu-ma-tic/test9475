package Bladeslayer.BladesBot;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.entities.Activity;
import net.dv8tion.jda.api.requests.GatewayIntent;
import net.dv8tion.jda.api.utils.MemberCachePolicy;

import javax.security.auth.login.LoginException;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;

public class Bot {

    public static String prefix = "a!";

    //Main Method

    public static void main(String[] args) throws LoginException , FileNotFoundException {
        File file = new File("D:\\BotToken.txt");
        FileReader fr = new FileReader(file);
        
       /// String token = FileUtils.readFileToString(new File("C:\\Users\\Anirudh\\Desktop\\BotToken.txt"), "utf-8");
        JDABuilder  jda = JDABuilder.createDefault("NzU3NzkwMzI2NjUwODMwOTIw.X2lhPA.H9OX9syt38Sjg7bbImPobNihEy8");
        jda.enableIntents(GatewayIntent.GUILD_MEMBERS);
        jda.setActivity(Activity.playing("Destiny 2 | a!help"));
       // jda.addEventListeners(new GuildMessageReceived(), GuildMessageReactionAdd());
        jda.addEventListeners(new Clear(), new GuildMemberJoin() , new Trails(), new Hi(), new UwU(), new Specs(), new GuildMemberLeave(), new Ping(), new WebScrap(), new Help());
        jda.setMemberCachePolicy(MemberCachePolicy.ALL);
        jda.build();


    }
}