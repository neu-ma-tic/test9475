let discord = new LoginWithDiscord({
    cache: true,
    clientID: "474677697474330625",
    scopes: [
        Scope.Identify, Scope.Connections, Scope.Guilds
    ]
});
let guilds;
discord.onlogin = async () => {
    document.getElementById("login").style.display = "none";
    document.getElementById("loaded").style.display = null;
    let user = await discord.fetchUser();
    let connections = await discord.fetchConnections();
    guilds = await discord.fetchGuilds();
//2146958847
//let adminguilds = guilds. filter(guild => guild.permissions.has("MANAGE_GUILD") || guild.permissions.has("ADMINISTRATOR"));

let adminguilds = guilds. filter(guild => guild.permissions.has("MANAGE_GUILD") || guild.permissions.has("ADMINISTRATOR") || guild.owner === true);
    document.getElementById("userpfp").src = user.avatarURL;
    document.getElementById("userid").innerHTML = user.id;
    document.getElementById("usertag").innerHTML = `<span class="username">${user.username}</span><span class="desc">${user.discriminator}</span>`;
  //  document.getElementById("useremail").innerHTML = user.email;
   
    let g = document.getElementById("guilds");
    g.innerHTML = "";
    for (let guild of adminguilds) {
        let child = document.createElement("div");
        child.classList.add("guild");
       
        child.innerHTML = guild.icon
            ? `<a href="http://agentx.ga/manage/${guild.id}/${user.id}"><img title="${guild.name}" src="${guild.iconURL}"/></a>`
            : `<div class="img"><a href="http://agentx.ga/manage/${guild.id}/${userid}"><span title="${guild.name}">${guild.name.split(" ").map(x => x[0]).join("")}</span></a></div>`;
        g.appendChild(child);
}    
};
function inspectGuild(guildid) {
    let inspector = document.getElementById("guildinspector");
    if (guildid == null) {
        inspector.innerHTML = `<div class="img"></div><div class="name"></div>`;
        return;
    }
    let guild = guilds.find(x => x.id === guildid);
    inspector.innerHTML = guild.icon
        ? `<img src="${guild.iconURL}"/><div class="name">${guild.name} ${guild.owner ? "<img class='owner' src='./owner.svg'/>" : ""}</span></div>`
        : `<div class="img"><span>${guild.name.split(" ").map(x => x[0]).join("")}</span></div><div class="name">${guild.name} ${guild.owner ? "<img class='owner' src='./owner.svg'/>" : ""}</span>`;
}
discord.onlogout = async () => {
    document.getElementById("login").style.display = null;
    document.getElementById("loaded").style.display = "none";
};
async function login() {
    await discord.login();
}
async function logout() {
    await discord.logout();
}
