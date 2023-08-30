// Messages boostrap
window.setTimeout(() => {
    $(".alert").fadeTo(2000, 0).slideDown(2000,()=> {
        $(this).remove();
    });;
}, 1000);

// sweetalert2 libreria cuadro de dialogos

function confirmar(e) {
    const confirmacion = confirm('¿Seguro que quiere eliminarlo?')
    if (!confirmacion){
        e.preventDefault()
    }
}

const btn_eliminar_cliente = $('#btn-eliminar-cliente');
const btn_eliminar_localidad = $('#btn-eliminar-localidad');

$(btn_eliminar_cliente).on('click', function (e) {
    confirmar(e)
});

$(btn_eliminar_localidad).on('click',function (e) { 
    confirmar(e)
});