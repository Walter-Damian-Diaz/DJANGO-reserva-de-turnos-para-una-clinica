$(document).ready(function() {
    var table = $('#example').DataTable( {
        rowReorder: {
            selector: 'td:nth-child(2)'
        },
        responsive: true,

        "language": {
            "emptyTable":			"<i>No hay datos disponibles en la tabla.</i>",
            "info":		   		"Del _START_ al _END_ de _TOTAL_ ",
            "infoEmpty":			"Mostrando 0 registros de un total de 0.",
            "infoFiltered":			"(filtrados de un total de _MAX_ registros)",
            "infoPostFix":			"(actualizados)",
            "lengthMenu":			"Mostrar _MENU_ registros",
            "loadingRecords":		"Cargando...",
            "processing":			"Procesando...",
            "search":			"<span style='font-size:25px;'>Buscar:</span>",
            "searchPlaceholder":		"Dato para buscar",
            "zeroRecords":			"No se han encontrado coincidencias.",
            "paginate": {
                "first":			"Primera",
                "last":				"Última",
                "next":				"Siguiente",
                "previous":			"Anterior"
            },
            "aria": {
                "sortAscending":	"Ordenación ascendente",
                "sortDescending":	"Ordenación descendente"
            }
        },

        
    } );
} );