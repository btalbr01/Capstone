<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homes List</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
    <script>
        //function to sort by ascending or descending prices
        function sortByPrice(ascending) {
            var rows = document.querySelectorAll("tbody tr");
            var sortedRows = Array.from(rows).sort((a, b) => {
                var priceA = parseFloat(a.children[1].innerText.replace("$", "").replace(/,/g, ""));
                var priceB = parseFloat(b.children[1].innerText.replace("$", "").replace(/,/g, ""));
                return ascending ? priceA - priceB : priceB - priceA;
            });
            var tbody = document.querySelector("tbody");
            tbody.innerHTML = "";
            sortedRows.forEach(row => tbody.appendChild(row));
        }
    </script>
</head>
<body>
    <h2>Homes List</h2>
    <!--text boxes for user input. defaults to 0-->
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
    <label for="minPrice">Minimum Price:</label>
    <input type="text" id="minPrice" name="minPrice" value="0">
    <label for="maxPrice">Maximum Price:</label>
    <input type="text" id="maxPrice" name="maxPrice" value="9999999">
    <br>
    <label for="minBeds">Minimum Beds:</label>
    <input type="text" id="minBeds" name="minBeds" value="0">
    <label for="minBaths">Minimum Baths:</label>
    <input type="text" id="minBaths" name="minBaths" value="0">
    <label for="minArea">Minimum Area (sqft):</label>
    <input type="text" id="minArea" name="minArea" value="0">
    <input type="submit" value="Filter">
    <br>
</form>
    <!--buttons to sort by price-->
    <button onclick="sortByPrice(true)">Sort by Price (Ascending)</button>
    <button onclick="sortByPrice(false)">Sort by Price (Descending)</button>
    <table>
        <thead>
            <tr>
                <th>Address</th>
                <th>Price</th>
                <th>Beds</th>
                <th>Baths</th>
                <th>Area</th>
                <th>Measurement</th>
                <th>Property Type</th>
                <th>Source</th>
                <th>URL</th>
            </tr>
        </thead>
        <tbody>
            <?php
//database connection parameters
$servername = "localhost"; 
$username = "root"; 
$password = ""; 
$database = "properties";

//create connection
$conn = new mysqli($servername, $username, $password, $database);

//check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

//initialize variables to store minimum and maximum prices
$minPrice = $maxPrice = "";
$category = isset($_POST['category']) ? $_POST['category'] : 'homes';

//check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve minimum and maximum prices from the form
    $minPrice = $_POST["minPrice"];
    $maxPrice = $_POST["maxPrice"];
    $minBeds = isset($_POST["minBeds"]) ? $_POST["minBeds"] : 0;
    $minBaths = isset($_POST["minBaths"]) ? $_POST["minBaths"] : 0;
    $minArea = isset($_POST["minArea"]) ? $_POST["minArea"] : 0;

    //SQL query to fetch data based on the selected category and filter parameters
    if ($category == 'homes') {
        $sql = "(SELECT Address, Price, Beds, Baths, Area, Measurement, `Property Type`, 'Zillow' AS Source, URL FROM zillow_homes WHERE Price BETWEEN $minPrice AND $maxPrice AND Beds >= $minBeds AND Baths >= $minBaths AND Area >= $minArea)
                UNION
                (SELECT Address, Price, Beds, Baths, Area, Measurement, `Property Type`, 'Realtor' AS Source, URL FROM realtor_homes WHERE Price BETWEEN $minPrice AND $maxPrice AND Beds >= $minBeds AND Baths >= $minBaths AND Area >= $minArea)";
    } elseif ($category == 'land') {
        $sql = "(SELECT * FROM zillow_land WHERE Price BETWEEN $minPrice AND $maxPrice)
                UNION
                (SELECT * FROM realty_land WHERE Price BETWEEN $minPrice AND $maxPrice)";
    }

    $result = $conn->query($sql);

    //output data of each row
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo "<tr>";
            foreach ($row as $key => $value) {
                if ($key == 'URL') {
                    echo "<td><a href='" . $value . "'>" . $value . "</a></td>";
                } else {
                    echo "<td>" . $value . "</td>";
                }
            }
            echo "</tr>";
        }
    } else {
        echo "<tr><td colspan='9'>No results found</td></tr>";
    }
}


//close connection
$conn->close();
?>


        </tbody>
    </table>
</body>
</html>
