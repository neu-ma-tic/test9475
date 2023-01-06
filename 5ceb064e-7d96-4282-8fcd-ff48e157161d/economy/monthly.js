module.exports = {
  
  name: "monthly",
  code: `
$title[Monthly Salary.]
$thumbnail[$userAvatar[$authorID]]
$description[קיבלת **$getServerVar[monthly]** מהתקציב היומי שלך! הכסף כבר במזומן!]
$color[RANDOM]
$footer[ShopRoles]
$addTimestamp

$setGlobalUserVar[cash;$sum[$getGlobalUserVar[cash];$getServerVar[monthly]]]
$globalCooldown[30d;**⏰ חכה %time% בשביל לעשות פקודה שוב!**]`
}