
window.addEventListener("load", () => {
    document.querySelector(".main").classList.remove("hidden");
    document.querySelector(".home-section").classList.add("active");
    /* Page Loader */
    document.querySelector(".page-loader").classList.add("fade-out")
    setTimeout(() =>{
        document.querySelector(".page-loader").style.display = "none";
    },1500);
});

/* ----------------- Toggle Navbar ----------------------- */

const navToggler = document.querySelector(".nav-toggler");
navToggler.addEventListener("click", () => {
    hideScetion();
    toggleNavbar();
    document.body.classList.toggle("hide-scrolling");
});
function hideScetion(){
    document.querySelector("section.active").classList.toggle("fade-out");
}
function toggleNavbar(){
    document.querySelector(".header").classList.toggle("active");
}

/* ----------------- Active Section ----------------------- */

document.addEventListener("click", (e) => {
    if(e.target.classList.contains("link-item") && e.target.hash !== ""){
        document.querySelector(".overlay").classList.add("active");
        navToggler.classList.add("hide");
        if(e.target.classList.contains("nav-item")){
            toggleNavbar();
        }
        else{
            hideScetion();
            document.body.classList.add("hide-scrolling");
        }
        setTimeout(() =>{
            document.querySelector("section.active").classList.remove("active","fade-out");
            document.querySelector(e.target.hash).classList.add("active");
            window.scrollTo(0,0);
            document.body.classList.remove("hide-scrolling");
            navToggler.classList.remove("hide");
            document.querySelector(".overlay").classList.remove("active");
        },500);
    }
});

/* ----------------- Day section ----------------------- */


function imgSlider(anything){
    document.querySelector('.item_img').src = anything;

}
function changeCircleColor(color){
    const circle = document.querySelector('.circle');
    circle.style.background = color;
}
