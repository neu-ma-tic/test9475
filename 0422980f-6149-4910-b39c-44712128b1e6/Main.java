import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.entities.Activity;
import net.dv8tion.jda.api.requests.GatewayIntent;
import net.dv8tion.jda.api.utils.Compression;

import javax.security.auth.login.LoginException;

public class Main {

    public static JDABuilder builder;

    public static void main(String[] args) throws LoginException {

        String token = "ODM2MjY5NDQ5NTg1NDkxOTg4.YIbinQ.U_Ds8htOUleshmf5No3ilhS_C_4";
        builder = JDABuilder.createDefault(token);
        builder.setBulkDeleteSplittingEnabled(false);
        builder.setCompression(Compression.NONE);
        builder.setActivity(Activity.watching("auf dich!"));
        builder.enableIntents(GatewayIntent.GUILD_MEMBERS);
        builder.build();

    }
}