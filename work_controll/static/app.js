var btn_green = document.querySelector('.btn-green');
var btn_red = document.querySelector('.btn-red');

btn_green.addEventListener('click', greenChange)


function greenChange() {
    btn_green.style.backgroundColor = 'green';
    if (btn_green.style.backgroundColor == 'green') {
        btn_red.style.backgroundColor = 'grey'
    }
}
btn_red.addEventListener('click', redChange)

function redChange() {
    btn_red.style.backgroundColor = 'red';
    if (btn_red.style.backgroundColor == 'red') {
        btn_green.style.backgroundColor = 'grey'
    }
}


