$(".hamburger").on("click", function() {
    $("#sidebarExtension").toggleClass("closed");

    $(".dashboardItem").toggleClass("navbarExtended");
});