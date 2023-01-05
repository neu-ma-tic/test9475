module.exports = {
  
  name: "selldiamond",
  code: `
$setGlobalUserVar[cash;$sum[$getGlobalUserVar[cash];100]]
$setGlobalUserVar[diamond;$sub[$getGlobalUserVar[diamond];1]]
$title[__**SELLING DIAMOND💎**__]
$color[00ff59]
$description[
**@$username Successfully selling 1 diamond for $100.**]
$onlyIf[$getGlobalUserVar[diamond]>=1;You don't have that many diamonds!.]`
}