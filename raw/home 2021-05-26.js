var canAnimate = true;

$(document).ready(function () {

    // // Animacion de numeros
    let waypoint_numbers = new Waypoint({
        element: document.getElementsByClassName('numbers')[1],
        handler: function (direction) {

            const obj = $('.datoprincipal').get(0);
            if (canAnimate) {
                $(this.element).css('opacity', 0);
                $(this.element).addClass('animate__fadeInUp animate__animated');
                //animateValue(obj, 0, 15, 1700);
                animarDatos();
            }
            $('.container-vaccine .contenedor-contenido-tabs .contenido-tab:nth-child(2) .vaccine-content .img-vaccine .cont-animacion .cont-contenido').addClass("actual");

        },
        offset: '100%',
        triggerOnce: true
    });

    // // Waypoints fade in

    // DEJAR EN FADEIN porque FadeInUp hace fallar el tooltip de Mexico
    $('.contenedor-wrapper')
        .css({ 'opacity': '0' })
        .waypoint(function (direction) {
            if (direction === 'down') {
                $(this.element).addClass('animate__fadeIn animate__animated');
            }

        }, {
            offset: '75%',
            triggerOnce: true
        });

    $('.contenedor-tabs')
        .css({ 'opacity': '0' })
        .waypoint(function (direction) {
            if (direction === 'down') {
                $(this.element).addClass('animate__fadeIn animate__animated');
            }

        }, {
            offset: '75%',
            triggerOnce: true
        });

    // // Click en etapas
    $('.cont-item').on('click', function (e) {
        e.preventDefault();
        if (!$(this).hasClass('active')) {
            $('.cont-item').removeClass('active');
            $(this).addClass('active');
        }
    });

    var actualInicial = $('.container-vaccine .contenedor-tabs .tab.btn-active:nth-child(2)').attr("valorPrincipal");
    var actualPosicion = $('.container-vaccine .contenedor-tabs .tab.btn-active:nth-child(2)').attr("valorPosition");
    $("<style type='text/css'> .container-vaccine .vaccine-content .img-vaccine .cont-animacion .cont-contenido.actual { width: " + actualInicial + "%; } .container-vaccine .vaccine-content .img-vaccine .numbers{ left: " + actualPosicion + "%; } </style>").appendTo("head");

    // Click Vacuna
    $('.container-vaccine .contenedor-tabs .tab.btn-active').on('click', function (e) {
        var valorPrincipal = $(this).attr("valorPrincipal");
        var valorPosition = $(this).attr("valorPosition");
        e.preventDefault();
        if (!$(this).hasClass('active')) {
            $('.container-vaccine .contenedor-tabs .tab.active').removeClass('active');
            $(this).addClass('active');
            var indice = $(this).attr("tab");
            $(".container-vaccine .contenedor-contenido-tabs .contenido-tab").hide();
            $(".container-vaccine .contenedor-contenido-tabs .contenido-tab").eq(indice - 1).fadeIn(500);
            //animarDatos();
            $('.container-vaccine .vaccine-content .img-vaccine .cont-animacion .cont-contenido').removeClass("actual");

            $('.container-vaccine .vaccine-content .img-vaccine .cont-animacion .cont-contenido').css("width", "");

            //$('.container-vaccine .contenedor-contenido-tabs .contenido-tab:nth-child('+ indice +') .vaccine-content .img-vaccine .cont-animacion .cont-contenido').addClass("actual");

            $('.container-vaccine .contenedor-contenido-tabs .contenido-tab:nth-child(' + indice + ') .vaccine-content .img-vaccine .cont-animacion .cont-contenido').animate({
                width: valorPrincipal + '%'
            });
            $('.container-vaccine .contenedor-contenido-tabs .contenido-tab:nth-child(' + indice + ') .vaccine-content .img-vaccine .numbers').css("left", valorPosition + '%');

            $('.container-vaccine .contenedor-contenido-tabs .contenido-tab:nth-child(' + indice + ') .datos-vacunacion').addClass('animate__fadeInUp animate__animated');
        }
    });




    // VACUNADOS MAPA
    let vacunas_data = [
        {
            "Estado": "Aguascalientes",
            "vacunados": "135,446"
        },
        {
            "Estado": "Baja California",
            "vacunados": "236,531"
        },
        {
            "Estado": "Baja California Sur",
            "vacunados": "84,606"
        },
        {
            "Estado": "Campeche",
            "vacunados": "163,147"
        },
        {
            "Estado": "Chiapas",
            "vacunados": "221,403"
        },
        {
            "Estado": "Chihuahua",
            "vacunados": "290,929"
        },
        {
            "Estado": "CDMX",
            "vacunados": "1,870,855"
        },
        {
            "Estado": "Coahuila",
            "vacunados": "321,216"
        },
        {
            "Estado": "Colima",
            "vacunados": "81,319"
        },
        {
            "Estado": "Durango",
            "vacunados": "164,374"
        },
        {
            "Estado": "Estado de México",
            "vacunados": "1,832,243"
        },
        {
            "Estado": "Guanajuato",
            "vacunados": "559,477"
        },
        {
            "Estado": "Guerrero",
            "vacunados": "227,832"
        },
        {
            "Estado": "Hidalgo",
            "vacunados": "351,953"
        },
        {
            "Estado": "Jalisco",
            "vacunados": "779,491"
        },
        {
            "Estado": "Michoacán",
            "vacunados": "390,117"
        },
        {
            "Estado": "Morelos",
            "vacunados": "228,990"
        },
        {
            "Estado": "Nayarit",
            "vacunados": "124,018"
        },
        {
            "Estado": "Nuevo León",
            "vacunados": "412,740"
        },
        {
            "Estado": "Oaxaca",
            "vacunados": "265,270"
        },
        {
            "Estado": "Puebla",
            "vacunados": "355,973"
        },
        {
            "Estado": "Querétaro",
            "vacunados": "191,274"
        },
        {
            "Estado": "Quintana Roo",
            "vacunados": "125,066"
        },
        {
            "Estado": "San Luis Potosí",
            "vacunados": "199,505"
        },
        {
            "Estado": "Sinaloa",
            "vacunados": "340,301"
        },
        {
            "Estado": "Sonora",
            "vacunados": "332,421"
        },
        {
            "Estado": "Tabasco",
            "vacunados": "169,433"
        },
        {
            "Estado": "Tamaulipas",
            "vacunados": "257,685"
        },
        {
            "Estado": "Tlaxcala",
            "vacunados": "138,201"
        },
        {
            "Estado": "Veracruz",
            "vacunados": "674,202"
        },
        {
            "Estado": "Yucatán",
            "vacunados": "196,926"
        },
        {
            "Estado": "Zacatecas",
            "vacunados": "130,755"
        }
    ];

    //vacunas_data.forEach(function (item, index) {
      //  $("path[data-title='" + item.Estado + "']").attr('data-vacunados', item.vacunados);
    //});

    // let path_states = $('#primaryMap path');
    // // console.log(path_states);
    // for (let i = 0; i < path_states.length; i++) {
    //     console.log($(path_states[i]).attr('data-state_name'));
    // }

});

// Animate Numbers
function animateValue(obj, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        obj.innerHTML = numberWithCommas(Math.floor(progress * (end - start) + start));
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    canAnimate = false;
    window.requestAnimationFrame(step);
}

// Formmatting numbers
function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}



Number.prototype.format = function (n) {
    var r = new RegExp('\\d(?=(\\d{3})+' + (n > 0 ? '\\.' : '$') + ')', 'g');
    return this.toFixed(Math.max(0, Math.floor(n))).replace(r, '$&,');
};

function animarDatos() {
    $('.count').each(function () {
        $(this).prop('counter', 0).animate({
            counter: $(this).text().replace(/,/g, "")
        }, {
            duration: 1700,
            easing: 'easeOutExpo',
            step: function (step) {
                $(this).text('' + step.format());
            }
        });
    });
}