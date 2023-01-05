import com.seailz.modalapi.listeners.ModalListener;
import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.OnlineStatus;
import net.dv8tion.jda.api.entities.Activity;
import net.dv8tion.jda.api.requests.GatewayIntent;

import javax.security.auth.login.LoginException;

public class birthdaybot {
    public static void main(String[] args) throws LoginException {
        String botprefix = "birthdaybot";
        String botstatus = "Happy Birthday";
        String bottoken = "MTAzMzEyNDkxMzQxNTk5NTQ5NA.GVyJLN.6QtRdcax3ZcCKHe6iGW4yZSWWaTzHlrx0OrTEQ";


        JDABuilder builder = JDABuilder.createDefault(bottoken).enableIntents(GatewayIntent.GUILD_MEMBERS, GatewayIntent.MESSAGE_CONTENT);
        builder.setStatus(OnlineStatus.DO_NOT_DISTURB);
        builder.setActivity(Activity.playing(botstatus));
        builder.addEventListeners(new birthday());
        builder.addEventListeners(new ModalListener());
        JDA birthdaybot = builder.build();

        System.out.println("birthdaybot Bot activated!");
        System.out.println("birthdaybot Bot Prefix: " + botprefix);
    }
}
