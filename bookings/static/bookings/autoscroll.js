document.addEventListener("DOMContentLoaded", function () {
    const movieScroll = document.getElementById("movie-scroll");
    let scrollAmount = 0;
    const scrollStep = 220; 
    const scrollDelay = 4000; 

    function autoScroll() {
        if (scrollAmount < movieScroll.scrollWidth - movieScroll.clientWidth) {
            scrollAmount += scrollStep;
        } else {
            scrollAmount = 0;
        }
        movieScroll.scrollTo({
            left: scrollAmount,
            behavior: "smooth"
        });
    }

    setInterval(autoScroll, scrollDelay);
});
