// $(document).ready(function() {
        // var table = $('#table_id').DataTable( {
        // lengthChange: false,
        // buttons: ['excel', 'pdf',]
        // } );
 
        // table.buttons().container()
        // .appendTo( '#tb_rapper .col-md-6:eq(0)' );
        // } );

    



    function getTimestamp () {
    const pad = (n,s=2) => (`${new Array(s).fill(0)}${n}`).slice(-s);
    const d = new Date();
    
    return `${pad(d.getFullYear(),4)}-${pad(d.getMonth()+1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
    }

    var date = getTimestamp();
    var fileTitle = "Funeral records "+date;
    

        $(document).ready(function() {
    $('#table_id').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                title: fileTitle
            },
            {
                extend: 'pdfHtml5',
                title: fileTitle
            }
        ]
    } );
} );
