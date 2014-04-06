$(document).ready(function() { 
    $("#shop-owl").owlCarousel({ 
        items: 3,
        itemsDesktop: [1440, 3],
        autoPlay: 6000,
        stopOnHover: true,
        navigation: true,
        navigationText: ["Forrige", "Næste"],  
        responsive: true,
        responsiveRefreshRate: 1000,
        responsiveBaseWidth: '#main-content-container',
        lazyLoad:true,
    }); 
});