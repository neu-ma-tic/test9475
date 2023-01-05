module.exports = {
  
  name: "buyfishrod",
  code: `
$description[**@$username Success in buying a Fishing equipment🎣 !!**]
$color[$random[0;999999]]
$setGlobalUserVar[cash;$sub[$getGlobalUserVar[cash];75]]
$setGlobalUserVar[fishrod;$sum[$getGlobalUserVar[fishrod];1]]
$onlyIf[$getGlobalUserVar[cash]>=75;Not enough cash!]`
}