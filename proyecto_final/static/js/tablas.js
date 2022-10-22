$('#clientes').DataTable({
    responsive: true,
    paging: true,
    pageLength:10,
    lengthChange:true,
    lengthMenu:[ [5,10, 25, 50, 100, -1], [5,10, 25, 50, 100, "Todo"] ],
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
            columns:[0,1,2,3]
            }   
        },
        {
            extend: 'excel',
            text: '<i class="fas fa-file-excel"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Excel',
            exportOptions:{
                columns:[0,1,2,3]
                }   
        },
        {
            extend: 'print',
            text: '<i class="fas fa-print"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Imprimir',
            exportOptions:{
                columns:[0,1,2,3]
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
                columns:[0,1,2,3]
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


$('#categorias').DataTable({
    responsive: true,
    paging: true,
    pageLength:10,
    lengthChange:true,
    lengthMenu:[ [5,10, 25, 50, 100, -1], [5,10, 25, 50, 100, "Todo"] ],
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
            titleAttr: 'Excel',
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
            text: '<i class="fas fa-file-pdf"></i>',
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
    lengthMenu:[ [5,10, 25, 50, 100, -1], [5,10, 25, 50, 100, "Todo"] ],
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
            titleAttr: 'Excel',
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
    lengthMenu:[ [5,10, 25, 50, 100, -1], [5,10, 25, 50, 100, "Todo"] ],
    autoWidth: true,
    searching: true,
    bInfo: true,
    bSort: true,
    fixedColumns: true,
    dom: 'lBfrtip',
    buttons:[
        {
        extend: 'copy',
        text: '<i class="fas fa-clone"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Copiar',
        footer: true,
        exportOptions:{
            columns:[1,2,3,4,5]
            }   
        },
        {
            extend: 'excel',
            text: '<i class="fas fa-file-excel"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Excel',
            footer: true,
            exportOptions:{
                columns:[1,2,3,4,5]
                }   
        },
        {
            extend: 'print',
            text: '<i class="fas fa-print"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Imprimir',
            footer: true,
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
            footer: true,
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
    },
    footerCallback: function (row, data, start, end, display) {
        var api = this.api();

        // Remove the formatting to get integer data for summation
        var intVal = function (i) {
            return typeof i === 'string' ? i.replace(/[\Q,]/g, '') * 1 : typeof i === 'number' ? i : 0;
        };

        // Total over all pages
        total = api
            .column(4)
            .data()
            .reduce(function (a, b) {
                return intVal(a) + intVal(b);
            }, 0);

        // Total over this page
        pageTotal = api
            .column(4, { page: 'current' })
            .data()
            .reduce(function (a, b) {
                return intVal(a) + intVal(b);
            }, 0);

        // Update footer
        $(api.column(4).footer()).html('Q' + pageTotal);
    }
    

})

$('#colaborador').DataTable({
    responsive: true,
    paging: true,
    pageLength:10,
    lengthChange:true,
    lengthMenu:[ [5,10, 25, 50, 100, -1], [5,10, 25, 50, 100, "Todo"] ],
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
            titleAttr: 'Excel',
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

$('#compras').DataTable({
    responsive: true,
    paging: true,
    pageLength:10,
    lengthChange:true,
    lengthMenu:[ [5,10, 25, 50, 100, -1], [5,10, 25, 50, 100, "Todo"] ],
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
        footer: true,
        exportOptions:{
            columns:[1,2,3,4,5]
            }   
        },
        {
            extend: 'excel',
            text: '<i class="fas fa-file-excel"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Excel',
            footer: true,
            exportOptions:{
                columns:[1,2,3,4,5]
                }   
        },
        {
            extend: 'print',
            text: '<i class="fas fa-print"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Imprimir',
            footer: true,
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
            footer: true,
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
    },
    footerCallback: function (row, data, start, end, display) {
        var api = this.api();

        // Remove the formatting to get integer data for summation
        var intVal = function (i) {
            return typeof i === 'string' ? i.replace(/[\Q,]/g, '') * 1 : typeof i === 'number' ? i : 0;
        };

        // Total over all pages
        total = api
            .column(4)
            .data()
            .reduce(function (a, b) {
                return intVal(a) + intVal(b);
            }, 0);

        // Total over this page
        pageTotal = api
            .column(4, { page: 'current' })
            .data()
            .reduce(function (a, b) {
                return intVal(a) + intVal(b);
            }, 0);

        // Update footer
        $(api.column(4).footer()).html('Q' + pageTotal);
    }
})

$('#proveedor').DataTable({
    responsive: true,
    paging: true,
    pageLength:10,
    lengthChange:true,
    lengthMenu:[ [5,10, 25, 50, 100, -1], [5,10, 25, 50, 100, "Todo"] ],
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
        footer: true,
        exportOptions:{
            columns:[0,1,2,3,5]
            }   
        },
        {
            extend: 'excel',
            text: '<i class="fas fa-file-excel"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Excel',
            footer: true,
            exportOptions:{
                columns:[0,1,2,3,5]
                }   
        },
        {
            extend: 'print',
            text: '<i class="fas fa-print"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Imprimir',
            footer: true,
            exportOptions:{
                columns:[0,1,2,3,5]
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
            footer: true,
            exportOptions:{
                columns:[0,1,2,3,4,5]
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
    },
    footerCallback: function (row, data, start, end, display) {
        var api = this.api();

        // Remove the formatting to get integer data for summation
        var intVal = function (i) {
            return typeof i === 'string' ? i.replace(/[\Q,]/g, '') * 1 : typeof i === 'number' ? i : 0;
        };

        // Total over all pages
        total = api
            .column(3)
            .data()
            .reduce(function (a, b) {
                return intVal(a) + intVal(b);
            }, 0);

        // Total over this page
        pageTotal = api
            .column(3, { page: 'current' })
            .data()
            .reduce(function (a, b) {
                return intVal(a) + intVal(b);
            }, 0);

        // Update footer
        $(api.column(3).footer()).html('Q' + pageTotal);
    }
})

$('#proveedores').DataTable({
    responsive: true,
    paging: true,
    pageLength:10,
    lengthChange:true,
    lengthMenu:[ [5,10, 25, 50, 100, -1], [5,10, 25, 50, 100, "Todo"] ],
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
            columns:[1,2,3]
            }   
        },
        {
            extend: 'excel',
            text: '<i class="fas fa-file-excel"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Excel',
            exportOptions:{
                columns:[1,2,3]
                }   
        },
        {
            extend: 'print',
            text: '<i class="fas fa-print"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Imprimir',
            exportOptions:{
                columns:[1,2,3]
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
                columns:[1,2,3]
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
        if ($('#min').val() != '') {
            var min = new Date($('#min').val());
        } else {
            var min = null;
        }
        if ($('#max').val() != '') {
            var max = new Date($('#max').val());
        } else {
            var max = null;
        }
        var date = new Date( data[5] );
        
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

    // DataTables initialisation
    var table = $('#servicios').DataTable();
    var table2 = $('#compras').DataTable();
    var table3 = $('#proveedor').DataTable();
    // Refilter the table
    $('#min, #max').on('change', function () {
        table.draw();
        table2.draw();
        table3.draw();
    });
});