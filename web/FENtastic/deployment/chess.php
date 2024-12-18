<?php
// Set up the mapping of FEN pieces to Unicode chess characters.
$fenToUnicode = [
    'P' => '\u2659', 'N' => '\u2658', 'B' => '\u2657', 'R' => '\u2656', 'Q' => '\u2655', 'K' => '\u2654',
    'p' => '\u265F', 'n' => '\u265E', 'b' => '\u265D', 'r' => '\u265C', 'q' => '\u265B', 'k' => '\u265A'
];

// Function to parse FEN and create a 2D array of the board.
function parseFEN($fen) {
    $board = [];
    $rows = explode('/', $fen);

    foreach ($rows as $row) {
        $boardRow = [];
        for ($i = 0; $i < strlen($row); $i++) {
            if (is_numeric($row[$i])) {
                for ($j = 0; $j < (int)$row[$i]; $j++) {
                    $boardRow[] = ' '; // Empty squares.
                }
            } else {
                $boardRow[] = $row[$i];
            }
        }
        $board[] = $boardRow;
    }
    return $board;
}

// Function to render the board overlaying the Unicode pieces on the image.
function renderChessboard($fen, $imagePath, $outputPath) {
    global $fenToUnicode;

    // Load the chessboard image.
    $image = imagecreatefrompng($imagePath);
    $fontPath = __DIR__ . '/DejaVuSans.ttf'; // Ensure you have this TTF font in your directory.

    if (!$image || !file_exists($fontPath)) {
        die("Error: Missing required resources (chessboard image or font).\n");
    }

    // Set font size and text color.
    $fontSize = 64; // Adjust size to fit 1024x1024 image.
    $color = imagecolorallocate($image, 0, 0, 0); // Black.

    // Parse the FEN.
    $board = parseFEN($fen);

    // Calculate cell size (1024px / 8 cells).
    $cellSize = 1024 / 8;

    // Loop through the board and render pieces.
    foreach ($board as $y => $row) {
        foreach ($row as $x => $piece) {
            if ($piece !== ' ') {
                if (isset($fenToUnicode[$piece])) {
                    $unicode = mb_convert_encoding('&#x' . substr($fenToUnicode[$piece], 2) . ';', 'UTF-8', 'HTML-ENTITIES');

                    // Calculate the position for text placement.
                    $xPos = $x * $cellSize + $cellSize / 4;
                    $yPos = ($y + 1) * $cellSize - $cellSize / 4;

                    // Render the piece.
                    imagettftext($image, $fontSize, 0, $xPos, $yPos, $color, $fontPath, $unicode);
                }
            }
        }
    }

    // Save the output image.
    imagepng($image, $outputPath);
    imagedestroy($image);
}

// Handle user input.
//$fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"; // Default initial board position.
$fen = "8/k1r5/p1pb4/3p4/8/q1NP4/2R4p/1K1Q4 w - - 2 44";
if (isset($_GET['fen'])) {
    $decodedFen = $_GET['fen'];
    if ($decodedFen !== false) {
        $fen = $decodedFen;
    }
}

$imagePath = 'chessboard.png';
$outputPath = 'output.png';
renderChessboard($fen, $imagePath, $outputPath);

// Generate the HTML page.
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FEN Viewer</title>
</head>
<body>
    <h1>FEN Viewer</h1>
    <form method="GET" >
        <label for="fen">Enter FEN String:</label><br>
        <input type="text" id="fen" name="fen" value="<?php echo htmlspecialchars($fen); ?>" style="width: 100%;">
        <br><br>
        <button type="submit">Generate Board</button>
    </form>
    <br>
    <h2>Generated Board:</h2>
    <img src="<?php echo $outputPath; ?>" alt="Chessboard">
</body>
<!-- the key to the challenge is the default FEN string -->
</html>
