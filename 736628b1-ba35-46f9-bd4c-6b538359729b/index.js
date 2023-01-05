var locale = applicationManager.GetCurrentLocale();
Console.WriteLine("This user's language is {0}", locale);
var branch = applicationManager.GetCurrentBranch();
if (branch != MyBranches.Stable)
{
  Console.WriteLine("You are on a beta branch; expect bugs!");
}

applicationManager.GetOAuth2Token

applicationManager.ValidateOrExit((result) =>
{
  if (result == Discord.Result.Ok)
  {

  }
  else
  {
    Console.WriteLine("Oops! Something went wrong, closing game...");
  }
});

public class SignedAppTicket
{
  public long application_id;
  public Discord.User user;
  public List<Discord.Entitlement> entitlements;
  public string timestamp;
}

public void DoTheThing()
{
  // This example is using the libsodium-net library
  // https://github.com/adamcaudill/libsodium-net
  var appManager = discord.GetApplicationManager();
  var MY_PUBLIC_KEY = "460cab5f2237b71e3c2c06bzze217f4f68d55db16dae672bdfb6618235589999";
  var MY_SKU_ID = "492432195219099999";

  // Get the ticket
  appManager.GetTicket((Discord.Result res, ref string ticket) =>
  {
    // Split the ticket into its parts
    var parts = ticket.Split('.');

    // Ensure the version matches
    if(parts[0] == "2")
    {
      // Verify the signature
      // Your public key will be given to you by Discord
      if (Sodium.PublicKeyAuth.VerifyDetached(HexToByte(parts[1]), System.Text.Encoding.UTF8.GetBytes(parts[2]), HexToByte(MY_PUBLIC_KEY)))
      {
        // If valid, decode the string
        var byteData = Convert.FromBase64String(parts[2]);
        var json = System.Text.Encoding.UTF8.GetString(byteData);

        // Deserialize it into the ticket object
        var myTicket = Newtonsoft.Json.JsonConvert.DeserializeObject<SignedAppTicket>(json);

        // Check for entitlement to the SKU!
        if (myTicket.entitlements.Any(x => x.SkuId == MY_SKU_ID))
        {
          Console.WriteLine("User has entitlement to your game");
        }
        else
        {
          Console.WriteLine("Not entitled");
        }
      }
    }