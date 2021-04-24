window.onmessage = function(event) {
    const t = document.getElementsByClassName("js-plotly-plot")[0];
    const e = {
        "format": "png",
        "width": null,
        "height": null,
        "imageDataOnly": true
    };
    Plotly.downloadImage(t, e);
};
