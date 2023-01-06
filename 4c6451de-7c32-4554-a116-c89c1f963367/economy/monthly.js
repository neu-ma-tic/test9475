module.exports = {
  
  name: "monthly",
  code: `
$title[Monthly Salary.]
$thumbnail[$userAvatar[$authorID]]
$description[You have received **$getServerVar[monthly]** of your daily allowance! The money is already in cash!]
$color[RANDOM]
$footer[ZCOINS]
$addTimestamp

$setGlobalUserVar[cash;$sum[$getGlobalUserVar[cash];$getServerVar[monthly]]]
$globalCooldown[30d;**⏰ Wait for %time% to claim monthly salary again!**]`
}
git clone https://github.com/baeriri/multipurpose-bot.git