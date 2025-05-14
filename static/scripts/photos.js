// fetch img urls

// loop over image urls, getting width and height

// add to flex-box (?) or grid (?) layout
// specifying that if height > width, the photo should take up two rows
// (and if width > height, two columns?)

// add element to grid

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
    gridCell.setAttribute("class", "photo-vert");
  } else {
    gridCell.setAttribute("class", "photo");
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
