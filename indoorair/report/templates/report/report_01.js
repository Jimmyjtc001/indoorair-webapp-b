function onPageLoadRunGetTimeSeriesDAtumReport01FromAPI() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const dataString = this.responseText;
            const dataObj = JSON.parse(dataString);;
        }
    }
    xhttp.open("GET","{% url 'report_01_page' %}", true);
    xhttp.send();
}

onPageLoadRunGetTimeSeriesDAtumReportListFromAPI();
