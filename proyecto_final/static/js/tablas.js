
$('#tablapreuba').DataTable({
    responsive: true,
    paging: true,
    pageLength:10,
    lengthChange:true,
    autoWidth: true,
    searching: true,
    bInfo: true,
    bSort: true,
    dom: 'lBfrtip',
    buttons:[
        {
        extend: 'copy',
        text: '<i class="fas fa-clone"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Copiar',
        exportOptions:{
            columns:[0,1]
            }   
        },
        {
            extend: 'excel',
            text: '<i class="fas fa-file-excel"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Exel',
            exportOptions:{
                columns:[0,1]
                }   
        },
        {
            extend: 'print',
            text: '<i class="fas fa-print"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Imprimir',
            exportOptions:{
                columns:[0,1]
            },
            customize: function( win ){
                $(win.document.body).css('font-size','10pt')
                $(win.document.body).find('table')
                    .addClass('compact')
                    .css('font-size','inherit');
            }   
        },
        {
            extend: 'pdf',
            text: '<i class="fas fa-pdf"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'PDF',
            exportOptions:{
                columns:[0,1]
            },
            customize: function( win ){
                $(win.document.body).css('font-size','10pt')
                $(win.document.body).find('table')
                    .addClass('compact')
                    .css('font-size','inherit');
            }   
        }
        
    ],
    "language":{
        "url": "https://cdn.datatables.net/plug-ins/1.12.1/i18n/es-ES.json"
    }
})

$('#inventario').DataTable({
    responsive: true,
    paging: true,
    pageLength:10,
    lengthChange:true,
    autoWidth: true,
    searching: true,
    bInfo: true,
    bSort: true,
    dom: 'lBfrtip',
    buttons:[
        {
        extend: 'copy',
        text: '<i class="fas fa-clone"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Copiar',
        exportOptions:{
            columns:[1,2,3,4]
            }   
        },
        {
            extend: 'excel',
            text: '<i class="fas fa-file-excel"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Exel',
            exportOptions:{
                columns:[1,2,3,4]
                }   
        },
        {
            extend: 'print',
            text: '<i class="fas fa-print"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Imprimir',
            exportOptions:{
                columns:[1,2,3,4]
            },
            customize: function( win ){
                $(win.document.body).css('font-size','10pt')
                $(win.document.body).find('table')
                    .addClass('compact')
                    .css('font-size','inherit');
            }   
        },
        {
            extend: 'pdf',
            text: '<i class="fas fa-file-pdf"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'PDF',
            exportOptions:{
                columns:[1,2,3,4]
            },
            tableHeader:{
                alignment: 'center'
            },
            customize:function (doc){
                doc.styles.tableHeader.alignment= 'center';
                doc.styles.tableBodyOdd.alignment= 'center';
                doc.styles.tableBodyEven.alignment= 'center';
                doc.styles.tableHeader.fontSize= 7;
                doc.defaultStyle.fontSize= 6;
                doc.content[1].table.widths= Array(doc.content[1].table.body[1].length + 1).join('*').split('');
            }
            
        }
        
    ],
    "language":{
        "url": "https://cdn.datatables.net/plug-ins/1.12.1/i18n/es-ES.json"
    }
})


$('#servicios').DataTable({
    responsive: true,
    paging: true,
    pageLength:10,
    lengthChange:true,
    autoWidth: true,
    searching: true,
    bInfo: true,
    bSort: true,
    dom: 'lBfrtip',
    buttons:[
        {
        extend: 'copy',
        text: '<i class="fas fa-clone"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Copiar',
        exportOptions:{
            columns:[1,2,3,4,5]
            }   
        },
        {
            extend: 'excel',
            text: '<i class="fas fa-file-excel"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Exel',
            exportOptions:{
                columns:[1,2,3,4,5]
                }   
        },
        {
            extend: 'print',
            text: '<i class="fas fa-print"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Imprimir',
            exportOptions:{
                columns:[1,2,3,4,5]
            },
            customize: function( win ){
                $(win.document.body).css('font-size','10pt')
                $(win.document.body).find('table')
                    .addClass('compact')
                    .css('font-size','inherit');
            }   
        },
        {
            extend: 'pdf',
            text: '<i class="fas fa-file-pdf"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'PDF',
            exportOptions:{
                columns:[1,2,3,4,5]
            },
            tableHeader:{
                alignment: 'center'
            },
            customize:function (doc){
                doc.styles.tableHeader.alignment= 'center';
                doc.styles.tableBodyOdd.alignment= 'center';
                doc.styles.tableBodyEven.alignment= 'center';
                doc.styles.tableHeader.fontSize= 7;
                doc.defaultStyle.fontSize= 6;
                doc.content[1].table.widths= Array(doc.content[1].table.body[1].length + 1).join('*').split('');
            }
            
        }
        
    ],
    "language":{
        "url": "https://cdn.datatables.net/plug-ins/1.12.1/i18n/es-ES.json"
    }
})

