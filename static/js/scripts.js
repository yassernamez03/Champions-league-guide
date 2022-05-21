function big(e) {
    e.style.transform  = "scale(120%)"
}
function small(e) {
    e.style.transform  = "scale(100%)"
}
i = 1
t = document.querySelectorAll('.team')
t.forEach(element => {
    i = 1
    element.addEventListener('click',e=>{
        if (i==1){big(element)
            i = 0 
        }
        else if(i==0){small(element)
            i = 1
        } 
    })
});

