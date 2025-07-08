// concept: read film names and year from csv file
// construct img url from that data and get front and back image
// add the element to the grid
// give appropriate card or vertical card class

function createDynamicPictureGrid(imgUrl, description) {
  var dimensions = getImageDimensions(imgUrl, description);
}

async function getImageDimensions(src, description) {
  return new Promise((resolve) => {
    const img = new Image();
    img.src = src;
    document.body.appendChild(img);
    img.onload = () => {
      img.remove();
      addToGrid({ width: img.naturalWidth, height: img.naturalHeight }, src, description);
      resolve({})
    };
  });
}

function addToGrid(dimensions, imgUrl, description) {
  // get grid body element
  const gridParent = document.querySelector("#photo-parent");

  var gridCell = document.createElement("div"); 
  var figure = document.createElement("figure");
  var img = document.createElement("img"); 
  img.src = imgUrl;

  if (dimensions.height > dimensions.width) {
    gridCell.setAttribute("class", "grid-cell");
    img.setAttribute("class", "photo-flex-vert");
  } else {
    gridCell.setAttribute("class", "grid-cell");
    img.setAttribute("class", "photo-flex");
  }
  figure.appendChild(img)

  if (description != undefined) {
    var figCaption = document.createElement("figcaption"); // is a node
    figCaption.innerHTML = description;
    figure.appendChild(figCaption)

  }
  gridCell.appendChild(figure)
  gridParent.appendChild(gridCell);
}