$('#colaborador').DataTable({
    responsive: true,
    paging: true,
    pageLength:10,
    lengthChange:true,
    autoWidth: true,
    searching: true,
    bInfo: true,
    bSort: true,
    dom: 'lBfrtip',
    buttons:[
        {
        extend: 'copy',
        text: '<i class="fas fa-clone"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Copiar',
        exportOptions:{
            columns:[1,2,3,4,5,6]
            }   
        },
        {
            extend: 'excel',
            text: '<i class="fas fa-file-excel"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Exel',
            exportOptions:{
                columns:[1,2,3,4,5,6]
                }   
        },
        {
            extend: 'print',
            text: '<i class="fas fa-print"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Imprimir',
            exportOptions:{
                columns:[1,2,3,4,5,6]
            },
            customize: function( win ){
                $(win.document.body).css('font-size','10pt')
                $(win.document.body).find('table')
                    .addClass('compact')
                    .css('font-size','inherit');
            }   
        },
        {
            extend: 'pdf',
            text: '<i class="fas fa-file-pdf"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'PDF',
            exportOptions:{
                columns:[1,2,3,4,5,6]
            },
            tableHeader:{
                alignment: 'center'
            },
            customize:function (doc){
                doc.styles.tableHeader.alignment= 'center';
                doc.styles.tableBodyOdd.alignment= 'center';
                doc.styles.tableBodyEven.alignment= 'center';
                doc.styles.tableHeader.fontSize= 7;
                doc.defaultStyle.fontSize= 6;
                doc.content[1].table.widths= Array(doc.content[1].table.body[1].length + 1).join('*').split('');
            }
            
        }
        
    ],
    "language":{
        "url": "https://cdn.datatables.net/plug-ins/1.12.1/i18n/es-ES.json"
    }
})

var minDate, maxDate;
 
// Custom filtering function which will search data in column four between two values
$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        let min = moment($('#min').val(), 'YYYY-DD-MM', true).isValid() ?
            moment($('#min').val(), 'YYYY-DD-MM', true).unix() :
            null;
        
         let max = moment($('#max').val(), 'YYYY-DD-MM').isValid() ?
             moment( $('#max').val(), 'YYYY-DD-MM', true ).unix():
             null;
        var date = moment( data[4], 'YYYY-DD-MM', true ).unix();
      
      console.log("min: " + min + ' ' + $('#min').val())
      console.log($('#min').val() + ": " + moment($('#min').val(), 'YYYY-DD-MM', true).isValid())
      console.log("max: " + max + ' ' + $('#min').val())

        if (
            ( min === null && max === null ) ||
            ( min === null && date <= max ) ||
            ( min <= date   && max === null ) ||
            ( min <= date   && date <= max )
        ) {
            return true;
        }
        return false;
    }
);
 
$(document).ready(function() {
    // Create date inputs
    minDate = new DateTime($('#min'), {
        format: 'YYYY-DD-MM'
    });
    maxDate = new DateTime($('#max'), {
        format: 'YYYY-DD-MM'
    });
 
    // DataTables initialisation
    var table = $('#servicios').DataTable();
 
    // Refilter the table
    $('#min, #max').on('change', function () {
        table.draw();
    });
});

$(document).ready(function() {
    // Create date inputs
    minDate = new DateTime($('#min'), {
        format: 'YYYY-DD-MM'
    });
    maxDate = new DateTime($('#max'), {
        format: 'YYYY-DD-MM'
    });
 
    // DataTables initialisation
    var table = $('#colaborador').DataTable();
 
    // Refilter the table
    $('#min, #max').on('change', function () {
        table.draw();
    });
});