// Replace with your actual Spreadsheet ID
const spreadsheetId = "1tf07nkBNALTm4FzdZuj7U8TjJAHhd0Vqfdrql871Rr8";

// Replace with your API Key
const apiKey = "AIzaSyCOyCg5u_dyqHFJa6uQ0nodqRQ3rcFBsWE";

// Construct the URL for Google Sheets API v4
const url = `https://sheets.googleapis.com/v4/spreadsheets/${spreadsheetId}/values/all_books?key=${apiKey}`;

async function fetchGoogleSheetData() {
  try {
    // Fetch data from Google Sheets API
    const response = await fetch(url);
    const data = await response.json();

    // Extract rows from the data
    const rows = data.values;

    // Get the table body element
    const tableBody = document.querySelector("#data-table tbody");

    // Column key
    // 0 - Status
    // 1 - Title
    // 2 - Author
    // 3 - Type (Book club?)
    // 4 - Link
    // 5 - Review
    // 6 - Year
    // 7 - Date started
    // 8 - Date finished

    var statusMap = {
      Reading: "📌",
      "In the pile": "📚",
      DNF: "🚫",
      Finished: ""
    };

    // Loop through the rows (starting from row 1 to skip headers)
    for (let i = 1; i < rows.length; i++) {
      const row = document.createElement("tr");

      // Loop through each cell in the row and create a table cell for each
      rows[i].forEach((cell, j) => {
        var cellContents = cell;
        if (j == 0 || j == 4 || j == 7 || j == 8) {
          // skip
        } else if (j == 1) {
          // create the title
          var title = cell;
          if (rows[i][0] != "" && rows[i][0] != undefined) {
            // add emoji for status if available
            title = statusMap[rows[i][0]] + " " + cell;
            cellContents = title;
          }
          if (rows[i][4] != "" && rows[i][4] != undefined) {
            var linkElement = document.createElement("a");
            linkElement.setAttribute("href", rows[i][4]);
            linkElement.innerHTML = title + "🔗";
            cellContents = linkElement;
          }
          const cellElement = document.createElement("td");
          cellElement.append(cellContents);
          row.appendChild(cellElement);
        } else if (j == 5 && cell != undefined && cell !== "") {
          var detailsElement = document.createElement("details");
          var summaryElement = document.createElement("summary");
          summaryElement.textContent = "Read review";
          detailsElement.appendChild(summaryElement);
          var p = document.createElement("p");
          p.textContent = cell;
          detailsElement.appendChild(p);
          cellContents = detailsElement;
          const cellElement = document.createElement("td");
          cellElement.append(cellContents);
          row.appendChild(cellElement);
        } else {
          // just add the table
          const cellElement = document.createElement("td");
          cellElement.textContent = cellContents;
          row.appendChild(cellElement);
        }
      });

      // Append the row to the table
      tableBody.appendChild(row);
    }
  } catch (error) {
    console.error("Error fetching Google Sheets data:", error);
  }
}

// Call the function to fetch and display data
document.addEventListener("DOMContentLoaded", fetchGoogleSheetData);
