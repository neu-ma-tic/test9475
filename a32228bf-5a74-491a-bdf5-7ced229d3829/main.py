import os
import discord
from replit import db
import json
import requests
import time
from pymongo import MongoClient
import pymongo
client = pymongo.MongoClient("mongodb+srv://wally:world@wally.2qumy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
# Get the database
collection_name = db["walmart_items"]

w_url='https://images.squarespace-cdn.com/content/v1/597d0802cf81e04abc442f01/1542187178880-PR3JE7IVFOBKKDYU2XTR/walmart-bot.jpg?format=500w'
client = discord.Client()
my_secret = os.environ['TOKEN']
urls = ["google.com"]


def start():
  def url_request():
  

    url = "https://www.walmart.com/orchestra/home/graphql/deal?dealsId=deals/electronics&page=1&prg=desktop&rawFacet=undefined&seoPath=/shop/deals/electronics&ps=40&sort=best_match&searchParams.dealsId=deals/electronics&searchParams.page=1&searchParams.prg=desktop&searchParams.rawFacet=undefined&searchParams.seoPath=/shop/deals/electronics&searchParams.ps=40&searchParams.sort=best_match&searchParams.pageType=DealsPage&pageType=DealsPage&enablePortableFacets=true"
    
    payload = json.dumps({
      "query": "query Deals( $query:String $page:Int $prg:Prg! $facet:String $sort:Sort $catId:String! $max_price:String $min_price:String $module_search:String $affinityOverride:AffinityOverride $ps:Int $ptss:String $beShelfId:String $seoPath:String! $trsp:String $recall_set:String $dealsId:String! $pageType:String! $searchParams:JSON ={}$additionalQueryParams:JSON ={}$enablePortableFacets:Boolean = false ){search( query:$query page:$page prg:$prg facet:$facet sort:$sort cat_id:$catId max_price:$max_price min_price:$min_price module_search:$module_search affinityOverride:$affinityOverride additionalQueryParams:$additionalQueryParams ps:$ps ptss:$ptss trsp:$trsp recall_set:$recall_set _be_shelf_id:$beShelfId dealsId:$dealsId pageType:$pageType ){query searchResult{...DealsResultFragment}}contentLayout( channel:\"WWW\" pageType:$pageType tenant:\"WM_GLASS\" version:\"v1\" searchArgs:{query:$query cat_id:$catId _be_shelf_id:$beShelfId prg:$prg}){modules(tempo:{pageId:$dealsId}){...ModuleFragment type configs{...on EnricherModuleConfigsV1{zoneV1}__typename...on _TempoWM_GLASSWWWSearchSortFilterModuleConfigs{facetsV1 @skip(if:$enablePortableFacets){...FacetFragment}topNavFacets @include(if:$enablePortableFacets){...FacetFragment}allSortAndFilterFacets @include(if:$enablePortableFacets){...FacetFragment}}...on TempoWM_GLASSWWWPillsModuleConfigs{moduleSource pillsV2{...PillsModuleFragment}}...on TempoWM_GLASSWWWDealsListingConfigConfigs{_rawConfigs tileSize deals(searchParams:$searchParams){...DealsResultFragment}}...TileTakeOverProductFragment...on _TempoWM_GLASSWWWGiftFinderFiltersModuleConfigs{_rawConfigs facets{name type values{name itemCount isSelected}}}...on TempoWM_GLASSWWWGiftFinderModuleConfigs{_rawConfigs __typename}...ItemCarouselFragment...on TempoWM_GLASSWWWStoreSelectionHeaderConfigs{fulfillmentMethodLabel storeDislayName}...on TempoWM_GLASSWWWGenericCopyBlockConfigs{catCopyBlock(id:$dealsId pageType:$pageType)}...InlineSearchModuleFragment...EventTimerFragment...HorizontalChipModuleConfigsFragment...SkinnyBannerFragment...EarlyAccessBeforeEventBannerFragment...EarlyAccessLiveEventBannerFragment}}...LayoutFragment pageMetadata{location{postalCode stateOrProvinceCode city storeId}pageContext}}seoDealsMetaData(id:$dealsId path:$seoPath){metaTitle metaDesc metaCanon h1}}fragment DealsResultFragment on SearchInterface{title aggregatedCount...BreadCrumbFragment...DebugFragment...ItemStacksFragment...PageMetaDataFragment...PaginationFragment...RequestContextFragment...ErrorResponse modules{facetsV1 @skip(if:$enablePortableFacets){...FacetFragment}topNavFacets @include(if:$enablePortableFacets){...FacetFragment}allSortAndFilterFacets @include(if:$enablePortableFacets){...FacetFragment}pills{...PillsModuleFragment}giftFacets{name type values{name itemCount isSelected}}}}fragment ModuleFragment on TempoModule{name version type moduleId schedule{priority}matchedTrigger{zone}}fragment LayoutFragment on ContentLayout{layouts{id layout}}fragment BreadCrumbFragment on SearchInterface{breadCrumb{id name url}}fragment DebugFragment on SearchInterface{debug{sisUrl adsUrl}}fragment ItemStacksFragment on SearchInterface{itemStacks{displayMessage meta{adsBeacon{adUuid moduleInfo max_ads}query stackId stackType title layoutEnum totalItemCount totalItemCountDisplay viewAllParams{query cat_id sort facet affinityOverride recall_set min_price max_price}}itemsV2{...ItemFragment...InGridMarqueeAdFragment...TileTakeOverTileFragment}}}fragment ItemFragment on Product{__typename id usItemId fitmentLabel name checkStoreAvailabilityATC seeShippingEligibility brand type shortDescription imageInfo{...ProductImageInfoFragment}canonicalUrl externalInfo{url}itemType category{path{name url}}badges{flags{...on BaseBadge{key text type id}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought}}tags{...on BaseBadge{key text type}}}classType averageRating numberOfReviews esrb mediaRating salesUnitType sellerId sellerName hasSellerBadge availabilityStatusV2{display value}groupMetaData{groupType groupSubType numberOfComponents groupComponents{quantity offerId componentType productDisplayName}}productLocation{displayValue aisle{zone aisle}}fulfillmentSpeed offerId preOrder{...PreorderFragment}priceInfo{...ProductPriceInfoFragment}variantCriteria{...VariantCriteriaFragment}snapEligible fulfillmentBadge fulfillmentTitle fulfillmentType brand manufacturerName showAtc sponsoredProduct{spQs clickBeacon spTags}showOptions showBuyNow rewards{eligible state minQuantity rewardAmt promotionId selectionToken cbOffer term expiry description}}fragment ProductImageInfoFragment on ProductImageInfo{thumbnailUrl}fragment ProductPriceInfoFragment on ProductPriceInfo{priceRange{minPrice maxPrice}currentPrice{...ProductPriceFragment}wasPrice{...ProductPriceFragment}unitPrice{...ProductPriceFragment}listPrice{...ProductPriceFragment}shipPrice{...ProductPriceFragment}subscriptionPrice{priceString subscriptionString}priceDisplayCodes{priceDisplayCondition finalCostByWeight submapType}}fragment PreorderFragment on PreOrder{isPreOrder preOrderMessage preOrderStreetDateMessage}fragment ProductPriceFragment on ProductPrice{price priceString}fragment VariantCriteriaFragment on VariantCriterion{name type id isVariantTypeSwatch variantList{id images name rank swatchImageUrl availabilityStatus products selectedProduct{canonicalUrl usItemId}}}fragment InGridMarqueeAdFragment on MarqueePlaceholder{__typename type moduleLocation lazy}fragment TileTakeOverTileFragment on TileTakeOverProductPlaceholder{__typename type tileTakeOverTile{span title subtitle image{src alt}logoImage{src alt}backgroundColor titleTextColor subtitleTextColor tileCta{ctaLink{clickThrough{value}linkText title}ctaType ctaTextColor}}}fragment PageMetaDataFragment on SearchInterface{pageMetadata{storeSelectionHeader{fulfillmentMethodLabel storeDislayName}title canonical description location{addressId}}}fragment PaginationFragment on SearchInterface{paginationV2{maxPage pageProperties}}fragment RequestContextFragment on SearchInterface{requestContext{vertical isFitmentFilterQueryApplied searchMatchType categories{id name}}}fragment ErrorResponse on SearchInterface{errorResponse{correlationId source errorCodes errors{errorType statusCode statusMsg source}}}fragment InlineSearchModuleFragment on TempoWM_GLASSWWWInlineSearchConfigs{headingText placeholderText}fragment PillsModuleFragment on PillsSearchInterface{title url image:imageV1{src alt}}fragment FacetFragment on Facet{title name type layout min max selectedMin selectedMax unboundedMax stepSize isSelected values{id name description type itemCount isSelected baseSeoURL}}fragment EventTimerFragment on TempoWM_GLASSWWWEventTimerModuleConfigs{startTime endTime sunsetTime eventName eventNameColor preExpirationSubTextLong preExpirationSubTextShort postExpirationSubText backgroundColor fontColor borderColor linkBeforeExpiry{clickThrough{rawValue tag type value}linkText title uid}linkAfterExpiry{clickThrough{rawValue tag type value}linkText title uid}__typename}fragment HorizontalChipModuleConfigsFragment on TempoWM_GLASSWWWHorizontalChipModuleConfigs{chipModuleSource:moduleSource chipModule{title url{linkText title clickThrough{type value}}}chipModuleWithImages{title url{linkText title clickThrough{type value}}image{alt clickThrough{type value}height src title width}}}fragment SkinnyBannerFragment on TempoWM_GLASSWWWSkinnyBannerConfigs{desktopBannerHeight bannerImage{src title alt}mobileBannerHeight mobileImage{src title alt}clickThroughUrl{clickThrough{value}}backgroundColor heading{title fontColor}subHeading{title fontColor}bannerCta{ctaLink{linkText clickThrough{value}}textColor}}fragment ItemCarouselFragment on TempoWM_GLASSWWWItemCarouselConfigsV1{products{...ContentLayoutProduct}subTitle tileOptions{addToCart averageRatings displayAveragePriceCondition displayPricePerUnit displayStandardPrice displayWasPrice fulfillmentBadging mediaRatings productFlags productLabels productPrice productTitle}title type spBeaconInfo{adUuid moduleInfo pageViewUUID placement max}}fragment BadgesFragment on UnifiedBadge{flags{__typename...on BaseBadge{id text key query type}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought criteria{name value}}}labels{__typename...on BaseBadge{id text key}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought}}tags{__typename...on BaseBadge{id text key}}}fragment ContentLayoutProduct on Product{name badges{...BadgesFragment}canonicalUrl classType availabilityStatus showAtc averageRating snapEligible fulfillmentBadge fulfillmentSpeed fulfillmentTitle fulfillmentType itemType groupMetaData{groupType groupSubType numberOfComponents groupComponents{quantity offerId componentType productDisplayName}}imageInfo{thumbnailUrl}numberOfReviews offerId orderMinLimit orderLimit p13nDataV1{predictedQuantity flags{PREVIOUSLY_PURCHASED{text}CUSTOMERS_PICK{text}}}previouslyPurchased{label}preOrder{...PreorderFragment}priceInfo{currentPrice{...ProductPriceFragment}listPrice{...ProductPriceFragment}subscriptionPrice{priceString}priceDisplayCodes{clearance eligibleForAssociateDiscount finalCostByWeight hidePriceForSOI priceDisplayCondition pricePerUnitUom reducedPrice rollback strikethrough submapType unitOfMeasure unitPriceDisplayCondition}priceRange{minPrice maxPrice priceString}unitPrice{...ProductPriceFragment}wasPrice{...ProductPriceFragment}}rhPath salesUnit sellerId sellerName hasSellerBadge seller{name sellerId}shippingOption{slaTier shipMethod}showOptions snapEligible sponsoredProduct{spQs clickBeacon spTags}usItemId variantCount variantCriteria{name id variantList{name swatchImageUrl selectedProduct{usItemId canonicalUrl}}}}fragment EarlyAccessBeforeEventBannerFragment on TempoWM_GLASSWWWWalmartPlusEarlyAccessBeforeEventConfigsV1{earlyAccessLogo{src}dealsSubtext1 dealsSubtext2 dealsDisclaimer dealsBackground dealsLayout earlyAccessTitle earlyAccessCardMesssage earlyAccessLink1{linkText title clickThrough{value}}earlyAccessLink2{linkText title clickThrough{value}}}fragment EarlyAccessLiveEventBannerFragment on TempoWM_GLASSWWWWalmartPlusEarlyAccessDuringEventConfigsV1{earlyAccessLogo{src}dealsBackground dealsLayoutLiveEvent:dealsLayout earlyAccessTitle earlyAccessCardMesssage earlyAccessCounterLabel earlyAccessendTime earlyAccessstartTime earlyAccessendTime earlyAccesssunsetTime earlyAccessLink1{linkText title clickThrough{value}}earlyAccessLink2{linkText title clickThrough{value}}}fragment TileTakeOverProductFragment on TempoWM_GLASSWWWTileTakeOverProductConfigs{TileTakeOverProductDetails{span dwebPosition mwebPosition title subtitle image{src alt}logoImage{src alt}backgroundColor titleTextColor subtitleTextColor tileCta{ctaLink{clickThrough{value}linkText title}ctaType ctaTextColor}}}",
      "variables": {
        "id": "",
        "dealsId": "deals/electronics",
        "page": 1,
        "prg": "desktop",
        "facet": "",
        "catId": "",
        "seoPath": "/shop/deals/electronics",
        "ps": 40,
        "ptss": "",
        "trsp": "",
        "min_price": "",
        "max_price": "",
        "sort": "best_match",
        "beShelfId": "",
        "recall_set": "",
        "module_search": "",
        "storeSlotBooked": "",
        "additionalQueryParams": None,
        "searchParams": {
          "id": "",
          "dealsId": "deals/electronics",
          "query": "",
          "page": 1,
          "prg": "desktop",
          "facet": "",
          "catId": "",
          "seoPath": "/shop/deals/electronics",
          "ps": 40,
          "ptss": "",
          "trsp": "",
          "min_price": "",
          "max_price": "",
          "sort": "best_match",
          "beShelfId": "",
          "recall_set": "",
          "module_search": "",
          "storeSlotBooked": "",
          "additionalQueryParams": None,
          "cat_id": "",
          "_be_shelf_id": "",
          "pageType": "DealsPage"
        },
        "query": None,
        "pageType": "DealsPage",
        "enablePortableFacets": True
      }
    })
    headers = {
      'authority': 'www.walmart.com',
      'accept': 'application/json',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/json',
      'cookie': 'auth=MTAyOTYyMDE46eSyUeTa%2Fv4pI2s6PBa83b5K0U%2BdGkCojRKZVOWn3urPhZyNj2jYG7tkT0pVyPxo9GKPzTD0pGpv2RM7NErgk5PcMpNAjyeH%2FqR2osYms9gNtKYb4re5AV%2BBCBX4OjKy767wuZloTfhm7Wk2KcjygmNzsF5Ho8U7SJCh0TVScOnW406j4SVKcsQ4w54f2lXiZBbTpgbwiIK6lG7z6bh3cpgMxSue62QqElfFXVK953YUMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKrg%2BSnUMovXgmsFTtpNQgnvfMxbdOMUgth4wnir6U08mfbQX2GxOurGXk1C7A2NKPONY%2B8x92GCg4milNtkAtD3jFkh%2F4%2Fv5UrKAEV8vumyKB80cuj%2BjHcAFz2c8Wa3tR4SQzX7MAlLBJXxL%2Bwi6fx6Y%3D; ACID=8b5d96e5-d35e-4dba-9108-e4744c3b8bc0; hasACID=true; assortmentStoreId=1062; hasLocData=1; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; vtc=bKu3Y-uBs5XU3Iam0Mj7iM; bstc=bKu3Y-uBs5XU3Iam0Mj7iM; mobileweb=0; xpa=-wnVY|0t4gT|2MlgW|5eRjg|7qRDz|8wp7a|A7sVv|BIcmp|BXtVZ|Bpclf|DAwQd|Dmnts|EjkLl|HF4Pf|HmBmS|IJVMl|MfFwr|Pgtnl|V-nnO|YkREw|_-wfu|_hSAz|ccDGr|duBe9|gDOrs|kFqfr|qcwx4|qlyhA|qyn67|zCylr; exp-ck=0t4gT18wp7a2A7sVv3Bpclf1DAwQd3Dmnts3EjkLl1HF4Pf1IJVMl1MfFwr2Pgtnl1V-nnO1_hSAz1ccDGr1kFqfr1qcwx41qlyhA1qyn672; helpgql=1; TS013ed49a=01538efd7c9033859d551de85f5a5f2d7b226480192f62d4149cf44050c46557a2792bed85d5cc0e4735d50ba2d91cfe5dd23b3034; TBV=7; adblocked=false; dimensionData=1007; xpm=1%2B1655119540%2BbKu3Y-uBs5XU3Iam0Mj7iM~%2B0; _pxvid=8f8e98bf-eb0b-11ec-873a-795a71497767; pxcts=8f8ea463-eb0b-11ec-873a-795a71497767; ak_bmsc=72B4F36C1D147AE073342A27C83F30F1~000000000000000000000000000000~YAAQn8pNF1v7BVuBAQAA+/rPXBC/1FdEPeY5nof3aFbqYdVOBEAdyHzWlg8jnM1RP9SU0Q6RFwyt0V08Ra0zh0KNGhkTSKKsthXO8vSqJl9JDMwDNrIoXIuo6ON5BKXpAIXEd9LqNHMKG1fEVojPnjnqGjCMPeblJx/Wi8U5Qw/P2I4I/d6w1MXZerCtemTMFEPD2E0685bwOqk7DEBJH6A69/s1ojKE8hjAw7WALwXBH0ByguJXd00U3fptKHLgxi+loxE2DYUfyZQuspBmE0FwipE5Rsav5tLzuYPZuQLpR09uhdfH7mmeAMQxB7wJsmRP89cS6Ea//GKJQiQauWgstp1sRKR0S/KDFFj/I1cWV5DemCYqIMUSZCBmBY1DM4hOnB1mXX6TkgnIHjzDmMRhju2QHdYvzeV0d8jh9AjTqOrEEOG14/55f6Z/qW5eP0iojrrAWUkZ8pcJgKqo+Y+VMAlP2chNNQf5PXFkqXSWpzTJAWK+ekZq89k=; tb_sw_supported=true; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIxMDYyIiwiZGlzcGxheU5hbWUiOiJGcmllbmRzd29vZCBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI3NzU0NiIsImFkZHJlc3NMaW5lMSI6IjE1MCBXIEVsIERvcmFkbyBCbHZkIiwiY2l0eSI6IkZyaWVuZHN3b29kIiwic3RhdGUiOiJUWCIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiNzc1NDYtNjUwMCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6MjkuNTUxODYzLCJsb25naXR1ZGUiOi05NS4xNTkyMTN9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIxMDYyIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkJBS0VSWV9QSUNLVVAiLCJQSUNLVVBfQ1VSQlNJREUiLCJQSUNLVVBfSU5TVE9SRSIsIlBJQ0tVUF9TUEVDSUFMX0VWRU5UIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjoyOS41NDEyLCJsb25naXR1ZGUiOi05NS4xMzcxLCJwb3N0YWxDb2RlIjoiNzc1OTgiLCJjaXR5IjoiV2Vic3RlciIsInN0YXRlIjoiVFgiLCJjb3VudHJ5Q29kZSI6IlVTQSIsImdpZnRBZGRyZXNzIjpmYWxzZX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMTA2MiIsImRpc3BsYXlOYW1lIjoiRnJpZW5kc3dvb2QgU3VwZXJjZW50ZXIiLCJhY2Nlc3NQb2ludHMiOm51bGwsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbXSwiaW50ZW50IjoiUElDS1VQIiwic2NoZWR1bGVFbmFibGVkIjpmYWxzZX0sImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMTA2MiIsImRpc3BsYXlOYW1lIjoiRnJpZW5kc3dvb2QgU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiNzc1NDYiLCJhZGRyZXNzTGluZTEiOiIxNTAgVyBFbCBEb3JhZG8gQmx2ZCIsImNpdHkiOiJGcmllbmRzd29vZCIsInN0YXRlIjoiVFgiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6Ijc3NTQ2LTY1MDAifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjI5LjU1MTg2MywibG9uZ2l0dWRlIjotOTUuMTU5MjEzfSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiYWNjZXNzUG9pbnRzIjpbeyJhY2Nlc3NUeXBlIjoiREVMSVZFUllfQUREUkVTUyJ9XSwiaHViTm9kZUlkIjoiMTA2MiIsImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXX0sImluc3RvcmUiOmZhbHNlLCJyZWZyZXNoQXQiOjE2NTUxNDExNDMwMzYsInZhbGlkYXRlS2V5IjoicHJvZDp2Mjo4YjVkOTZlNS1kMzVlLTRkYmEtOTEwOC1lNDc0NGMzYjhiYzAifQ%3D%3D; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjEwNjIiLCJ0aW1lc3RhbXAiOjE2NTUxMTk1NDMwMjV9LCJwb3N0YWxDb2RlIjp7InRpbWVzdGFtcCI6MTY1NTExOTU0MzAyNSwiYmFzZSI6Ijc3NTk4In0sInZhbGlkYXRlS2V5IjoicHJvZDp2Mjo4YjVkOTZlNS1kMzVlLTRkYmEtOTEwOC1lNDc0NGMzYjhiYzAifQ%3D%3D; TB_SFOU-100=1; QuantumMetricUserID=9319d2cf05213a5f81fdbe1f40a68c59; QuantumMetricSessionID=7809ad4988eee68360058a33496b0390; _astc=c7b3d549f7946bcb21b88ee9665cf69b; _pxff_tm=1; akavpau_p2=1655120522~id=ae1ac1bf1dc3f5f1397c51c8c14a0922; _px3=fb900ea0206d0c62c28859c7b1ed6252f121d2ce6c91e65949f1412dbee647aa:5AFXyiVd6WRjguiSn8PTGNS9OFlfw8lYELxSKOEhFy7nshTVef1OZHteB4dlE7LyhJaeTOPTExt4k1kUCBFSQQ==:1000:IogkuoqT3sKYdI9euWVyKXVX5xMKswp7aXpQqOIcTO4cc+J+M8ddpe6s5uLnFXtAWLFONmeK/SrBbJIGzseaDweYxEr8zwlycY+0+mkjcN5ZqvKMCQQtU4dJS2KBwWCl08ogTz6h+6d6dNACzLBlVroyMAF1oeiWWaYBas5omowKNjJir+CD9kE12oLL+SCSI4icn5SacXoOil1mXJkFyg==; xptwg=1891525273:1DDACA321379380:4D78B8B:A4637474:73F9B339:7FFF7D39:; TS01b0be75=01538efd7cfa82b938b8a5ef93bc150b4eb9e15357897ecf78ad55dba50f4dc7ffdeb602e2e8bf210678c9310e042d1f6a71e16750; bm_sv=CC66B24784BE5EB1E59000ADAD5744FF~YAAQncpNF0IaYSiBAQAAI8fVXBCh/6oou8/HBUSrI+5Sr7OSWuTygKKE6huamp4mwGdCAwXQY4OyjjOxm0AN1GVmBAW3z2Prh4Txs0J+uDDpWvmq6X/ID/kqp0T4tS/+eUEsa6YbnbptMSHxqXguu9Pn0xaZK8OV8O/L8jTvT9U93CPRCBa8LLx9wZ9MXClKEL5e3/H4Zz8WBq6QYFWM6ECvdt2qvr7jDvxZE3NP/uxL78MUcC6VqHzDzKQeqpSF/yI=~1; ACID=a0df90fd-cfef-47ba-a8f3-e3cd371b35e2; hasACID=true; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsInN0b3JlSW50ZW50IjoiUElDS1VQIiwibWVyZ2VGbGFnIjpmYWxzZSwiaXNEZWZhdWx0ZWQiOmZhbHNlLCJwaWNrdXAiOnsibm9kZUlkIjoiMTA2MiIsInRpbWVzdGFtcCI6MTY1NDczOTcxOTA2OH0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjU0NzM5NzE5MDY4LCJiYXNlIjoiNzc1OTgifSwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOmEwZGY5MGZkLWNmZWYtNDdiYS1hOGYzLWUzY2QzNzFiMzVlMiJ9; vtc=X82_KfO9nmPPCumkUhoevg',
      'device_profile_ref_id': 'w9nFaMk0vRRIZIy815zgjg_KAolgIjFaUhb8',
      'origin': 'https://www.walmart.com',
      'referer': 'https://www.walmart.com/shop/deals/electronics',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'traceparent': 'QUf_55E_0KnDQQ5IwZXKurtXYcYdhdiSTThp',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
      'wm_mp': 'true',
      'wm_page_url': 'https://www.walmart.com/shop/deals/electronics',
      'wm_qos.correlation_id': 'QUf_55E_0KnDQQ5IwZXKurtXYcYdhdiSTThp',
      'x-apollo-operation-name': 'Deals',
      'x-enable-server-timing': '1',
      'x-latency-trace': '1',
      'x-o-bu': 'WALMART-US',
      'x-o-ccm': 'server',
      'x-o-correlation-id': 'QUf_55E_0KnDQQ5IwZXKurtXYcYdhdiSTThp',
      'x-o-gql-query': 'query Deals',
      'x-o-mart': 'B2C',
      'x-o-platform': 'rweb',
      'x-o-platform-version': 'main-496-dfe8cb',
      'x-o-segment': 'oaoh'
    }


  
    return requests.request("POST", url, headers=headers, data=payload)
  
      #print(r.text)
  
  r = url_request()
  data = json.loads(r.text)
  wally_db=[]
  
  # This is added so that many files can reuse the function get_database()
      # Get the database

  important_data = data['data']['search']['searchResult']['itemStacks'][0]
  # print(important_data)
  
  for item in important_data['itemsV2']:
    total_price = 0
    try:
        price = float(item['priceInfo']['currentPrice']['price'])
        if item['priceInfo']['shipPrice'] == None:
            shipping_price = 0
        else:
            total_price = float(item['priceInfo']['currentPrice']['price']) + float(    item['priceInfo']['shipPrice'])
        if total_price == 0:
          total_price = float(item['priceInfo']['currentPrice']['price'])
        #print(item['usItemId'])
        #print(item['name'])
        #print("New Price $" + str(total_price))
        try:
          #print("Old Price " + item['priceInfo']['listPrice']['priceString'])
          old_price = item['priceInfo']['listPrice']['priceString']
        finally:
            discount = str(round((1-total_price/item['priceInfo']['listPrice']['price'])*100,0))
            #print("Discount "+discount+ "%")
            #print("https://www.walmart.com" + item['canonicalUrl'])
            #print("-------------------------------")
            #if()
            temp =collection_name.find_one({"_id": item['_id']})
            #if temp == None or temp['total_price'] !=total_price:
            item_1 = {
                    "_id":item['usItemId'],
                    "name": item['name'],
                    "total_price": total_price,
                    "old_price": item['priceInfo']['listPrice']['price'],
                    "discount": discount,
                    "imageInfo": item['imageInfo']['thumbnailUrl'],
                    "url": "https://www.walmart.com" + item['canonicalUrl']
            }
            collection_name.insert_one(item_1)
            wally_db.append(item_1)
    except:
        pass
  return wally_db

def get_discount(wally_db):
    return wally_db['discount']


def sort(wally_db):
  wally_db.sort(key=get_discount, reverse=True)
  db["walmart_items"] = wally_db
  return wally_db

def update_url (url):
  if "urls" in db.keys():
    urls = db["urls"]
    urls.append(url)
    db["urls"] = urls
  else:
    db["urls"] = [url]

def remove_url (url):
    if "urls" in db.keys():
      urls = db["urls"]
      urls.remove(url)
      db["urls"] = urls

def list_url():
  results=""
  if "urls" in db.keys():
    urls = db["urls"]
    for x in range(len(urls)):
      results = results + urls[x]+" "
  else:
    results = "No URLs"    
  return results

@client.event
async def on_ready():
  print('We have loggined as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$wbot rem url '):
    url = message.content.replace('$wbot rem url ','')
    remove_url(url)
    await message.channel.send("URL "+url+ " was succesfully removed.")
      
  if message.content.startswith('$wbot add url '):
    url = message.content.replace('$wbot add url ','')
    update_url(url)
    await message.channel.send("URL "+url+ " was succesfully added.")
      
  if message.content == '$wbot list':
    url_list = list_url()
    await message.channel.send(url_list)

  if message.content == '$wbot start':
    while True:
      result = start()
      #result = sort(result1)
      for item in result:      
        embed = discord.Embed(
          title = item['name'],
          #description = 'This is a description.',
          colour = discord.Colour.blue(),
          url = item['url']
        )
        embed.set_footer(text = 'Walmart Bot V1',icon_url=w_url)
        #embed.set_image(url='')
        embed.set_thumbnail(url=item['imageInfo'])
        embed.set_author(name =  'Walmart Bot V1',icon_url=w_url)
        #message.channel.send("Name " + result["name"])
        embed.add_field(name='Discount:',value = str(item['discount']) + '%', inline=True)
        embed.add_field(name='Original:',value = '$'+str(item['old_price']), inline=True)
        embed.add_field(name='Discounted:',value = '$'+ str(item['total_price']), inline=True)
        #await message.channel.send("Current Price $" + str(item["total_price"]))
        #await message.channel.send("Old Price $" + str(item["old_price"]))
        #await message.channel.send("Discount " + str(item["discount"])+"%")
        #await message.channel.send("Url " + item["url"])
        await message.channel.send(embed=embed)
        time.sleep(5)
    time.sleep(600)
    
client.run(my_secret)

