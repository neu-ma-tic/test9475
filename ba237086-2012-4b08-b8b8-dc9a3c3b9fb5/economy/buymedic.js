module.exports = {
  
  name: "buymedic",
  code: `
$description[**@$username Success in buying a Medicine💊 !!**]
$setGlobalUserVar[cash;$sub[$getGlobalUserVar[cash];125]]
$setGlobalUserVar[hm;$sum[$getGlobalUserVar[hm];1]]
$onlyIf[$getGlobalUserVar[cash]>=125;Not enough cash!]
$color[$random[0;999999]]
`
}