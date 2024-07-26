let linkArray = [
    ["https://search.marginalia.nu/", "Try the 'random' button! - as it says " +
     " 'attempts to show you sites you perhaps weren't aware of in favor of the sort of sites you probably already knew existed.'."],
    ["https://drawing.garden","A garden :)"],
    ["https://rain.computer/","A very cute personal site"],
    ["https://dreamwiki.sixey.es/","Weird ascii art"],
    ["https://mcmansionhell.com/","Recently rediscovered McMansion and the annotated images. I'd reccommend you skip down to the 'texas gothic revival' post and start there."],
    ["https://goblin-heart.net/sadgrl/magnet-poetry/","An online magnet poetry maker"],
    ["https://www.pcgamer.com/the-metaverse-is-bullshit/","Enjoyed this pcgamer metaverse rant."],
    ["https://www.cs.cmu.edu/~sef/sefSmiley.htm", "Short webpage written by the guy who invented the smiley face :-)"],
    ["https://www.shortboxcomicsfair.com/", "The shortbox digital comics fair has an amazing selection of digital comics to browse - it starts in Oct but you can still check out the exhibitors."]
]
function randChoice(size) {
    return Math.floor(Math.random() * size)
}
function getRandomImg() {
    var randNo = randChoice(9) + 1
    var api_url = "https://api.microlink.io/?url=" + linkArray[randNo - 1][0]
    document.getElementById('random-link').setAttribute('href', linkArray[randNo - 1][0]);
    document.getElementById('description').innerHTML = linkArray[randNo - 1][1];
    document.getElementById('random-link-api').setAttribute('api', api_url);
    //document.getElementById('aside').innerHTML = descriptionArray[randNo - 1]

}